CREATE DATABASE office_bim4thb;

CREATE TABLE employee(
eid INT PRIMARY KEY,
ename VARCHAR(20) NOT NULL,
address VARCHAR(15),
gender VARCHAR(6),
department VARCHAR(15),
post VARCHAR(15)
);

DROP DATABASE office_bim4thb;

CREATE DATABASE office_bim4thb;

CREATE TABLE employee(
eid INT PRIMARY KEY,
ename VARCHAR(20) NOT NULL,
address VARCHAR(15),
gender VARCHAR(6),
department VARCHAR(15),
post VARCHAR(15)
);

ALTER TABLE employee
ADD job_status VARCHAR(10);

CREATE TABLE salary(
eid INT PRIMARY KEY,
basic_sal INT,
allowance NUMERIC(10,2)DEFAULT 0,
d_allow NUMERIC (10,2) DEFAULT 0,
gross_sal NUMERIC(10,2) DEFAULT 0,
tax NUMERIC(10,2) DEFAULT 0,
net_sal NUMERIC(10,2) DEFAULT 0,
FOREIGN KEY (eid)REFERENCES employee(eid)
);

INSERT INTO employee(eid, ename,address, gender,department,post,job_status)
VALUES (101, 'Aman Nepal', 'Kritipur', 'Male', 'ADMIN', 'Officer', 'P'),
(102, 'Ram Karki', 'Lalitpur', 'Male', 'ADMIN', 'Assistant', 'T'),
(103, 'Sita Maharjan', 'Chitwan', 'Female', 'ACC', 'Officer', 'T'),
(104, 'Bibek Thapa', 'Kathmandu', 'Male', 'ACC', 'Manager', 'P'),
(105, 'Anju Shrestha', 'Chitwan', 'FeMale', 'ADMIN', 'Director', 'P'),
(106, 'Salin Malla', 'Lalitpur', 'Male', 'Sales', 'Manager', 'T'),
(107, 'Neeta Bista', 'Kritipur', 'Female', 'Sales', 'Officer', 'P'),
(108, 'Partham Dangol', 'Kathmandu', 'Male', 'Sales', 'Assistant', 'T'),
(109, 'Ritesh Basnet', 'Lalitpur', 'Male', 'Store', 'Officer', 'P'),
(110, 'Bisesh Baskota', 'Kathmandu', 'Male', 'Store', 'Assistant', 'P');

INSERT INTO salary(eid,basic_sal)
VALUES (101,50000),
(102,3300),
(103,50000),
(104,65000),
(105,75000),
(106,65000),
(107,50000),
(108,33000),
(109,50000),
(110,33000);

SELECT * FROM employee WHERE job_status='p';

SELECT * FROM employee WHERE ename LIKE 'A%';
SELECT * FROM employee WHERE ename NOT LIKE 'A%';
SELECT * FROM employee WHERE ename LIKE '__t%';
SELECT * FROM employee WHERE ename LIKE 'B%a';
SELECT * FROM employee WHERE post !='Manager';


UPDATE salary
SET allowance=0.15*basic_sal;

UPDATE salary AS s
JOIN employee AS e ON s.eid=e.eid
SET s.d_allow=0.10*s.basic_sal WHERE e.post='Manager'OR e.post='Director';

SELECT *FROM salary;

UPDATE salary
SET gross_sal=basic_sal+allowance+d_allow;

UPDATE salary
SET tax=0.075*gross_sal WHERE gross_sal>60000;

UPDATE salary
SET net_sal=gross_sal-tax;

SELECT e.eid,e.ename,e.post,s.basic_sal,s.allowance
FROM employee AS e
INNER JOIN salary AS s
ON e.eid=s.eid;

SELECT e.eid,e.ename,e.post,s.net_sal
FROM employee AS e
INNER JOIN salary AS s
ON e.eid=s.eid
WHERE e.post IN('Director','Manager','Officer');

SELECT e.eid,e.ename,e.post,s.net_sal
FROM employee AS e
INNER JOIN salary AS s
ON e.eid=s.eid
ORDER BY e.department;















