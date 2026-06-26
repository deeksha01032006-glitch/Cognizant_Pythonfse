import mysql.connector
import time

conn=mysql.connector.connect(
host="localhost",
user="root",
password="deeksha01",
database="college_db"
)

cur=conn.cursor()

print("VERSION 1")

start=time.time()

cur.execute(
"SELECT * FROM enrollments"
)

rows=cur.fetchall()

count=1

for row in rows:

    cur.execute(
    """
    SELECT first_name
    FROM students
    WHERE student_id=%s
    """,
    (row[1],)
    )

    cur.fetchone()

    count+=1

print(count,"queries executed")

print(
time.time()-start
)

print()

print("VERSION 2")

start=time.time()

cur.execute(
"""
SELECT
e.*,
s.first_name

FROM enrollments e

JOIN students s

ON e.student_id=
s.student_id
"""
)

cur.fetchall()

print("1 query executed")

print(
time.time()-start
)

conn.close()