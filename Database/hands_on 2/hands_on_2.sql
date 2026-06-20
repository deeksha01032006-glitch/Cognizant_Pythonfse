---------------------------------------------------
-- HANDS ON 2 : TASK 1
-- INSERT / UPDATE / DELETE
---------------------------------------------------

USE college_db;

---------------------------------------------------
-- Departments
---------------------------------------------------

INSERT INTO departments (dept_name, head_of_dept, budget)
VALUES
('Computer Science','Dr. Ramesh Kumar',850000.00),
('Electronics','Dr. Priya Nair',620000.00),
('Mechanical','Dr. Suresh Iyer',540000.00),
('Civil','Dr. Ananya Sharma',430000.00);

SELECT COUNT(*) FROM departments;

---------------------------------------------------
-- Students
---------------------------------------------------

INSERT INTO students
(first_name,last_name,email,date_of_birth,department_id,enrollment_year)
VALUES
('Arjun','Mehta','arjun.mehta@college.edu','2003-04-12',1,2022),
('Priya','Suresh','priya.suresh@college.edu','2003-07-25',1,2022),
('Rohan','Verma','rohan.verma@college.edu','2002-11-08',2,2021),
('Sneha','Patel','sneha.patel@college.edu','2004-01-30',3,2023),
('Vikram','Das','vikram.das@college.edu','2003-09-14',1,2022),
('Kavya','Menon','kavya.menon@college.edu','2002-05-17',2,2021),
('Aditya','Singh','aditya.singh@college.edu','2004-03-22',4,2023),
('Deepika','Rao','deepika.rao@college.edu','2003-08-09',1,2022);

SELECT COUNT(*) FROM students;

---------------------------------------------------
-- Add 2 Extra Students
---------------------------------------------------

INSERT INTO students
(first_name,last_name,email,date_of_birth,department_id,enrollment_year)
VALUES
('Deeksha','S','deeksha.s@college.edu','2006-03-01',1,2025),

('Nithya','K','nithya.k@college.edu','2005-08-15',2,2025);

SELECT COUNT(*) FROM students;

---------------------------------------------------
-- Courses
---------------------------------------------------

INSERT INTO courses
(course_name,course_code,credits,department_id)
VALUES
('Data Structures & Algorithms','CS101',4,1),
('Database Management Systems','CS102',3,1),
('Object Oriented Programming','CS103',4,1),
('Circuit Theory','EC101',3,2),
('Thermodynamics','ME101',3,3);

SELECT COUNT(*) FROM courses;

---------------------------------------------------
-- Enrollments
---------------------------------------------------

INSERT INTO enrollments
(student_id,course_id,enrollment_date,grade)
VALUES
(1,1,'2022-07-01','A'),
(1,2,'2022-07-01','B'),
(2,1,'2022-07-01','B'),
(2,3,'2022-07-01','A'),
(3,4,'2021-07-01','A'),
(4,5,'2023-07-01',NULL),
(5,1,'2022-07-01','C'),
(5,2,'2022-07-01','A'),
(6,4,'2021-07-01','B'),
(7,5,'2023-07-01',NULL),
(8,1,'2022-07-01','A'),
(8,3,'2022-07-01','B');

SELECT COUNT(*) FROM enrollments;

---------------------------------------------------
-- Professors
---------------------------------------------------

INSERT INTO professors
(prof_name,email,department_id,salary)
VALUES
('Dr. Anand Krishnan','anand.k@college.edu',1,95000),
('Dr. Meena Pillai','meena.p@college.edu',1,88000),
('Dr. Sunil Rajan','sunil.r@college.edu',2,82000),
('Dr. Latha Gopal','latha.g@college.edu',3,79000),
('Dr. Kartik Bose','kartik.b@college.edu',4,76000);

SELECT COUNT(*) FROM professors;

---------------------------------------------------
-- Update Grade
---------------------------------------------------

UPDATE enrollments
SET grade='B'
WHERE student_id=5
AND course_id=1;

---------------------------------------------------
-- Preview NULL grades
---------------------------------------------------

SELECT *
FROM enrollments
WHERE grade IS NULL;

---------------------------------------------------
-- Delete NULL grades
---------------------------------------------------

DELETE FROM enrollments
WHERE grade IS NULL;

---------------------------------------------------
-- Final Verification
---------------------------------------------------

SELECT COUNT(*) AS total_students
FROM students;

