#include <stdio.h>
#include <math.h>
#include <stdbool.h>

typedef enum {
	Rail_Locked,
	Rail_Unlocking,
	Rail_Moving,
	Rail_Locking,
	Rail_Fault
} RailState;	

typedef struct {
	float mass_kg;
	float position_mm;
	float target_mm;
	float velocity_mm_per_s;
	float max_speed_mm_per_s;
	float torque_Nm;
	bool brake_locked;
	RailState state;
} RailModule;

static float clamp(float x, float lo, float hi) {
	return fminf(hi, fmaxf(lo, x));
}

static float calculated_speed_limit(float mass_kg){
	return clamp(100.0f -10.0f * mass_kg, 20.0f, 80.0f);
}

static float estimated_torque(float mass_kg, float acceleration_m_per_s2){
	return mass_kg * acceleration_m_per_s2 * 9.81f; // F = m * a, torque is proportional to force
}

static void rail_update(RailModule *m, float dt) {
	switch (m->state) {
		case Rail_Locked:
			if (!m->brake_locked) {
				m->state = Rail_Unlocking;
			}
			break;
		case Rail_Unlocking:
			if (m->brake_locked) {
				m->state = Rail_Locked;
			} else {
				m	->state = Rail_Moving;
			}
			break;
		case Rail_Moving:
			if (fabsf(m->position_mm - m->target_mm) < 1.0f) {
				m->state = Rail_Locking;
			} else {
				float speed_limit = calculated_speed_limit(m->mass_kg);
				if (fabsf(m->velocity_mm_per_s) > speed_limit) {
					m->velocity_mm_per_s = copysignf(speed_limit, m->velocity_mm_per_s);
				}
				m->position_mm += m->velocity_mm_per_s * dt;
			}
			break;
		case Rail_Locking:
			if (m->brake_locked) {
				m->state = Rail_Locked;
			} else {
				m->state = Rail_Fault;
			}
			break;
		case Rail_Fault:
			break; // Handle fault condition
	}
}

int main (void) {
	RailModule plant = {
		.mass_kg = 5.0f,
		.position_mm = 0.0f,
		.target_mm = 100.0f,
		.velocity_mm_per_s = 0.0f,
		.max_speed_mm_per_s = 50.0f,
		.torque_Nm = 0.0f,
		.brake_locked = true,
		.state = Rail_Locked
	};

	float dt = 0.1f; // Time step in seconds

	for (int i = 0; i < 100; ++i) {
		if (i == 10) {
			plant.brake_locked = false; // Unlock the brake after 1 second
		}
		if (i == 80) {
			plant.brake_locked = true; // Lock the brake after 8 seconds
		}

		rail_update(&plant, dt);
		
		printf("Time: %.1fs, Position: %.2fmm, Velocity: %.2fmm/s, State: %d\n", 
		       i * dt, plant.position_mm, plant.velocity_mm_per_s, plant.state);
		
		if (plant.state == Rail_Fault) {
			printf("Rail is in fault state!\n");
			break;
		}
	}

	return 0;
}
