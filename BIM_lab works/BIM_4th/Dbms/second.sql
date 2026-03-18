CREATE DATABASE students_mgmtB;

CREATE TABLE course(
cid VARCHAR(10) PRIMARY KEY,
course_name VARCHAR(25) NOT NULL
);

USE students_mgmtB;

CREATE TABLE student(
roll INT PRIMARY KEY,
sname VARCHAR(25) NOT NULL,
address VARCHAR(25),
phone NUMERIC(10,0),
cid VARCHAR(10)
);

USE students_mgmtb;

ALTER TABLE student
ADD email VARCHAR(30);

ALTER TABLE course
ADD faculty VARCHAR(26);

SELECT * FROM course;

INSERT INTO course(cid,course_name,faculty)
VALUES ('BIM','Bachelors in Information Management','IT'),
('BHM','Bachelors in Hotel Management','Management'),
('Bcs','Bachelors in Information Management','IT'),
('BCA','Bachelors in Computer Application','IT'),
('BSc.CSIT','Bachelors in Computer Science & IT','IT'),
('BBM','Bachelors in Business Management','Management'),
('BBA','Bachelors in Business Admimistration','Management'),
('BE','Bachelors in Engineering','Science'),
('BFA','Bachelors in Fine Arts','Arts');

SELECT * FROM course;

INSERT INTO student(roll, sname, address, phone, cid, email)
VALUES
(1, 'Aman Nepal', 'Kritipur', 9856647547, 'BIM', 'aman.nepal1@gmail.com'),
(2, 'Ram Karki', 'Lalitpur', 9855465744, 'BHM', 'ram.karki2@gmail.com'),
(3, 'Sita Maharjan', 'Chitwan', 9856647456, 'BCA', 'sita.maharjan3@gmail.com'),
(4, 'Aarya Tuladhar', 'Bhaktapur', 9841234567, 'BAC', 'aarya.tuladhar4@gmail.com'),
(5, 'Suman Shrestha', 'Pokhara', 9801234567, 'BBA', 'suman.shrestha5@gmail.com'),
(6, 'Bibek Rai', 'Dharan', 9811234567, 'BBM', 'bibek.rai6@gmail.com'),
(7, 'Rekha Gurung', 'Butwal', 9821234567, 'BSc.CSIT', 'rekha.gurung7@gmail.com'),
(8, 'Kishor Tamang', 'Biratnagar', 9831234567, 'BE', 'kishor.tamang8@gmail.com'),
(9, 'Sarita Thapa', 'Janakpur', 9842234567, 'BFA', 'sarita.thapa9@gmail.com'),
(10, 'Manoj Basnet', 'Itahari', 9851234567, 'BIM', 'manoj.basnet10@gmail.com'),
(11, 'Nisha Khadka', 'Hetauda', 9861234567, 'BHM', 'nisha.khadka11@gmail.com'),
(12, 'Kamal Shah', 'Birgunj', 9871234567, 'BBA', 'kamal.shah12@gmail.com'),
(13, 'Rina KC', 'Tansen', 9881234567, 'BAC', 'rina.kc13@gmail.com'),
(14, 'Anil Lama', 'Nepalgunj', 9891234567, 'BCA', 'anil.lama14@gmail.com'),
(15, 'Bimala Acharya', 'Dhangadhi', 9802234567, 'BE', 'bimala.acharya15@gmail.com'),
(16, 'Dipak Bista', 'Surkhet', 9812234567, 'BBM', 'dipak.bista16@gmail.com'),
(17, 'Mina Adhikari', 'Ghorahi', 9822234567, 'BSc.CSIT', 'mina.adhikari17@gmail.com'),
(18, 'Raju Yadav', 'Kohalpur', 9832234567, 'BFA', 'raju.yadav18@gmail.com'),
(19, 'Pooja Singh', 'Banepa', 9843234567, 'BIM', 'pooja.singh19@gmail.com'),
(20, 'Sandeep Maharjan', 'Tokha', 9852234567, 'BHM', 'sandeep.maharjan20@gmail.com');




