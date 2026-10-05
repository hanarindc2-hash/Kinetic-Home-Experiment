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


# Kinetic Home — 연구 기반과 아키텍처·소스코드·디자인 가이드라인

> 키네틱 홈의 목적은 생활 속 문제를 해결해 거주자의 불편과 피로를 줄이면서, 거주자가 자신의 집에서 판단하고 선택하고 행동하는 주체성을 유지하도록 돕는 것이다.

| 문서 정보 | 내용 |
| --- | --- |
| 문서 ID | KH-GUIDE |
| 버전 / 작성일 | 0.1 / 2026-10-05 |
| 문서 상태 | 사용자 지정 목적·문제·연구 범위를 고정하고, 구체적인 설계 결정을 준비하는 기준 문서 |
| 적용 대상 | 공간·기구·제어·소프트웨어 아키텍처, 소스코드, 제품·인터랙션 디자인 |
| 프로젝트 명칭 | 이 문서는 Kinetic Home / 키네틱 홈을 사용한다. 원문 자료의 Kinetic House 명칭은 출처에서 유지한다. |
| 근거 | Notion Elog #001과 2026-10-05 사용자 문서 작성 요구사항 |
| 현재 한계 | 레일·엘리베이터의 컨셉과 로직, 상세 구조, 기술 스택, 성능 수치는 미확정 |

## 1. 문서의 역할과 읽는 방법

이 문서는 사람이 연구의 근거와 설계 방향을 검토하고, AI가 같은 경계 안에서 분석·설계·구현하도록 돕는 단일 기준 문서다. 문제 정의를 고정하는 일과 해결 방법을 확정하는 일을 구분한다. 문서 작성 완료는 상세 설계 승인이나 제품 검증 완료를 의미하지 않는다.

### 1.1 상태와 지침의 강도

| 표기 | 의미 | 활용 방법 |
| --- | --- | --- |
| 확정 | 사용자가 명시한 목적·문제 정의·연구 범위 | 이후 작업의 기준으로 유지한다. |
| 기록 | Elog #001에서 확인한 생활 기록과 회고 진술 | 기록의 조건과 한계를 함께 인용한다. |
| 분석 | 원문 또는 이 문서에서 도출한 해석 | 관찰 사실이나 검증 결과로 바꾸어 쓰지 않는다. |
| 미확정 | 선택·정의·측정이 아직 필요한 사항 | 결정된 값이나 작동 방식처럼 구현하지 않는다. |
| 제안 | 이 문서에서 구체화한 설계·연구·검증 방법 | 후보로 비교하고 채택 여부를 기록한다. |

지침의 **필수**는 이 문서를 적용하는 작업에서 지켜야 할 경계이며, **권장**은 목적에 맞게 조정할 수 있는 작업 방법이다. 제안으로 표시된 구조나 예시는 필수 구현 사양이 아니다. 별도 표시가 없는 5~8장의 세부 지침은 사용자 목적을 설계와 개발에 연결하기 위해 이 문서에서 도출한 기준이며, 사용자가 상세 설계를 승인했다는 뜻이 아니다.

### 1.2 문서 지도

- 2장: 프로젝트 목적과 확정 범위
- 3장: Elog #001의 관찰·분석·근거 한계
- 4장: 레일·엘리베이터의 미확정 사항과 연구 과제
- 5장: 공간·기구·소프트웨어 아키텍처 지침
- 6장: 소스코드 작성 지침
- 7장: 제품·인터랙션 디자인 지침
- 8장: 검증과 설계 확정 조건
- 9장: 사람과 AI의 문서 활용 규칙
- 10장: 출처와 변경 이력

## 2. 프로젝트 목적과 확정 범위

### P-01. 거주자의 불편과 피로를 줄인다 — 확정

문제해결의 대상은 거주자가 실제 생활에서 겪는 부담이다. 물건을 보관할 자리를 찾고, 꺼내고, 사용하고, 되돌려놓고, 다음 사용 때 다시 찾는 과정을 함께 살핀다. 시스템을 사용하기 위해 추가로 드는 정리·조작·대기·관리의 부담도 평가에 포함한다.

### P-02. 주거 안에서 거주자의 주체성을 유지한다 — 확정

