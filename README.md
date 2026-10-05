# Kinetic-Home-Experiment
Kinetic Home is more than robotic furniture. It is an architectural system designed for human living. This repository contains on-device AI experiments for kinetic systems. Come and join us.

# Kinetic Home — Research Foundations and Architecture, Source Code, and Design Guidelines

> The purpose of Kinetic Home is to solve everyday problems that cause residents inconvenience and fatigue, while preserving their agency to judge, choose, and act within their own homes.

| Document Information | Details |
| --- | --- |
| Document ID | KH-GUIDE |
| Version / Date | 0.1 / 2026-10-05 |
| Document Status | A reference document that establishes the purpose, problem, and research scope specified by the user and prepares the ground for concrete design decisions |
| Applies To | Spatial, mechanical, control, and software architecture; source code; product and interaction design |
| Project Naming | This document uses Kinetic Home. The name Kinetic House is retained when referring to the original source. |
| Basis | Notion Elog #001 and the user's document requirements dated 2026-10-05 |
| Current Limitations | Rail and elevator concepts and logic, detailed structures, technology stack, and performance figures remain undecided |

## 1. Purpose of This Document and How to Read It

This is a single reference document that helps people review the research evidence and design direction, and helps AI analyze, design, and implement within the same boundaries. It distinguishes establishing the problem definition from finalizing a solution. Completing this document does not mean that detailed designs have been approved or that product validation is complete.

### 1.1 Status Labels and Requirement Levels

| Label | Meaning | How to Use It |
| --- | --- | --- |
| Established | The purpose, problem definition, or research scope explicitly specified by the user | Retain it as a basis for subsequent work. |
| Recorded | Everyday activity records and retrospective statements confirmed in Elog #001 | Cite the conditions and limitations of the record alongside it. |
| Analysis | An interpretation derived in the source or in this document | Do not present it as an observed fact or a validated result. |
| Undecided | An item that still requires selection, definition, or measurement | Do not implement it as an established value or operating method. |
| Proposal | A design, research, or validation method developed in this document | Compare it as a candidate and record whether it is adopted. |

**Required** identifies a boundary that work using this document must respect. **Recommended** identifies a working method that can be adjusted to suit the purpose. Structures and examples labeled as proposals are not mandatory implementation specifications. Unless otherwise labeled, the detailed guidelines in Sections 5–8 are criteria derived in this document to connect the user's purpose to design and development; they do not indicate that the user has approved detailed designs.

### 1.2 Document Map

- Section 2: Project purpose and established scope
- Section 3: Observations, analysis, and evidence limitations in Elog #001
- Section 4: Open questions and research tasks for the rail and elevator systems
- Section 5: Spatial, mechanical, and software architecture guidelines
- Section 6: Source code guidelines
- Section 7: Product and interaction design guidelines
- Section 8: Validation and conditions for finalizing designs
- Section 9: Document usage rules for people and AI
- Section 10: Sources and change history

## 2. Project Purpose and Established Scope

### P-01. Reduce Residents' Inconvenience and Fatigue — Established

Problem solving should address the burdens residents experience in everyday life. Examine the complete process of finding a place to store an item, retrieving it, using it, returning it, and finding it again for the next use. Include any additional organizing, operation, waiting, and maintenance required to use the system in the evaluation.

### P-02. Preserve Residents' Agency Within Their Homes — Established

Residents are the decision makers regarding their way of living, where and when they use their belongings, and the extent of assistance they receive. The system must support their judgment and actions. Greater automation or convenience for the system must not be treated as an automatic justification for reducing residents' choices.

This document defines agency as **the ability to understand a situation, choose or decline assistance, intervene in an ongoing process, and adapt it to one's own way of living**. The specific means of interaction will be determined through subsequent design and validation.

### P-03. Address the Mismatch Between Diverse Everyday Items and Storage Cabinets as a Core Problem — Established