SELECT COUNT(*) AS total_enrollments
FROM enrollments;
---------------------------------------------------
-- HANDS ON 2 : TASK 2
-- SINGLE TABLE QUERIES AND FILTERING
---------------------------------------------------

USE college_db;

---------------------------------------------------
-- 20. Students enrolled in 2022
---------------------------------------------------

SELECT *
FROM students
WHERE enrollment_year = 2022
ORDER BY last_name ASC;

---------------------------------------------------
-- 21. Courses with credits > 3
---------------------------------------------------

SELECT *
FROM courses
WHERE credits > 3
ORDER BY credits DESC;

---------------------------------------------------
-- 22. Professors salary between 80000 and 95000
---------------------------------------------------

SELECT *
FROM professors
WHERE salary BETWEEN 80000 AND 95000;

---------------------------------------------------
-- 23. Students whose email ends with @college.edu
---------------------------------------------------

SELECT *
FROM students
WHERE email LIKE '%@college.edu';

---------------------------------------------------
-- 24. Count students per enrollment year
---------------------------------------------------

SELECT
enrollment_year,
COUNT(*) AS total_students
FROM students
GROUP BY enrollment_year
ORDER BY enrollment_year;
---------------------------------------------------
-- HANDS ON 2 : TASK 3
-- MULTI TABLE QUERIES (JOINS)
---------------------------------------------------

USE college_db;

---------------------------------------------------
-- 25. Show students with department names
---------------------------------------------------

SELECT
s.student_id,
s.first_name,
s.last_name,
d.dept_name
FROM students s
JOIN departments d
ON s.department_id = d.department_id;

---------------------------------------------------
-- 26. Show courses with department names
---------------------------------------------------

SELECT
c.course_id,
c.course_name,
d.dept_name
FROM courses c
JOIN departments d
ON c.department_id = d.department_id;

---------------------------------------------------
-- 27. Show enrollments with student names
---------------------------------------------------

SELECT
e.enrollment_id,
s.first_name,
s.last_name,
e.course_id,
e.grade
FROM enrollments e
JOIN students s
ON e.student_id = s.student_id;

---------------------------------------------------
-- 28. Show student and course details
---------------------------------------------------

SELECT
s.first_name,
s.last_name,
c.course_name,
e.grade
FROM enrollments e
JOIN students s
ON e.student_id = s.student_id
JOIN courses c
ON e.course_id = c.course_id;

---------------------------------------------------
-- 29. Count students in each department
---------------------------------------------------

SELECT
d.dept_name,
COUNT(s.student_id) AS total_students
FROM departments d
LEFT JOIN students s
ON d.department_id = s.department_id
GROUP BY d.dept_name;

---------------------------------------------------
-- 30. Show professors with department names
---------------------------------------------------

SELECT
p.prof_name,
d.dept_name,
p.salary
FROM professors p
JOIN departments d
ON p.department_id = d.department_id;
---------------------------------------------------
-- HANDS ON 2 : TASK 4
-- AGGREGATE FUNCTIONS AND GROUPING
---------------------------------------------------

USE college_db;

---------------------------------------------------
-- 31. Total number of students
---------------------------------------------------

SELECT COUNT(*) AS total_students
FROM students;

---------------------------------------------------
-- 32. Average professor salary
---------------------------------------------------

SELECT AVG(salary) AS average_salary
FROM professors;

---------------------------------------------------
-- 33. Highest and lowest professor salary
---------------------------------------------------

SELECT
MAX(salary) AS highest_salary,
MIN(salary) AS lowest_salary
FROM professors;

---------------------------------------------------
-- 34. Count courses in each department
---------------------------------------------------

SELECT
department_id,
COUNT(*) AS total_courses
FROM courses
GROUP BY department_id;

---------------------------------------------------
-- 35. Count students department wise
---------------------------------------------------

SELECT
department_id,
COUNT(*) AS total_students
FROM students
GROUP BY department_id;

---------------------------------------------------
-- 36. Average course credits
---------------------------------------------------

SELECT AVG(credits) AS average_credits
FROM courses;

---------------------------------------------------
-- 37. Total budget of departments
---------------------------------------------------

SELECT SUM(budget) AS total_budget
FROM departments;

---------------------------------------------------
-- 38. Departments having more than 1 student
---------------------------------------------------

SELECT
department_id,
COUNT(*) AS student_count
FROM students
GROUP BY department_id
HAVING COUNT(*) > 1;