CREATE TABLE employee(
ID INT PRIMARY KEY,
e_name VARCHAR(15) NOT NULL,
Did INT,
Salary NUMERIC(10,2),
JoiningDate DATE,
Performance_Rating VARCHAR(1),
FOREIGN KEY(Did) REFERENCES Department(Did)
);
DROP TABLE employee;
CREATE TABLE Department(
Did INT PRIMARY KEY,
Department VARCHAR(25)
);

DROP TABLE Department;

INSERT INTO Department(Did,Department)
VALUES (100,'HR'),
(101,'IT'),(102,'Sales'),(103,'Marketing');
4
INSERT INTO employee (ID,e_name,Did,Salary,JoiningDate,Performance_Rating)
VALUES (1,'Alice',100,45000,'2020-01-01','A'),
(2,'Bob',101,55000,'2021-02-15','B'),
(3,'Charlie',102,48000,'2019-03-20','A'),
(4,'Diana',103,5000,'2020-04-10','C'),
(5,'Ethan',102,60000,'2021-05-21','B'),
(6,'Fiona',103,47000,'2019-06-13','A'),
(7,'George',100,44000,'2022-07-12','C'),
(8,'Hannah',103,52000,'2021-08-18','B'),
(9,'John',103,42000,'2021-08-09','A');
5
SELECT * FROM employee
WHERE Did IN
(SELECT Did FROM Department WHERE Department='Marketing');

6
SELECT e_name,Performance_Rating FROM employee
WHERE Performance_Rating IN (SELECT Performance_Rating FROM employee WHERE Salary>46000);

7
SELECT SUM(Salary) AS total_salary,
AVG(Salary) AS avg_salary, 
MIN(Salary) AS min_salary,
MAX(Salary) AS max_salary
FROM employee;