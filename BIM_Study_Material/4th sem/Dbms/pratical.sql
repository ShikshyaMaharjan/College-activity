CREATE TABLE student (
    id INT PRIMARY KEY,
    NAME VARCHAR(50),
    marks INT
);

INSERT INTO student(id, NAME, marks)
VALUES (1, 'Ram', 80,),
(2, 'Sita', 75,),
(3, 'Hari', 90,),
(4, 'Gita', 60,);

1.
SELECT COUNT(*) AS total_students
FROM student;

SELECT SUM(marks) AS total_marks
FROM student;


SELECT * FROM student;


SELECT COUNT(*) AS total_students FROM student;

SELECT SUM(marks) AS total_marks FROM student;

SELECT AVG(marks) AS average_marks FROM student;

SELECT MAX(marks) AS highest_marks FROM student;

SELECT MIN(marks) AS lowest_marks FROM student;

2.
-- Create second table
CREATE TABLE  student_new (
    id INT PRIMARY KEY,
    NAME VARCHAR(50),
    marks INT
);

-- Insert data
INSERT INTO student_new VALUES (4, 'Gita', 60);
INSERT INTO student_new VALUES (5, 'Anita', 85);
INSERT INTO student_new VALUES (6, 'Raju', 70);
INSERT INTO student_new VALUES (7, 'Maya', 95);

-- UNION
SELECT * FROM student
UNION
SELECT * FROM student_new;

-- INTERSECT
SELECT * FROM student
INTERSECT
SELECT * FROM student_new;

-- EXCEPT
SELECT * FROM student
EXCEPT
SELECT * FROM student_new;

3.
ALTER TABLE student
ADD COLUMN city VARCHAR(50);

UPDATE student SET city = 'Kathmandu' WHERE id = 1;
UPDATE student SET city = 'Dharan' WHERE id = 2;
UPDATE student SET city = 'Pokhara' WHERE id = 3;
UPDATE student SET city = 'Dharan' WHERE id = 4;
UPDATE student SET city = 'Biratnagar' WHERE id = 5;


SELECT * FROM student
WHERE city = 'Dharan';

4. -- Write a query to display records from employee table First name start with 'S'.Last name ending by 'a' Names who have salary more than 40,000.

CREATE TABLE  employee (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    salary DECIMAL(10,2)
);

INSERT INTO employee VALUES (1, 'Sita', 'Sharma', 35000);
INSERT INTO employee VALUES (2, 'Sunil', 'Koirala', 45000);
INSERT INTO employee VALUES (3, 'Rita', 'Shrestha', 50000);
INSERT INTO employee VALUES (4, 'Sanjay', 'Gurung', 42000);
INSERT INTO employee VALUES (5, 'Sarita', 'Poudel', 38000);
INSERT INTO employee VALUES (6, 'Hari', 'Sharma', 48000);

SELECT * FROM employee
WHERE first_name LIKE 'S%';

SELECT * FROM employee
WHERE last_name LIKE '%a';

SELECT * FROM employee
WHERE salary > 40000;
  
  
  -- set B
 
 1.
 CREATE TABLE  employee1 (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    salary DECIMAL(10,2),
    department VARCHAR(50)
);

INSERT INTO employee1 VALUES (1, 'Shikshya', 'Mahrajan', 45000, 'HR');
INSERT INTO employee1 VALUES (2, 'Sweta', 'Koirala', 50000, 'IT');
INSERT INTO employee1 VALUES (3, 'sita', 'Shrestha', 55000, 'Finance');
INSERT INTO employee1 VALUES (4, 'Sanjay', 'Adhikari', 40000, 'IT');

SELECT * FROM employee1
WHERE salary > (SELECT AVG(salary) FROM employee1);

SELECT * FROM employee1
WHERE salary = (SELECT MAX(salary) FROM employee1);

SELECT * FROM employee1
WHERE salary < (SELECT MAX(salary) FROM employee1);

2.
-- Write SQL code to display records from two tables i.e. employee and department table using UNION operator.
-- Create employee table
CREATE TABLE  IF NOT EXISTS employee (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    salary DECIMAL(10,2)
);

INSERT INTO employee VALUES (101, 'Sita', 'Sharma', 45000);
INSERT INTO employee VALUES (102, 'Sunil', 'Koirala', 50000);
INSERT INTO employee VALUES (103, 'Rita', 'Shrestha', 55000);
INSERT INTO employee VALUES (104, 'Sanjay', 'Adhikari', 40000);

-- Create department table
CREATE TABLE  department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

INSERT INTO department VALUES (101, 'HR');
INSERT INTO department VALUES (102, 'IT');
INSERT INTO department VALUES (103, 'Finance');
INSERT INTO department VALUES (104, 'Marketing');

-- Display records using UNION
SELECT first_name AS NAME FROM employee
UNION
SELECT dept_name AS NAME FROM department;

-- Display records using UNION ALL (optional)
SELECT first_name AS NAME FROM employee
UNION ALL
SELECT dept_name AS NAME FROM department;

3.
-- Create employee master table
CREATE TABLE emp_master(
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    salary INT,
    branch_id INT
);

-- Insert 3 employees
INSERT INTO emp_master VALUES (1, 'aarya', 50000, 101);
INSERT INTO emp_master VALUES (2, 'sweta', 60000, 102);
INSERT INTO emp_master VALUES (3, 'luniva', 55000, 103);

-- Create branch master table
CREATE TABLE br_master(
    br_id INT PRIMARY KEY,
    br_name VARCHAR(100),
    location VARCHAR(100)
);

-- Insert 3 branches
INSERT INTO br_master VALUES (101, 'Head Office', 'Kathmandu');
INSERT INTO br_master VALUES (102, 'Regional Office', 'Pokhara');
INSERT INTO br_master VALUES (104, 'Branch Office', 'Dharan'); -- note: 104, no employee linked


SELECT e.emp_id, e.emp_name, e.salary, b.br_name, b.location
FROM emp_master e
INNER JOIN br_master b
ON e.branch_id = b.br_id;



SELECT e.emp_id, e.emp_name, e.salary, b.br_name, b.location
FROM emp_master e
LEFT JOIN br_master b
ON e.branch_id = b.br_id;


SELECT e.emp_id, e.emp_name, e.salary, b.br_name, b.location
FROM emp_master e
RIGHT JOIN br_master b
ON e.branch_id = b.br_id;
 
-- full ko 
SELECT e.emp_id, e.emp_name, e.salary, b.br_name, b.location
FROM emp_master e
LEFT JOIN br_master b
ON e.branch_id = b.br_id

UNION

SELECT e.emp_id, e.emp_name, e.salary, b.br_name, b.location
FROM emp_master e
RIGHT JOIN br_master b
ON e.branch_id = b.br_id;






