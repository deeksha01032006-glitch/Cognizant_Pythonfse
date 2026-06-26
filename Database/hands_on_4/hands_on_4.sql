---------------------------------------------------
-- HANDS ON 4
-- TASK 1
-- BASELINE PERFORMANCE
---------------------------------------------------

USE college_db;

EXPLAIN FORMAT=JSON

SELECT
s.first_name,
s.last_name,
c.course_name

FROM enrollments e

JOIN students s
ON s.student_id=e.student_id

JOIN courses c
ON c.course_id=e.course_id

WHERE s.enrollment_year=2022;

---------------------------------------------------
-- COMMENTS
---------------------------------------------------

-- Check JSON output
-- Look for:
-- "access_type":"ALL"

-- ALL = Full Table Scan

-- Note rows examined
-- Example:
-- rows_examined_per_scan: 8

-- Save observations here
---------------------------------------------------
-- TASK 1 ANALYSIS
---------------------------------------------------

-- EXPLAIN FORMAT=JSON output:

-- Table:
-- students

-- access_type:
-- ALL

-- Meaning:
-- Full Table Scan

-- query_cost:
-- 2.30

-- Observation:
-- Query scans entire students table because
-- no index exists on enrollment_year.

-- Optimization required:
-- Create index on enrollment_year.
USE college_db;

CREATE INDEX idx_students_year
ON students(enrollment_year);
CREATE UNIQUE INDEX idx_enrollments_unique
ON enrollments(student_id,course_id);
CREATE INDEX idx_course_code
ON courses(course_code);
EXPLAIN FORMAT=JSON

SELECT
s.first_name,
s.last_name,
c.course_name

FROM enrollments e

JOIN students s
ON s.student_id=e.student_id

JOIN courses c
ON c.course_id=e.course_id

WHERE s.enrollment_year=2022;
---------------------------------------------------
-- TASK 2 ANALYSIS
---------------------------------------------------

-- BEFORE INDEX

-- access_type = ALL
-- query_cost = 2.30

-- Meaning:
-- Full Table Scan

---------------------------------------------------

-- AFTER INDEX

-- access_type = ref
-- query_cost = 4.60

-- Meaning:
-- Index Scan used

-- Observation:
-- Query now uses the
-- enrollment_year index.

-- Improvement:
-- Reduced table scanning and
-- improved lookup efficiency.
---------------------------------------------------
-- TASK 3 ANALYSIS
---------------------------------------------------

-- N+1:
-- 1 query to fetch enrollments
-- + N queries for students

-- Total:
-- 13 queries

-- Optimized JOIN:
-- 1 query

-- For 10000 rows:
-- N+1 = 10001 queries
-- JOIN = 1 query