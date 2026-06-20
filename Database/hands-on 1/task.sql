-- Create Database
CREATE DATABASE college_db;

-- Use Database
USE college_db;

---------------------------------------------------
-- 1. Departments Table
---------------------------------------------------

CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL,
    hod_name VARCHAR(100),
    budget DECIMAL(12,2)
);

---------------------------------------------------
-- 2. Students Table
---------------------------------------------------

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    date_of_birth DATE,
    department_id INT,
    enrollment_year INT,

    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);

---------------------------------------------------
-- 3. Courses Table
---------------------------------------------------

CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(150) NOT NULL,
    course_code VARCHAR(20) UNIQUE,
    credits INT,
    department_id INT,

    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);

---------------------------------------------------
-- 4. Enrollments Table
---------------------------------------------------

CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    grade CHAR(2),

    FOREIGN KEY (student_id)
    REFERENCES students(student_id),

    FOREIGN KEY (course_id)
    REFERENCES courses(course_id)
);

---------------------------------------------------
-- 5. Professors Table
---------------------------------------------------

CREATE TABLE professors (
    professor_id INT AUTO_INCREMENT PRIMARY KEY,
    prof_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department_id INT,
    salary DECIMAL(10,2),

    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);
---------------------------------------------------
-- TASK 2 : VERIFY NORMALISATION
---------------------------------------------------

-- 1NF (First Normal Form)
-- All columns contain atomic values.
-- No column stores multiple values.
-- Example violation:
-- phone_numbers = '9876543210,9876543211'
-- This would violate 1NF.

-- 2NF (Second Normal Form)
-- All non-key attributes depend fully on primary keys.
-- In enrollments table, grade and enrollment_date
-- depend on the student-course relationship.
-- No partial dependency exists.

-- 3NF (Third Normal Form)
-- No transitive dependency exists.
-- Example:
-- student_id -> department_id -> dept_name
-- Therefore dept_name is stored in departments table
-- and not inside students.

-- 3NF Analysis for enrollments table
-- enrollment_id uniquely identifies enrollment.
-- grade depends only on enrollment.
-- student and course details are stored separately.
-- Therefore enrollments satisfies 3NF.


---------------------------------------------------
-- TASK 3 : ALTER AND EXTEND THE SCHEMA
---------------------------------------------------

USE college_db;

---------------------------------------------------
-- Step 10
-- Add phone_number to students
---------------------------------------------------

ALTER TABLE students
ADD phone_number VARCHAR(15);

---------------------------------------------------
-- Step 11
-- Add max_seats to courses
---------------------------------------------------

ALTER TABLE courses
ADD max_seats INT DEFAULT 60;

---------------------------------------------------
-- Step 12
-- Add CHECK constraint for grade
---------------------------------------------------

ALTER TABLE enrollments
ADD CONSTRAINT chk_grade
CHECK (
grade IN ('A','B','C','D','F')
OR grade IS NULL
);

---------------------------------------------------
-- Step 13
-- Rename hod_name → head_of_dept
---------------------------------------------------

ALTER TABLE departments
RENAME COLUMN hod_name TO head_of_dept;

---------------------------------------------------
-- Step 14
-- Remove phone_number (schema rollback)
---------------------------------------------------

ALTER TABLE students
DROP COLUMN phone_number;

---------------------------------------------------
-- Verification
---------------------------------------------------

DESC departments;

DESC courses;

DESC students;

DESC enrollments;