거주자는 생활방식, 물건의 배치와 사용 시점, 도움을 받을 범위를 결정하는 주체다. 시스템은 거주자의 판단과 행동을 보조해야 한다. 자동화 수준이나 시스템 편의를 이유로 거주자의 선택권을 당연히 축소해서는 안 된다.

이 문서에서 주체성은 **상황을 이해하고, 도움을 선택하거나 거절하고, 진행에 개입하고, 자신의 생활방식에 맞게 바꿀 수 있는 능력**으로 구체화한다. 그 구체적인 조작 방식은 후속 디자인과 검증에서 정한다.

### P-03. 다양한 생활물품과 수납장 사이의 부조화를 핵심 문제로 다룬다 — 확정

캐리어·가방·책·이어폰 등 가구에 보관하거나 가구와 함께 사용하는 생활물품은 크기와 형태가 제각각이다. 이를 받아줘야 하는 수납장과의 관계에서 반복적인 보관 피로가 발생한다는 개인 경험을 연구의 출발점으로 삼는다.

따라서 물건의 다양성, 수납장의 수용 방식, 보관·회수 행동을 함께 설계한다. 수납량 증가나 빈 공간 확보만으로 문제가 해결됐다고 판단하지 않는다.

### P-04. 레일과 엘리베이터를 주요 시스템 연구 대상으로 둔다 — 연구 범위 확정 / 해법 미확정

키네틱 홈에 사용할 주요 시스템으로 레일과 엘리베이터를 연구한다. 다만 두 시스템의 **로직과 컨셉은 아직 확정되지 않았다.** 배치, 이동 대상, 이송·인계 방식, 제어 순서와 사용자 경험에 대한 연구와 발상이 필요하다.

이 문서에서 엘리베이터는 수직 이송 기능을 논의하기 위한 작업 용어다. 사람 탑승 여부를 포함한 용도·규격·구조는 확정하지 않는다. 레일과 엘리베이터를 연구한다는 결정이 특정 기구 형식이나 전자동 운전을 승인한 것은 아니다.

## 3. Elog #001의 관찰과 분석 결과

