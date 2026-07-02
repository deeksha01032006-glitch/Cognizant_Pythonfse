# Hands-On 3

## Test Automation Process, Lifecycle & Framework Types

**Name:** Deeksha S

**Module:** QA Concepts & Selenium Basics

---

# Task 1

## 17. Criteria for Deciding Whether a Test Case Should Be Automated

The following are five important criteria for selecting test cases for automation. The example used is:

**Scenario:** Test that the POST `/api/courses/` endpoint returns HTTP 201 and correct course data when valid input is provided.

### 1. Repetitive Execution

Tests executed frequently should be automated because they save time.

**Application:**
The POST API is executed during every regression cycle, making it a good automation candidate.

---

### 2. Stable Functionality

Features that rarely change are suitable for automation.

**Application:**
The POST endpoint is a core API and is unlikely to change frequently.

---

### 3. High Business Priority

Critical business features should always be automated.

**Application:**
Creating a course is one of the main functionalities of the Course Management API.

---

### 4. Data-Driven Testing

Tests requiring multiple input combinations are ideal for automation.

**Application:**
Different course names, IDs, durations, and instructors can be tested automatically.

---

### 5. Time Saving

Automation reduces manual effort for repetitive tests.

**Application:**
Instead of manually testing the POST endpoint after every release, automated execution completes within seconds.

---

## 18. Test Case Selection

| Test Case | Decision | Justification |
|------------|----------|---------------|
| Regression testing of all CRUD endpoints | Automate | Frequently executed after every code change. |
| Exploratory testing of new search feature | Manual | Requires human observation and creativity. |
| Performance testing with 100 concurrent users | Automate | Performance tools can simulate multiple users efficiently. |
| UI Login Test | Automate | Login is executed in almost every testing cycle. |
| Verify Swagger Documentation | Manual | Documentation changes occasionally and requires human verification. |
| Smoke Test after deployment | Automate | Quick validation after every deployment saves time. |

---

## 19. Test Automation ROI

### Definition

Return on Investment (ROI) measures whether the time and effort spent creating automated tests are recovered through repeated execution.

### Given

- Automation Development = 4 hours
- Manual Execution = 30 minutes (0.5 hour)

### ROI Calculation

Automation Cost

```
4 hours
```

Manual Execution Cost

```
0.5 hour per execution
```

Break-even Point

```
4 ÷ 0.5 = 8 executions
```

Therefore, automation becomes beneficial after **8 executions**.

### Maintenance Cost

After the 10th execution:

```
20% of 0.5 hour = 0.1 hour
```

Total execution time after 10 runs

```
0.5 + 0.1 = 0.6 hour
```

Even after maintenance, automation remains cost-effective because it saves significant manual effort.

---

## 20. Flaky Test

### Definition

A flaky test is a test that sometimes passes and sometimes fails without any changes in the application.

### Example

A Selenium test clicks the Login button before the page finishes loading.

Sometimes the test passes, sometimes it fails.

### Strategies to Prevent Flaky Tests

1. Use Explicit Waits instead of Thread.sleep().
2. Use stable element locators such as ID or Name.
3. Maintain test independence so tests do not rely on previous executions.

---

# Task 2

## 21. Automation Framework Types

### Linear Framework

**Description**

Tests are written in a single script and executed sequentially.

**Advantage**

Simple to understand and develop.

**Disadvantage**

Poor code reuse and difficult maintenance.

**Course Management Example**

Testing only the login feature in a small project.

---

### Modular Framework

**Description**

The application is divided into reusable modules.

**Advantage**

Reusable code and easier maintenance.

**Disadvantage**

Requires planning during framework design.

**Course Management Example**

Separate modules for Login, Courses, Students, and Faculty.

---

### Data-Driven Framework

**Description**

Test data is stored externally in Excel, CSV, or JSON files.

**Advantage**

Same test script works with multiple data sets.

**Disadvantage**

Managing external data files increases complexity.

**Course Management Example**

Testing login using 50 different usernames and passwords.

---

### Keyword-Driven Framework

**Description**

Tests are created using keywords representing actions.

**Advantage**

Non-technical testers can create test cases.

**Disadvantage**

Framework implementation is more complex.

**Course Management Example**

Keywords such as Login, ClickButton, CreateCourse.

---

### Hybrid Framework

**Description**

Combines Modular, Data-Driven, and Keyword-Driven approaches.

**Advantage**

Highly reusable, flexible, and scalable.

**Disadvantage**

Initial development takes more time.

**Course Management Example**

Large Selenium automation project covering all Course Management features.

---

## 22. Recommended Framework

### Recommendation

A **Hybrid Framework** combining:

- Modular Framework
- Data-Driven Framework
- Keyword-Driven Framework

### Justification

- Supports 50 different login credentials using external test data.
- Login functionality can be reused across multiple test cases.
- Non-technical team members can write keyword-based test scenarios.
- Easier maintenance for large automation projects.

---

## 23. Hybrid Framework Folder Structure

```text
CourseManagementAutomation/
│
├── config/
│      config.py
│
├── test_data/
│      login_data.xlsx
│      course_data.csv
│
├── page_objects/
│      login_page.py
│      course_page.py
│      dashboard_page.py
│
├── utilities/
│      driver_factory.py
│      logger.py
│      helpers.py
│
├── test_cases/
│      test_login.py
│      test_courses.py
│      test_dashboard.py
│
├── reports/
│
├── screenshots/
│
├── requirements.txt
│
└── README.md
```

### Explanation

- **config** stores project configuration.
- **test_data** stores Excel and CSV files.
- **page_objects** contains Selenium Page Object classes.
- **utilities** contains reusable helper methods.
- **test_cases** contains Selenium test scripts.
- **reports** stores test execution reports.
- **screenshots** stores failed test screenshots.

---

# Conclusion

This hands-on explained how to decide which test cases should be automated, how automation provides return on investment (ROI), and how flaky tests can be prevented. It also compared five automation framework types—Linear, Modular, Data-Driven, Keyword-Driven, and Hybrid—and recommended a Hybrid Framework for the Course Management System because it offers reusability, scalability, and maintainability for real-world Selenium automation projects.