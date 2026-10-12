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
