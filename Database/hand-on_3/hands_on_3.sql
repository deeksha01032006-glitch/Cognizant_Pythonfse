---------------------------------------------------
-- HANDS ON 3 : TASK 1
-- SUBQUERIES
---------------------------------------------------

USE college_db;

---------------------------------------------------
-- 35. Students enrolled in more courses
-- than average enrollments per student
---------------------------------------------------

SELECT
s.student_id,
s.first_name,
s.last_name,
COUNT(e.course_id) AS total_courses
FROM students s
JOIN enrollments e
ON s.student_id=e.student_id
GROUP BY
s.student_id,
s.first_name,
s.last_name
HAVING COUNT(e.course_id) >
(
SELECT AVG(course_count)
FROM
(
SELECT COUNT(*) AS course_count
FROM enrollments
GROUP BY student_id
) avg_table
);

---------------------------------------------------
-- 36. Courses where all enrolled students
-- received grade A
---------------------------------------------------

SELECT
c.course_id,
c.course_name
FROM courses c
WHERE NOT EXISTS
(
SELECT *
FROM enrollments e
WHERE e.course_id=c.course_id
AND e.grade<>'A'
);

---------------------------------------------------
-- 37. Highest salary professor
-- in each department
---------------------------------------------------

SELECT
p.prof_name,
p.salary,
p.department_id
FROM professors p
WHERE p.salary=
(
SELECT MAX(p2.salary)
FROM professors p2
WHERE p2.department_id=
p.department_id
);

---------------------------------------------------
-- 38. Derived table:
-- departments average salary > 85000
---------------------------------------------------

SELECT *
FROM
(
SELECT
department_id,
AVG(salary) AS avg_salary
FROM professors
GROUP BY department_id
) dept_avg
WHERE avg_salary>85000;
---------------------------------------------------
-- HANDS ON 3 : TASK 2
-- CREATING AND USING VIEWS
---------------------------------------------------

USE college_db;

---------------------------------------------------
-- 39. Student Enrollment Summary View
---------------------------------------------------

CREATE VIEW vw_student_enrollment_summary AS
SELECT
s.student_id,
CONCAT(s.first_name,' ',s.last_name) AS full_name,
d.dept_name,
COUNT(e.course_id) AS total_courses,

ROUND(
AVG(
CASE
WHEN e.grade='A' THEN 4
WHEN e.grade='B' THEN 3
WHEN e.grade='C' THEN 2
WHEN e.grade='D' THEN 1
WHEN e.grade='F' THEN 0
END
),2
) AS GPA

FROM students s
LEFT JOIN departments d
ON s.department_id=d.department_id

LEFT JOIN enrollments e
ON s.student_id=e.student_id

GROUP BY
s.student_id,
full_name,
d.dept_name;

---------------------------------------------------
-- 40. Course Statistics View
---------------------------------------------------

CREATE VIEW vw_course_stats AS
SELECT

c.course_name,
c.course_code,

COUNT(e.student_id)
AS total_enrollments,

ROUND(
AVG(
CASE
WHEN e.grade='A' THEN 4
WHEN e.grade='B' THEN 3
WHEN e.grade='C' THEN 2
WHEN e.grade='D' THEN 1
WHEN e.grade='F' THEN 0
END
),2
) AS avg_gpa

FROM courses c

LEFT JOIN enrollments e
ON c.course_id=e.course_id

GROUP BY
c.course_name,
c.course_code;

---------------------------------------------------
-- Verify View
---------------------------------------------------

SELECT *
FROM vw_course_stats;

---------------------------------------------------
-- 41. Students GPA > 3
---------------------------------------------------

SELECT *
FROM vw_student_enrollment_summary
WHERE GPA>3.0;

---------------------------------------------------
-- 42. Try UPDATE
---------------------------------------------------

UPDATE vw_student_enrollment_summary
SET total_courses=5
WHERE student_id=1;

---------------------------------------------------
-- Notes:
-- Multi-table views generally are not updatable
-- because values come from multiple tables and
-- SQL cannot determine where updates belong.
---------------------------------------------------

---------------------------------------------------
-- 43. Drop Views
---------------------------------------------------

DROP VIEW vw_course_stats;

DROP VIEW vw_student_enrollment_summary;

---------------------------------------------------
-- Recreate WITH CHECK OPTION
---------------------------------------------------

CREATE VIEW vw_student_enrollment_summary AS

SELECT
student_id,
first_name,
last_name,
department_id

FROM students

WHERE department_id IS NOT NULL

WITH CHECK OPTION;

---------------------------------------------------
-- Final Verify
---------------------------------------------------

SELECT *
FROM vw_student_enrollment_summary;
---------------------------------------------------
-- HANDS ON 3 : TASK 3
-- STORED PROCEDURES & TRANSACTIONS
---------------------------------------------------

USE college_db;

---------------------------------------------------
-- 44. Procedure: Enroll Student
---------------------------------------------------

DELIMITER $$

CREATE PROCEDURE sp_enroll_student(
IN p_student_id INT,
IN p_course_id INT,
IN p_enrollment_date DATE
)

BEGIN

IF EXISTS
(
SELECT *
FROM enrollments
WHERE student_id=p_student_id
AND course_id=p_course_id
)

THEN

SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT='Duplicate enrollment not allowed';

ELSE

INSERT INTO enrollments
(student_id,course_id,enrollment_date)

VALUES
(
p_student_id,
p_course_id,
p_enrollment_date
);

END IF;

END$$

DELIMITER ;

---------------------------------------------------
-- Test Procedure
---------------------------------------------------

CALL sp_enroll_student(
1,
3,
'2026-06-22'
);

---------------------------------------------------
-- 45. Transfer Student Transaction
---------------------------------------------------

CREATE TABLE IF NOT EXISTS
department_transfer_log
(
log_id INT AUTO_INCREMENT PRIMARY KEY,

student_id INT,

old_department INT,

new_department INT,

transfer_date TIMESTAMP
DEFAULT CURRENT_TIMESTAMP
);

DELIMITER $$

CREATE PROCEDURE sp_transfer_student(

IN p_student_id INT,

IN p_new_department INT

)

BEGIN

DECLARE old_dept INT;

START TRANSACTION;

SELECT department_id
INTO old_dept
FROM students
WHERE student_id=p_student_id;

UPDATE students

SET department_id=
p_new_department

WHERE student_id=
p_student_id;

INSERT INTO
department_transfer_log
(
student_id,
old_department,
new_department
)

VALUES
(
p_student_id,
old_dept,
p_new_department
);

COMMIT;

END$$

DELIMITER ;

---------------------------------------------------
-- Test Transfer
---------------------------------------------------

CALL sp_transfer_student(
1,
2
);

---------------------------------------------------
-- Verify Log
---------------------------------------------------

SELECT *
FROM department_transfer_log;

---------------------------------------------------
-- 46. Rollback Test
---------------------------------------------------

START TRANSACTION;

UPDATE students

SET department_id=999

WHERE student_id=2;

ROLLBACK;

SELECT *
FROM students
WHERE student_id=2;

---------------------------------------------------
-- 47. SAVEPOINT Test
---------------------------------------------------

START TRANSACTION;

INSERT INTO enrollments
(student_id,course_id,enrollment_date)

VALUES
(
2,
2,
'2026-06-22'
);

SAVEPOINT first_insert;

INSERT INTO enrollments
(student_id,course_id,enrollment_date)

VALUES
(
999,
1,
'2026-06-22'
);

ROLLBACK TO first_insert;

COMMIT;

---------------------------------------------------
-- Verify
---------------------------------------------------

SELECT *
FROM enrollments
WHERE student_id=2;