# Hands-On 1

## QA Concepts, Functional Testing & Defect Lifecycle

**Name:** Deeksha S

**Module:** QA Concepts & Selenium Basics

---

# Task 1

## 1. Testing Types for the Course Management API

### Unit Testing

**Test Case:**

Verify that the function `validate_course_name()` correctly validates the course name.

**Example:**

- Input: "Python"
- Expected Output: Valid

**Testing Type:** Functional Testing

---

### Integration Testing

**Test Case:**

Verify that the POST `/api/courses` endpoint successfully stores the course details in the database.

**Components Tested:**

- API Endpoint
- Database

**Testing Type:** Functional Testing

---

### System Testing

**Test Case:**

Create a new course using the API and retrieve it using the GET endpoint to verify the complete end-to-end workflow.

**Testing Type:** Functional Testing

---

### User Acceptance Testing (UAT)

**Test Case:**

A college administrator logs into the application, creates a new course, edits the course information, and verifies that the updated course is displayed correctly.

**Testing Type:** Functional Testing

---

## 2. Functional and Non-Functional Testing

The above four test cases are examples of **Functional Testing** because they verify whether the application performs the required functionality correctly.

### Example of Non-Functional Testing

**Performance Testing**

Verify that the Course Management API responds within **2 seconds** when **500 users** send requests simultaneously.

---

## 3. Black-Box Testing vs White-Box Testing

### Black-Box Testing

Black-box testing verifies the functionality of an application without knowing its internal source code.

**Example:**

Testing the POST `/api/courses` endpoint by sending requests and verifying the response.

### White-Box Testing

White-box testing verifies the internal code, logic, conditions, loops, and program structure.

**Example:**

Testing the internal validation function `validate_course_name()`.

### Who Performs Them?

- **QA Testers** generally perform **Black-Box Testing**.
- **Developers** generally perform **White-Box Testing**.

---

## 4. Formal Test Cases

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
|--------------|-------------|---------------|------------|-----------------|---------------|-----------|
| TC001 | Create a new course | API server is running | Send a POST request with valid course details | Course is created successfully with HTTP Status Code **201 (Created)** | | |
| TC002 | Create a course with an empty name | API server is running | Send a POST request with an empty course name | API returns **400 Bad Request** with a validation error | | |
| TC003 | Create a duplicate course | Course already exists | Send a POST request with the same course name | API returns a duplicate course error message | | |

---

# Task 2

## 5. Defect Lifecycle

The defect lifecycle describes the different stages a defect goes through from identification to closure.

```
New
  ↓
Assigned
  ↓
Open
  ↓
Fixed
  ↓
Retest
  ↓
Verified
  ↓
Closed
```

### Explanation of Each Stage

- **New:** The defect is identified and reported by the QA tester.
- **Assigned:** The defect is assigned to a developer for analysis and fixing.
- **Open:** The developer starts working on resolving the defect.
- **Fixed:** The developer fixes the defect and marks it as fixed.
- **Retest:** The QA tester retests the application to verify the fix.
- **Verified:** The tester confirms that the defect has been fixed successfully.
- **Closed:** The defect is closed after successful verification.

### Alternate Paths

**Rejected:**

- The developer rejects the defect because it is invalid, cannot be reproduced, or is not considered a bug.

**Deferred:**

- The defect is accepted but postponed to a future release because it is not critical or due to project constraints.

---

## 6. Severity and Priority Classification

| Bug | Severity | Priority | Justification |
|------|----------|----------|---------------|
| **a)** POST `/api/courses` returns **500 Internal Server Error** for all requests | Critical | P1 | The API is completely unusable because users cannot create courses. It must be fixed immediately. |
| **b)** Course names longer than 150 characters are silently truncated without an error | Medium | P2 | The application continues to work, but data is lost, affecting data integrity. |
| **c)** The `/docs` Swagger page has a typo in the API description | Low | P4 | This is a documentation issue and does not affect the application's functionality. |
| **d)** Login with correct credentials occasionally returns **401 Unauthorized** on the first attempt | High | P1 | Users cannot reliably log in. Since the issue is intermittent, it may indicate a deeper system problem and should be fixed urgently. |

---

## 7. Defect Report

**Defect ID:** BUG-001

**Title:** POST `/api/courses` returns 500 Internal Server Error

**Environment:**

- Windows 11
- Python 3.x
- VS Code
- Google Chrome

**Build Version:** v1.0

**Severity:** Critical

**Priority:** P1

### Steps to Reproduce

1. Start the Course Management API.
2. Open Postman or Swagger UI.
3. Send a POST request to `/api/courses` with valid course details.
4. Observe the response.

### Expected Result

The API should create a new course successfully and return **HTTP Status Code 201 (Created).**

### Actual Result

The API returns **HTTP Status Code 500 (Internal Server Error)**, and the course is not created.

### Attachments

- Screenshot of the 500 Internal Server Error.

---

## 8. Difference Between Severity and Priority

### Severity

Severity indicates how seriously a defect affects the application's functionality.

### Priority

Priority indicates how urgently a defect should be fixed.

### Example

A spelling mistake on the CEO's dashboard has **Low Severity** because it does not affect the application's functionality. However, it has **High Priority** because it is highly visible and should be corrected before the software is released.

Another example is a rarely used feature that crashes the application. It has **High Severity** because it affects functionality but may have **Low Priority** if very few users use that feature.

---

# Conclusion

This hands-on helped in understanding the fundamentals of Quality Assurance, including testing levels, functional and non-functional testing, black-box and white-box testing, defect lifecycle, severity and priority classification, defect reporting, and formal test case writing. These concepts provide a strong foundation for learning Selenium test automation in the upcoming hands-on exercises.