**근거:** [S1 — Elog #001 — Kinetic House Research](https://app.notion.com/p/3ed3350629a681578462eb4a28e66bea). 아래 내용은 2026-10-05에 확인한 원문의 Question, Observation, Friction Mapping, Concept 전달 요약 및 마무리 결정을 정리한 것이다.

### 3.1 실제 생활 흐름과 반복 행동 — 기록

| ID | 원문에서 확인한 내용 | 근거 성격 |
| --- | --- | --- |
| OBS-01 | 기상 → 루틴 확인 → 아침식사 → 목욕 → 옷 갈아입기 → 외출 준비 | 사용자가 작성한 생활 흐름 |
| OBS-02 | 귀가 → 가방·휴대폰·지갑·액세서리 내려놓기 → 잠옷으로 갈아입기 → 세수·양치 → 개인활동 → 수면 | 사용자가 작성한 생활 흐름 |
| OBS-03 | 가방·옷·필기도구·휴대폰·액세서리를 반복해서 꺼내거나 정리한다. | 반복 행동에 관한 생활 기록 |
| OBS-04 | 가방을 둘 공간을 찾기 위해 애쓴다. | 공간과 행동 사이의 구체적인 마찰 기록 |
| OBS-05 | 외출 전 지갑·이어폰·휴대폰의 위치를 잊어 다시 찾아다닌다. | 물건 회수 과정의 마찰 기록 |
| OBS-06 | 가방·노트북·아이패드, 의자·데스크톱 등이 쓰이지 않을 때에도 공간을 점유한다. | 공간 점유 기록; 각 물건이 실제로 방해하는지는 별도 확인 필요 |
| OBS-07 | 캐리어·가방·책·이어폰 등 크기와 형태가 다른 물건을 수납장에 보관하는 관계에서 반복적으로 피로를 느껴왔다. | 2026-10-05에 명시한 개인의 회고 진술 |

이 기록에는 특정 관찰 일시·장소·조건과 연결된 치수·시간·횟수 측정이 없다. 특히 OBS-07은 반복 경험에 대한 회고이며, 당일 수행한 현장 측정 결과로 해석해서는 안 된다. [S1]

### 3.2 원문에서 도출한 문제 정의와 분석 — 분석 / 문제 선택 확정

- **핵심 마찰:** 형태와 크기가 다양한 생활 도구를 기존 수납장에 맞춰 보관하는 과정에서 느끼는 피로다. 가방 둘 자리 찾기는 이 문제를 드러내는 구체적인 사례다.
- **대표 장면:** 귀가 후 가방·소지품을 내려놓는 순간부터 다음 외출 때 다시 챙기는 과정이다. 문제 범위에는 캐리어와 책처럼 크기·형태가 다른 물건도 포함한다.
- **연구 질문:** 서로 다른 크기·형태의 생활 도구를 보관하고 다시 꺼낼 때, 수납 공간은 무엇을 어떻게 보조해야 거주자의 피로를 줄일 수 있는가?
- **확정한 범위:** 개인의 반복 경험과 기존 생활 기록을 바탕으로 이 문제를 연구의 핵심으로 선택했다. Elog #001은 문제 정의를 확정하는 단계로 마무리됐다.
- **일반화 가설:** 이 문제가 다른 1인가구에서도 중요한 병목일 수 있다. 보편성·심각도·발생 조건은 아직 검증하지 않았다. [S1]

### 3.3 현재 근거로 확정할 수 없는 것

| ID | 아직 확인하지 않은 내용 | 후속 확인 방향 — 제안 |
| --- | --- | --- |
| GAP-01 | 물건별 치수와 실제 수납장 규격 | 물건과 보관 위치를 짝지어 실측한다. |
| GAP-02 | 보관·회수 시간, 발생 빈도, 이동 횟수, 피로의 정도 | 대표 장면의 현재 방식을 기록해 비교 기준을 만든다. |
| GAP-03 | 형태·크기 차이가 물건 찾기 문제를 일으키는 인과관계 | 자리 부족, 가림, 기억, 배치 변경 등 가능한 원인을 구분한다. |
| GAP-04 | 다른 1인가구에도 같은 문제가 나타나는지 | 생활 조건이 다른 사람의 경험을 별도로 확인한다. |
| GAP-05 | 로보틱스·가변 수납·레일·자동화·AI가 피로를 줄이는 효과 | 후보별로 가장 작은 비교 실험을 수행한다. |
| GAP-06 | Ori 사례의 원문 출처·확인 기능·적용 환경 | 원문 자료와 확인 날짜를 기록한 뒤 해석과 분리한다. |

Elog #001의 Ori 관련 작성란은 미완성이다. `Furniture → Interior → Apartment → Architecture`는 해당 연구의 해석 틀이며, Ori의 사업 범위나 성과를 입증한 결론이 아니다. 또한 원문에 보존된 2026-10-03 진행 안내는 수행 전 안내이며 결과가 아니다. [S1]

### 3.4 이 문서의 설계적 해석 — 분석

연구 단위는 **물건 ↔ 수납장 ↔ 거주자의 행동** 사이의 관계로 잡는다. 같은 물건도 사용하는 시점, 되돌려놓는 위치, 접근 자세에 따라 부담이 달라질 수 있기 때문이다. 이는 OBS-03~07을 바탕으로 도출한 설계 관점이며, 효과가 입증된 해결책은 아니다.

## 4. 레일·엘리베이터의 연구와 발상

### 4.1 미확정 사항

| ID | 결정할 질문 | 현재 상태 |
| --- | --- | --- |
| OPEN-01 | 무엇을 움직이는가: 개별 물품, 트레이, 수납 모듈, 가구 전체 중 어느 단위인가? | 미확정 |
| OPEN-02 | 레일은 어디에 배치하고 어떤 방향·경로로 이동하는가? | 미확정 |
| OPEN-03 | 엘리베이터는 무엇을 어느 높이로 옮기며, 레일과 어떻게 인계하는가? | 미확정 |
| OPEN-04 | 어떤 물건 크기·형태·무게를 수용하고, 수용하지 못한 물건은 어떻게 다루는가? | 미확정 |
| OPEN-05 | 사람이 요청하는가, 시스템이 제안하는가, 조건에 따라 자동 실행하는가? | 미확정 |
| OPEN-06 | 이동 순서, 경로 점유, 동시 요청, 중단·재개를 어떻게 처리하는가? | 미확정 |
| OPEN-07 | 장애물, 인계 실패, 위치 불확실성, 전원 상실 시 어떤 상태를 유지·복구하는가? | 미확정 |
| OPEN-08 | 설치·청소·유지관리 부담을 포함해 현재 수납보다 유익한가? | 미검증 |

### 4.2 발상 후보 — 제안, 채택된 컨셉 아님

아래 후보는 비교를 시작하기 위한 예시다. 레일은 수평, 엘리베이터는 수직이라는 조합을 기본 설계로 고정하거나, 후보 하나를 실제 시스템으로 간주하지 않는다.

| 후보 | 탐색할 개념 | 먼저 확인할 불확실성 |
| --- | --- | --- |
| IDEA-01 | 물건을 담은 트레이·모듈을 레일과 수직 이송부 사이에서 전달 | 다양한 물건의 수용, 고정과 인계, 옮긴 뒤 꺼내기 편의 |
| IDEA-02 | 수납장 일부를 접근하기 쉬운 위치·높이로 이동 | 가구 이동이 필요한 이유, 주변 동선, 전체 하중과 공간 부담 |
| IDEA-03 | 수납 위치 조정과 제한된 이송 보조를 결합 | 복잡도를 줄여도 보관·회수 피로가 충분히 줄어드는지 |
| BASE-01 | 현재 수납 방식과 가변 칸막이·배치 개선 등 비구동 대안 | 로봇 시스템이 추가 부담을 감수할 만큼 더 나은지 비교할 기준 |

### 4.3 다음 연구 순서 — 권장

1. 캐리어·가방·책·이어폰 등 서로 다른 물건과 실제 수납 위치를 짝지어 기록한다.
2. 각 조합에서 힘든 동작과 원인을 분리한다. 예: 자리 찾기, 자세 바꾸기, 다른 물건 옮기기, 되돌려놓기.
3. 어떤 행동을 보조할지 정하고, 레일·엘리베이터 후보와 비구동 대안을 같은 장면에서 비교한다.
4. 가장 불확실한 질문 하나를 골라 종이 모형·수동 모형·시뮬레이션 등으로 작게 확인한다.
5. 관찰된 개선과 새로 생긴 부담을 함께 기록한 뒤, 유지·수정·보류할 사항을 정한다.

연구 순서나 모형 제작은 실물 구동 구조의 타당성 검증 완료를 뜻하지 않는다.

## 5. 아키텍처 가이드라인

### ARC-01. 물건·수납·행동을 함께 표현한다 — 필수

물건을 모두 같은 크기의 상자로 가정하거나, 수납장을 용량 수치 하나로만 표현하지 않는다. 실제로 필요한 속성을 조사해 모델에 반영한다. 미측정 값은 미측정 상태로 유지한다.

**조사할 속성의 예 — 제안:** 물건의 외형·방향·무게·변형 가능성·사용 빈도, 수납부의 입구·내부 공간·접근 높이·꺼낼 여유, 함께 보관할 물건과 이동 중 유지할 조건. 수납 적합성은 들어가는지뿐 아니라 꺼내고 되돌려놓을 수 있는지도 포함한다.

### ARC-02. 생활 목적과 구동 방법을 분리한다 — 필수

“외출 준비에 필요한 물건에 접근한다”와 “어느 모터를 어떤 순서로 구동한다”를 별도의 책임으로 다룬다. 레일·엘리베이터 컨셉을 바꾸더라도 생활 시나리오와 평가 기준을 유지할 수 있도록 한다.

| 책임 구분 — 제안 | 다룰 내용 |
| --- | --- |
| 생활 시나리오 | 누가, 언제, 무엇을 위해 도움을 요청하는지 |
| 물건·수납 모델 | 어떤 물건이 어디에 있으며 어떤 조건으로 보관·회수 가능한지 |
| 동작 계획 | 목표 상태로 가기 위한 순서, 경로, 인계 조건 |
| 구동 연동 | 선택된 레일·엘리베이터와 센서·구동기의 연결 |
| 상태·개입 관리 | 현재 진행, 거주자 요청, 중단 조건, 실패와 복구 가능성 |

이 구분은 책임을 검토하기 위한 제안이다. 서비스 수, 프로세스 수, 폴더 구조나 통신 방식을 확정하지 않는다.

### ARC-03. 거주자의 개입을 기본 동작에 포함한다 — 필수

도움의 요청·거절·변경·중단을 정상적인 사용 상황으로 다룬다. 움직이는 중 취소 요청이 들어오면 현재 위치와 하중 등을 고려해 어떻게 안전한 상태로 이행할지 정의해야 한다. 중단을 단순한 즉시 전원 차단으로 가정하지 않는다. 구체적인 정지·유지·복구 방식은 기구 연구에서 검증한다.

### ARC-04. 작동할 수 없는 상황도 설계한다 — 필수

수용 불가능한 물건, 경로 막힘, 위치 미확인, 인계 실패 등에서 시스템이 무엇을 알고 무엇을 할 수 없는지 구분한다. 계속 동작할 조건이 확인되지 않았다면 정상 진행으로 처리하지 않는다. 거주자가 물건에 접근할 대안과 복구 절차는 후속 설계 과제로 남긴다.

## 6. 소스코드 가이드라인

이 장은 향후 작성할 소스코드의 기준이다. 현재 구현된 코드나 결정된 기술 스택을 설명하지 않는다.

| ID | 강도 | 지침 |
| --- | --- | --- |
| CODE-01 | 필수 | 미확정 규격·수치·로직을 확정 사양처럼 숨기지 않는다. 실험에 필요한 가정은 출처, 적용 범위, 변경 가능성을 함께 표시한다. |
| CODE-02 | 필수 | 생활 시나리오와 물건·수납 모델이 특정 구동기나 임시 기구 배치에 직접 종속되지 않도록 책임을 구분한다. |
| CODE-03 | 필수 | 요청된 상태, 관측된 상태, 알 수 없는 상태를 구분한다. 명령 전송만으로 이동·인계 완료를 기록하지 않는다. |
| CODE-04 | 필수 | 조건 검사, 실행, 완료 확인, 실패 처리와 사용자 개입을 명시한다. 상태 이름과 전이 로직 자체는 선택된 컨셉에 맞춰 결정한다. |
| CODE-05 | 필수 | 물건의 크기·위치·수용 가능 여부를 모를 때 임의의 정상값으로 대체하지 않는다. 불확실한 상태의 처리 정책을 드러낸다. |
| CODE-06 | 필수 | 시뮬레이션·모의 데이터·실물 측정 결과를 구분한다. 모형이나 소프트웨어 검증을 실물 성능·안전성 검증으로 보고하지 않는다. |
| CODE-07 | 권장 | 실험 조건과 관찰 결과를 다시 확인할 수 있도록 필요한 상태 변화와 실패 이유를 기록한다. 개인 생활 기록은 평가에 필요한 범위로 제한한다. |
| CODE-08 | 권장 | 변경 설명에 관련 원칙·연구 질문 ID와 검증 범위를 적는다. 예: P-02, OPEN-06, ARC-03. |

**후속 구현의 검증 장면 — 제안:** 수용 불가능한 크기의 물건, 동시에 들어온 요청, 이동 중 개입, 인계 확인 실패, 위치 정보 소실, 중단 후 복구. 정확한 예상 동작과 합격 기준은 해당 컨셉의 결정 기록에서 정의한다.

## 7. 제품·인터랙션 디자인 가이드라인

### DES-01. 도움을 받는 과정 자체의 피로를 줄인다 — 필수

물건마다 복잡한 등록을 요구하거나, 사용할 때마다 별도 용기에 다시 담거나, 수납을 위해 여러 번 조작해야 한다면 그 부담을 개선 효과에서 차감한다. 준비부터 사용 후 되돌려놓기까지 전체 흐름을 평가한다. [P-01, P-03]

### DES-02. 물건의 다양성과 생활의 변화를 수용한다 — 필수

서로 다른 크기와 형태뿐 아니라 새 물건이 들어오거나 임시로 내려놓는 상황도 고려한다. 모든 생활물품을 하나의 표준 용기에 맞추는 방식을 전제로 삼지 않는다. 공통 용기나 모듈을 제안한다면 수용 범위, 예외 물건, 추가 정리 부담을 함께 검토한다. [P-03, ARC-01]

### DES-03. 거주자가 시스템의 행동을 이해하고 개입할 수 있게 한다 — 필수

무엇이 움직이는지, 왜 대기하는지, 도움을 받지 않을 수 있는지, 진행을 어떻게 바꿀 수 있는지를 이해할 수 있어야 한다. 알림의 양과 확인 절차는 일상 피로를 늘리지 않도록 조정한다. 자동 실행을 채택할 경우 허용 범위와 해제·개입 방법을 먼저 정의한다. [P-02, ARC-03]

### DES-04. 공간 점유와 움직임을 생활 장면 안에서 평가한다 — 필수

가구가 차지하는 면적만으로 불편을 판정하지 않는다. 통행, 물건 접근, 휴식·작업과 실제로 충돌하는지 확인한다. 움직임에 따른 대기, 소음, 시각적 부담, 청소와 관리도 평가 항목으로 검토한다. 이러한 부담이 현재 관찰에서 측정됐다고 서술하지 않는다. [OBS-06, OPEN-08]

### DES-05. 외형과 연출은 생활 가치 및 기구 연구와 연결한다 — 권장

형태·색상·소재·노출 구조·조작부 위치는 미확정이다. 디자인 시안에는 사용 장면, 줄이려는 부담, 거주자의 선택권, 기구상 가정을 함께 적는다. 표현 이미지를 제작 가능성이나 사용성 검증의 근거로 대신하지 않는다.

## 8. 검증과 설계 확정 조건

### 8.1 비교 기록 — 제안

| 평가 축 | 기록할 내용 | 현재 상태 |
| --- | --- | --- |
| 신체적 부담 | 옮기는 횟수, 자세 변화, 들기·당기기 등 어려운 동작 | 기준값·목표값 미정 |
| 인지적 부담 | 자리 결정, 위치 찾기, 상태 해석, 별도 조작의 부담 | 기준값·목표값 미정 |
| 시간과 흐름 | 보관·회수 소요 시간, 대기, 생활 흐름의 중단 | 기준값·목표값 미정 |
| 수납 대응성 | 서로 다른 물건을 넣고 꺼내고 되돌려놓을 수 있는 범위 | 대상·치수 미측정 |
| 주체성 | 도움 거절, 진행 변경, 배치 변경, 예외 상황에서의 선택 가능성 | 시나리오·판정 기준 미정 |
| 유지 부담 | 설치, 청소, 재설정, 고장 시 접근과 복구에 드는 수고 | 기준값·목표값 미정 |

후보 간 비교는 가능한 한 같은 물건과 생활 장면을 사용하고, 조건이 달라지면 기록한다. 소요 시간만 줄어도 조작 피로가 커질 수 있으므로 한 수치로 성공을 선언하지 않는다.

### 8.2 상세 설계 확정 전 확인할 항목

- [ ] 대상 생활 장면과 물건–수납장 조합이 구체적으로 기록돼 있다.
- [ ] 줄일 부담과 비교 기준이 명시돼 있다.
- [ ] 레일·엘리베이터의 이동 대상, 경로, 인계와 제어 개념이 비교·선택돼 있다.
- [ ] 거주자의 선택·거절·개입 방식이 설계돼 있다.
- [ ] 크기·형태의 예외와 동작 불가 상황을 다뤘다.
- [ ] 근거와 미검증 사항을 구분하고, 검증 수준을 과장하지 않았다.
- [ ] 채택한 안, 보류한 안, 선택 이유와 결정 주체를 남겼다.

현재 이 체크리스트는 완료되지 않았다. 어떤 제안을 확정으로 바꿀 때에는 사용자의 명시적 결정 또는 해당 작업에 부여된 결정 권한을 근거로 남긴다.

### 8.3 결정 기록 양식 — 권장

각 결정은 다음 항목으로 기록한다. 빈 항목에는 임의 내용을 채우지 않고 `미정` 또는 `미검증`을 적는다.

- 결정 ID / 날짜 / 상태:
- 관련 원칙·관찰·연구 질문 ID:
- 해결할 문제와 사용 장면:
- 비교한 후보와 현재 방식:
- 선택한 안 / 보류한 안 / 이유:
- 실험·관찰 근거와 검증 범위:
- 거주자의 피로와 주체성에 미치는 영향:
- 남은 가정·제약 / 재검토 조건:
- 결정 주체와 확인 근거:

## 9. 사람과 AI를 위한 문서 사용 규칙

### 9.1 AI 작업 지침

1. 작업 전에 P-01~04와 관련 OBS·GAP·OPEN 항목을 확인한다.
2. 근거와 지침이 필요할 때 안정적인 ID를 인용한다. 관찰, 분석, 제안, 확정 사항을 섞지 않는다.
3. 레일·엘리베이터의 미확정 항목을 임의로 최종 사양으로 만들지 않는다. 비교를 위한 가정은 가정이라고 표시한다.
4. 새 아키텍처·코드·디자인 제안에는 해결할 부담, 거주자의 선택권, 검증 방법과 남은 불확실성을 적는다.
5. 외부 사례를 추가할 때 원문 출처·확인 날짜·직접 확인한 사실과 해석을 분리한다. Elog의 미작성 부분을 수행 결과로 채우지 않는다.
6. 충돌이 있으면 충돌한 항목을 드러낸다. 사용자의 후속 명시 지시가 기존 결정을 변경하면 관련 지침과 변경 이력을 함께 갱신한다.
7. 결과를 보고할 때 문서 작성, 시뮬레이션 확인, 실물 검증을 구분한다.
8. **사용자의 별도 명시 지시 없이 Git 커밋이나 푸시를 수행하지 않는다.**

### 9.2 구조와 서체

- **단일 기준:** 사람용·AI용 문서를 우선 분리하지 않는다. 설명과 실행 지침을 같은 문서에 두어 서로 다른 기준이 생기는 것을 줄인다.
- **구조:** 제목은 H1 하나, 주요 장은 H2, 세부 항목은 H3로 구성한다. 짧은 문단과 비교용 표를 사용한다.
- **추적성:** P, OBS, GAP, OPEN, ARC, CODE, DES 등의 ID를 유지한다. 항목이 바뀌면 의미 변화와 근거를 변경 이력에 남긴다.
- **저장 형식:** UTF-8 Markdown을 사용한다. 핵심 지침을 이미지, 색상, 접힌 영역에만 넣지 않는다.
- **GitHub 표시:** 본문과 제목은 GitHub 기본 서체를 사용하고, 코드·식별자에만 고정폭 표기를 사용한다. 일반 Markdown 문서 자체로 GitHub의 글꼴·글자 크기·행간을 강제하지 않는다.
- **로컬 열람 권장값:** 한국어를 지원하는 고딕 계열 본문 서체, 본문 16px 안팎, 행간 1.6 안팎을 뷰어에서 설정할 수 있다. 이는 열람 환경 권장값이며 문서에 적용된 고정 스타일은 아니다.
- **범위:** 이 서체 규칙은 문서 열람을 위한 것이다. 키네틱 홈 제품 UI의 서체나 디자인 시스템을 확정하지 않는다.

## 10. 출처와 변경 이력

### 출처

- **[S1]** [Elog #001 — Kinetic House Research](https://app.notion.com/p/3ed3350629a681578462eb4a28e66bea) — Notion, 확인일 2026-10-05. 원문 최종 수정 시각: 2026-10-05 12:45:13 KST. Question, Observation, Friction Mapping, Concept 전달 요약, 마무리 결정을 근거로 사용했다. 원문의 측정·사례 조사 빈칸은 미수행 상태로 반영했다.
- **[S2]** 사용자 직접 요구사항 — 2026-10-05, 이 문서 작성 요청. 레일·엘리베이터의 로직·컨셉 연구 필요, 다양한 생활물품과 수납장 문제, 불편·피로 해소와 주체성 유지, 사람·AI가 함께 읽는 Markdown, 임의 커밋·푸시 금지를 명시했다.

S1은 연구 기록의 출처이고 S2는 현재 작업의 요구사항이다. S1에서 해법을 확정하지 않은 상태와 S2에서 레일·엘리베이터를 주요 연구 대상으로 지정한 상태를 함께 반영했다. 이 문서가 추가한 후보·구조·검증 방법은 별도 출처가 있는 실증 결과가 아니라 설계를 진행하기 위한 제안이다.

### 변경 이력

| 버전 | 날짜 | 변경 내용 |
| --- | --- | --- |
| 0.1 | 2026-10-05 | Elog #001의 기록과 한계를 정리하고, 사용자 목적·연구 범위 및 아키텍처·코드·디자인 지침을 작성했다. 상세 설계는 미확정으로 유지했다. |
