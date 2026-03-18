CREATE DATABASE Bim4th;
CREATE TABLE employee(
eid INT PRIMARY KEY,
ename VARCHAR(15) NOT NULL,
address VARCHAR(10),
phone NUMERIC( 10,0)
);

DESCRIBE employee;

ALTER TABLE employee
ADD jobstatus VARCHAR(1);

ALTER TABLE employee
ADD email VARCHAR(25);

ALTER TABLE employee
DROP email;

INSERT INTO employee(eid, ename, address, phone, jobstatus)
VALUES(101, 'Rajesh Shakya', 'Tengal', 9841568844, 'P');

INSERT INTO employee(eid, ename, address, phone, jobstatus)
VALUES(102, 'SITA Shakya', 'Dallu', 9841565844, 'P'),
(103, 'Geeta Maharjan', 'Nardevi', 9841565854, 't'),
(104, 'Sweta Dangol', 'Kalimati', 9841565874, 'P'),
(105, 'Suhana Shrestha', 'Teku', 9841565847, 't'),
(106, 'Aarya Tuladhar', 'Lagan', 9841565847, 'P');

SELECT * FROM employee;
