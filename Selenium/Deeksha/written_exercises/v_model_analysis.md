
# Hands-On 2

## SDLC vs TDLC – V-Model & Agile QA Integration

**Name:** Deeksha S

**Module:** QA Concepts & Selenium Basics

---

# Task 1

## 9. V-Model Mapping

The V-Model establishes a relationship between each Software Development Life Cycle (SDLC) phase and its corresponding Testing Development Life Cycle (TDLC) phase.

```text
                 SDLC                           TDLC

        Requirements -----------------> Acceptance Testing

        System Design -----------------> System Testing

        Architecture Design -----------> Integration Testing

        Module Design -----------------> Unit Testing

                     \               /
                      \             /
                        Coding
```

### SDLC ↔ TDLC Mapping

| SDLC Phase | Corresponding TDLC Phase | Test Artifact Produced |
|------------|--------------------------|------------------------|
| Requirements | Acceptance Testing | Acceptance Test Plan |
| System Design | System Testing | System Test Plan |
| Architecture Design | Integration Testing | Integration Test Plan |
| Module Design | Unit Testing | Unit Test Cases |
| Coding | Execution of Tests | Source Code |

---

## 10. Test Artifacts Produced

### Requirements Phase

- Acceptance Test Plan
- Requirement Review Checklist

### System Design Phase

- System Test Plan
- Test Scenarios

### Architecture Design Phase

- Integration Test Plan
- Interface Test Cases

### Module Design Phase

- Unit Test Cases
- Module Test Plan

### Coding Phase

- Source Code
- Executable Build

---

## 11. Entry and Exit Criteria

| Testing Level | Entry Criteria | Exit Criteria |
|---------------|---------------|---------------|
| Unit Testing | Module coding completed | All unit tests passed, no critical defects |
| Integration Testing | Unit testing completed successfully | Interfaces tested successfully, no major defects |
| System Testing | Integrated application available | All planned test cases executed, critical defects resolved |
| Acceptance Testing | System testing completed | Customer acceptance obtained and application approved |

---

## 12. QA Engagement in the V-Model

### 1. Requirements Review

QA reviews the requirements to ensure they are clear, complete, consistent, and testable before development begins.

### 2. Design Review

QA participates in reviewing the system design and architecture to identify potential risks and prepare test scenarios before coding starts.

---

# Task 2

## 13. Problems in Waterfall Testing

In the Waterfall model, testing starts only after development is completed. This creates several problems:

### Problem 1

Defects are discovered very late, making them more expensive and time-consuming to fix.

### Problem 2

Requirement misunderstandings remain unnoticed until testing begins, leading to rework.

### Problem 3

Testing time is limited because development delays reduce the available testing schedule.

---

## 14. QA Role in Agile Ceremonies

### Sprint Planning

- Understand user stories.
- Define acceptance criteria.
- Estimate testing effort.
- Identify testing requirements.

### Daily Stand-up

- Share testing progress.
- Report blockers.
- Discuss defects.
- Coordinate with developers.

### Sprint Review

- Verify completed features.
- Demonstrate tested functionality.
- Validate acceptance criteria.

### Sprint Retrospective

- Discuss testing challenges.
- Suggest process improvements.
- Improve collaboration within the team.

---

## 15. Shift-Left Testing Practices

### a) Requirement Review

QA reviews requirements early to ensure they are complete, clear, and testable before development begins.

### b) Writing Test Cases Before Coding (TDD/BDD)

QA prepares test cases and acceptance criteria before developers start coding, reducing misunderstandings.

### c) Static Code Analysis

Developers use static analysis tools to identify coding issues before executing the application.

### d) API Contract Testing

QA validates API specifications and endpoint contracts before integrating different modules.

---

## 16. Acceptance Criteria (Given–When–Then)

### Scenario 1 – Happy Path

**Given** the college administrator is logged into the Course Management System

**When** valid course details are entered and the Create button is clicked

**Then** the course should be created successfully and a confirmation message should be displayed.

---

### Scenario 2 – Duplicate Course Code

**Given** a course with the same course code already exists

**When** the administrator attempts to create another course using the same course code

**Then** the system should display an error message indicating that the course code already exists.

---

### Scenario 3 – Missing Required Fields

**Given** the administrator is on the Create Course page

**When** one or more mandatory fields are left empty and the Create button is clicked

**Then** the system should display validation messages and prevent the course from being created.

---

# Conclusion

This hands-on provided an understanding of the relationship between SDLC and TDLC through the V-Model. It also explained entry and exit criteria, QA involvement throughout the software development lifecycle, Agile QA practices, Shift-Left testing, and writing acceptance criteria using the Given-When-Then format. These concepts help ensure better software quality and support effective test planning from the early stages of development.