Everyday items stored in or used with furniture—such as suitcases, bags, books, and earphones—vary widely in size and form. The research starts from the personal experience of recurring fatigue caused by storing these items in the cabinets that must accommodate them.

Design must therefore address item diversity, how cabinets accommodate items, and the actions of storing and retrieving them together. Increased storage capacity or additional free space alone must not be treated as proof that the problem has been solved.

### P-04. Treat Rails and Elevators as Principal Systems for Research — Research Scope Established / Solution Undecided

Research rails and elevators as principal systems for use in Kinetic Home. However, **the logic and concepts of both systems have not yet been finalized.** Research and ideation are needed on their placement, what they move, transport and handoff methods, control sequences, and the user experience.

In this document, elevator is a working term for discussing vertical transport. Its purpose, specifications, and structure—including whether it carries people—are not established. The decision to research rails and elevators does not constitute approval of a particular mechanism or fully automatic operation.

## 3. Observations and Analysis from Elog #001

**Source:** [S1 — Elog #001 — Kinetic House Research](https://app.notion.com/p/3ed3350629a681578462eb4a28e66bea). The following summarizes the source's Question, Observation, Friction Mapping, summary for the Concept chapter, and closing decision, as reviewed on 2026-10-05.

### 3.1 Actual Daily Routines and Repeated Actions — Recorded

| ID | Content Confirmed in the Source | Nature of the Evidence |
| --- | --- | --- |
| OBS-01 | Wake up → check routine → breakfast → bathe → change clothes → prepare to go out | Daily routine recorded by the user |
| OBS-02 | Return home → put down bag, phone, wallet, and accessories → change into pajamas → wash face and brush teeth → personal activities → sleep | Daily routine recorded by the user |
| OBS-03 | Repeatedly take out or put away bags, clothes, writing tools, a phone, and accessories. | Everyday record of repeated actions |
| OBS-04 | Struggle to find a place to put a bag. | A specific record of friction between space and action |
| OBS-05 | Forget where the wallet, earphones, or phone are and search for them before going out. | A record of friction when retrieving belongings |
| OBS-06 | Bags, a laptop, an iPad, a chair, a desktop computer, and other items occupy space even when not in use. | A record of space occupancy; whether each item actually causes an obstruction requires separate confirmation |
| OBS-07 | Have repeatedly felt fatigue in the relationship between storage cabinets and the need to store differently sized and shaped items, including suitcases, bags, books, and earphones. | A personal retrospective statement documented on 2026-10-05 |

These records contain no measurements of dimensions, duration, or counts linked to a specific observation date, time, location, and conditions. In particular, OBS-07 is a retrospective account of repeated experiences and must not be interpreted as the result of field measurements performed that day. [S1]

### 3.2 Problem Definition and Analysis Derived in the Source — Analysis / Problem Selection Established

- **Core friction:** The fatigue of fitting everyday items of varying sizes and forms into existing storage cabinets. Finding a place for a bag is a concrete example of this problem.
- **Representative scenario:** The process from putting down a bag and personal belongings after returning home to gathering them for the next outing. The problem scope also includes items with different sizes and forms, such as suitcases and books.
- **Research question:** When storing and retrieving everyday items of different sizes and forms, what should storage space help with, and how, to reduce residents' fatigue?
- **Established scope:** This problem was selected as the core research topic based on repeated personal experience and existing daily activity records. Elog #001 concluded by establishing the problem definition.
- **Generalization hypothesis:** This problem may also be a significant bottleneck in other single-person households. Its prevalence, severity, and conditions of occurrence have not yet been validated. [S1]

### 3.3 What the Current Evidence Cannot Establish

| ID | What Has Not Yet Been Confirmed | Proposed Follow-up |
| --- | --- | --- |
| GAP-01 | Dimensions of individual items and actual storage cabinet specifications | Pair each item with its storage location and measure both. |
| GAP-02 | Storage and retrieval times, frequency of occurrence, number of movements, and degree of fatigue | Record the current approach in the representative scenario to establish a comparison baseline. |
| GAP-03 | Whether differences in size and form cause difficulty finding items | Distinguish possible causes, such as insufficient space, items being hidden, memory, and changes in placement. |
| GAP-04 | Whether the same problem occurs in other single-person households | Separately examine the experiences of people with different living conditions. |
| GAP-05 | Whether robotics, adjustable storage, rails, automation, or AI reduce fatigue | Conduct the smallest useful comparative experiment for each candidate. |
| GAP-06 | Original sources, confirmed functions, and application settings for the Ori case study | Record original materials and review dates, and distinguish these from interpretation. |

The Ori-related fields in Elog #001 are incomplete. `Furniture → Interior → Apartment → Architecture` is an interpretive framework for the research, not a substantiated conclusion about Ori's business scope or achievements. The guidance dated 2026-10-03 preserved in the source is also guidance written before the work, not a record of results. [S1]

### 3.4 Design Interpretation in This Document — Analysis

Use the relationship between **items ↔ storage cabinets ↔ residents' actions** as the unit of research. Even for the same item, the burden may vary depending on when it is used, where it is returned, and the posture needed to access it. This is a design perspective derived from OBS-03–07, not a solution with proven effectiveness.

## 4. Research and Ideation for Rails and Elevators

### 4.1 Open Questions

| ID | Question to Resolve | Current Status |
| --- | --- | --- |
| OPEN-01 | What moves: an individual item, a tray, a storage module, or an entire piece of furniture? | Undecided |
| OPEN-02 | Where are rails placed, and in which directions and along which routes does movement occur? | Undecided |
| OPEN-03 | What does the elevator move, to what height, and how does it hand off to or from the rail system? | Undecided |
| OPEN-04 | Which item sizes, forms, and weights can be accommodated, and how are unsupported items handled? | Undecided |
| OPEN-05 | Does a person request an action, does the system suggest it, or does it execute automatically under specified conditions? | Undecided |
| OPEN-06 | How are movement order, route occupancy, simultaneous requests, interruption, and resumption handled? | Undecided |
| OPEN-07 | What state is maintained or restored when there is an obstacle, a failed handoff, uncertain position, or loss of power? | Undecided |
| OPEN-08 | Is the system more beneficial than current storage once installation, cleaning, and maintenance burdens are included? | Unvalidated |

### 4.2 Concept Candidates — Proposals, Not Adopted Concepts

The candidates below are examples to begin comparison. Do not establish horizontal rails combined with a vertical elevator as the default design, or treat any candidate as the actual system.

| Candidate | Concept to Explore | Uncertainty to Examine First |
| --- | --- | --- |
| IDEA-01 | Transfer trays or modules containing items between a rail system and a vertical transport unit | Accommodation of diverse items, securing and handing them off, and ease of retrieval after transport |
| IDEA-02 | Move part of a storage cabinet to an accessible position or height | The need to move furniture, surrounding circulation paths, total load, and spatial burden |
| IDEA-03 | Combine adjustment of storage locations with limited transport assistance | Whether storage and retrieval fatigue can be reduced sufficiently with lower complexity |
| BASE-01 | Current storage practices and alternatives without powered motion, such as adjustable dividers or improved placement | A baseline for judging whether a robotic system provides enough benefit to justify its additional burdens |

### 4.3 Suggested Research Sequence — Recommended

1. Pair different items, such as suitcases, bags, books, and earphones, with their actual storage locations and record them.
2. Identify the difficult actions and their causes for each pairing. Examples include finding a place, changing posture, moving other items, and returning an item.
3. Decide which action to assist, and compare rail and elevator candidates with alternatives without powered motion in the same scenario.
4. Select one question with the greatest uncertainty and investigate it at a small scale using a paper model, manually operated model, simulation, or similar method.
5. Record both observed improvements and newly introduced burdens, then decide what to retain, revise, or defer.

Following this research sequence or building models does not mean that the feasibility of the physical actuation structure has been validated.

## 5. Architecture Guidelines

### ARC-01. Represent Items, Storage, and Actions Together — Required

Do not assume that all items are identically sized boxes or represent a storage cabinet solely by a capacity figure. Investigate the properties that are actually needed and reflect them in the model. Keep unmeasured values explicitly unmeasured.

**Example properties to investigate — Proposal:** Item shape, orientation, weight, deformability, and frequency of use; storage openings, interior space, access height, and retrieval clearance; items stored together; and conditions that must be maintained during movement. Storage suitability includes whether an item can be retrieved and returned, as well as whether it fits.

### ARC-02. Separate Everyday Goals from Actuation Methods — Required

Treat “access the belongings needed to go out” and “drive particular motors in a particular sequence” as separate responsibilities. Preserve the everyday scenarios and evaluation criteria even if the rail and elevator concepts change.

| Proposed Responsibility | What It Covers |
| --- | --- |
| Everyday scenarios | Who requests assistance, when, and for what purpose |
| Item and storage model | Which items are where, and under what conditions they can be stored and retrieved |
| Motion planning | Sequences, routes, and handoff conditions needed to reach a target state |
| Actuation integration | Connections between the selected rail and elevator systems, sensors, and actuators |
| State and intervention management | Current progress, resident requests, interruption conditions, failures, and recovery possibilities |

This division is a proposal for examining responsibilities. It does not establish the number of services or processes, the folder structure, or communication methods.

### ARC-03. Include Resident Intervention in Normal Operation — Required

Treat requesting, declining, changing, and stopping assistance as normal usage situations. If a cancellation request arrives during movement, define how the system transitions to a safe state with consideration for its current position, load, and other relevant conditions. Do not assume that stopping simply means immediately cutting power. Validate specific stopping, holding, and recovery methods through mechanical research.

### ARC-04. Design for Situations in Which Operation Is Not Possible — Required

Distinguish what the system knows and what it cannot do when an item cannot be accommodated, a route is blocked, a position is unknown, or a handoff fails. If the conditions for continued operation have not been confirmed, do not treat the situation as normal progress. Alternative ways for residents to access their belongings and recovery procedures remain tasks for subsequent design.

## 6. Source Code Guidelines

This section sets criteria for source code to be written in the future. It does not describe existing implementations or an established technology stack.

| ID | Level | Guideline |
| --- | --- | --- |
| CODE-01 | Required | Do not conceal undecided specifications, values, or logic as finalized requirements. Identify the source, scope of application, and potential for change of assumptions needed for experiments. |
| CODE-02 | Required | Separate responsibilities so that everyday scenarios and item and storage models do not depend directly on a particular actuator or temporary mechanical layout. |
| CODE-03 | Required | Distinguish requested states, observed states, and unknown states. Do not record movement or handoff as complete merely because a command was sent. |
| CODE-04 | Required | Make condition checks, execution, completion confirmation, failure handling, and user intervention explicit. Determine state names and transition logic according to the selected concept. |
| CODE-05 | Required | Do not replace unknown item sizes, positions, or accommodation status with arbitrary normal values. Make the policy for handling uncertain states explicit. |
| CODE-06 | Required | Distinguish simulations, mock data, and physical measurements. Do not report model or software validation as validation of physical performance or safety. |
| CODE-07 | Recommended | Record necessary state changes and reasons for failure so that experimental conditions and observations can be reviewed. Limit personal daily activity records to what is needed for evaluation. |
| CODE-08 | Recommended | Include relevant principle and research question IDs and the scope of validation in change descriptions. Examples: P-02, OPEN-06, ARC-03. |

**Proposed validation scenarios for future implementation:** An item whose size cannot be accommodated, simultaneous requests, intervention during movement, failed handoff confirmation, loss of position information, and recovery after interruption. Define exact expected behavior and acceptance criteria in the decision record for the relevant concept.

## 7. Product and Interaction Design Guidelines

### DES-01. Reduce the Fatigue of Receiving Assistance Itself — Required

If the system requires complicated registration for each item, repacking into a separate container for every use, or multiple operations to store something, count that burden against its benefits. Evaluate the entire sequence from preparation to returning an item after use. [P-01, P-03]

### DES-02. Accommodate Item Diversity and Changes in Daily Life — Required

Consider different sizes and forms, as well as situations in which new items arrive or belongings are put down temporarily. Do not assume that all everyday items must fit a single standard container. If common containers or modules are proposed, examine their accommodation range, exceptions, and additional organizing burden together. [P-03, ARC-01]

### DES-03. Enable Residents to Understand and Intervene in System Behavior — Required

Residents should be able to understand what is moving, why the system is waiting, whether they can decline assistance, and how to change what is happening. Adjust the volume of notifications and confirmation procedures so that they do not increase everyday fatigue. If automatic execution is adopted, first define its permitted scope and how residents can disable it or intervene. [P-02, ARC-03]

### DES-04. Evaluate Space Occupancy and Movement Within Everyday Scenarios — Required

Do not judge inconvenience solely by the floor area occupied by furniture. Check whether it actually interferes with circulation, access to items, rest, or work. Consider waiting caused by movement, noise, visual burden, cleaning, and maintenance as evaluation topics. Do not describe these burdens as having been measured in the current observations. [OBS-06, OPEN-08]

### DES-05. Connect Appearance and Presentation to Everyday Value and Mechanical Research — Recommended

Form, color, materials, exposed structure, and control placement remain undecided. Include the usage scenario, burden to be reduced, residents' choices, and mechanical assumptions with each design proposal. Do not substitute presentation images for evidence of build feasibility or usability validation.

## 8. Validation and Conditions for Finalizing Designs

### 8.1 Comparison Records — Proposal

| Evaluation Dimension | What to Record | Current Status |
| --- | --- | --- |
| Physical burden | Number of movements, posture changes, and difficult actions such as lifting or pulling | Baseline and target values undecided |
| Cognitive burden | Choosing a storage place, finding items, interpreting system state, and performing additional operations | Baseline and target values undecided |
| Time and flow | Storage and retrieval time, waiting, and interruptions to everyday routines | Baseline and target values undecided |
| Storage accommodation | The range of different items that can be placed, retrieved, and returned | Target items and dimensions not yet measured |
| Agency | Ability to decline assistance, change progress or placement, and make choices in exceptional situations | Scenarios and assessment criteria undecided |
| Maintenance burden | Effort required for installation, cleaning, reconfiguration, access during failures, and recovery | Baseline and target values undecided |

Use the same items and everyday scenarios when comparing candidates wherever possible, and record any differences in conditions. A reduction in elapsed time can still increase the fatigue of operating the system, so do not declare success based on a single metric.

### 8.2 Checklist Before Finalizing Detailed Designs

- [ ] The target everyday scenario and item–cabinet pairings are documented concretely.
- [ ] The burden to be reduced and comparison baseline are explicit.
- [ ] Rail and elevator transport targets, routes, handoff methods, and control concepts have been compared and selected.
- [ ] Residents' means of choosing, declining, and intervening have been designed.
- [ ] Size and form exceptions and situations in which operation is not possible have been addressed.
- [ ] Evidence is distinguished from unvalidated claims, and the level of validation is not overstated.
- [ ] Adopted and deferred options, reasons for selection, and the decision maker are recorded.

This checklist is not currently complete. When changing a proposal to established status, record the user's explicit decision or the decision-making authority granted for that work as the basis.

### 8.3 Decision Record Template — Recommended

Record each decision using the following fields. For missing information, write `Undecided` or `Unvalidated` rather than inventing content.

- Decision ID / date / status:
- Related principle, observation, and research question IDs:
- Problem to solve and usage scenario:
- Candidates compared and current approach:
- Selected option / deferred options / reasons:
- Experimental and observational evidence and validation scope:
- Effects on residents' fatigue and agency:
- Remaining assumptions and constraints / conditions for reconsideration:
- Decision maker and supporting confirmation:

## 9. Document Usage Rules for People and AI

### 9.1 AI Working Instructions

1. Before starting work, review P-01–04 and the relevant OBS, GAP, and OPEN entries.
2. Cite stable IDs when referring to evidence and guidelines. Keep observations, analysis, proposals, and established decisions distinct.
3. Do not arbitrarily turn undecided rail and elevator details into final specifications. Label assumptions used for comparison as assumptions.
4. For new architecture, code, and design proposals, state the burden being addressed, residents' choices, the validation method, and remaining uncertainties.
5. When adding external case studies, distinguish original sources, review dates, directly confirmed facts, and interpretations. Do not fill incomplete Elog fields with claims of completed work.
6. Identify conflicting entries when a conflict exists. If the user's subsequent explicit instructions change an existing decision, update the relevant guidelines and change history together.
7. When reporting results, distinguish document preparation, simulation checks, and physical validation.
8. **Do not perform Git commits or pushes without separate, explicit instructions from the user.**

### 9.2 Structure and Typography

- **Single reference:** Do not initially split the document into separate versions for people and AI. Keep explanations and actionable guidelines together to reduce the risk of divergent criteria.
- **Structure:** Use one H1 title, H2 headings for major sections, and H3 headings for subsections. Use short paragraphs and tables for comparisons.
- **Traceability:** Retain IDs such as P, OBS, GAP, OPEN, ARC, CODE, and DES. When an entry changes, record the change in meaning and its basis in the change history.
- **File format:** Use UTF-8 Markdown. Do not place essential instructions exclusively in images, colors, or collapsed areas.
- **GitHub presentation:** Use GitHub's default typefaces for body text and headings, and reserve monospace formatting for code and identifiers. Do not attempt to force GitHub fonts, font sizes, or line spacing through a plain Markdown document.
- **Recommended local viewing settings:** A sans-serif body typeface that supports Korean, a body size of around 16px, and a line height of around 1.6 can be configured in the viewer. These are recommendations for the viewing environment, not fixed styles applied to the document.
- **Scope:** These typography rules apply to reading the document. They do not establish the typefaces or design system for the Kinetic Home product UI.

## 10. Sources and Change History

### Sources

- **[S1]** [Elog #001 — Kinetic House Research](https://app.notion.com/p/3ed3350629a681578462eb4a28e66bea) — Notion, reviewed on 2026-10-05. Source last edited: 2026-10-05 12:45:13 KST. The Question, Observation, Friction Mapping, summary for the Concept chapter, and closing decision were used as evidence. Empty measurement and case research fields in the source are reflected as work not yet performed.
- **[S2]** Direct user requirements — 2026-10-05, the request to create this document. The user specified the need to research rail and elevator logic and concepts; the problem of diverse everyday items and storage cabinets; reducing inconvenience and fatigue while preserving agency; Markdown usable by both people and AI; and the prohibition on commits or pushes without instruction.

S1 is the source of the research record, and S2 defines the requirements for this work. This document reflects both S1's position that solutions remain undecided and S2's designation of rails and elevators as principal research subjects. The candidates, structures, and validation methods added by this document are proposals for advancing design, not independently sourced empirical results.

### Change History

| Version | Date | Changes |
| --- | --- | --- |
| 0.1 | 2026-10-05 | Summarized the records and limitations of Elog #001 and documented the user's purpose, research scope, and architecture, code, and design guidelines. Detailed designs remain undecided. |
