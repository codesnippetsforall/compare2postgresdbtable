# compare2postgresdbtable
Python script to compare 2 Postgres Databases and compare rows for a specific table

*Python:*

Install packages for Python:
> pip install pandas
> pip install sqlalchemy

*Database:*

Download Postgres: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

Install Postgres 13.11 (or preferred as per your requirement)

> Create 2 Databases
> payroll_dev, payroll_qa

> Create 1 table in both the Databases
> employee and run below sql queries

CREATE TABLE IF NOT EXISTS employee ( 

	employee_id int, 
 
	employee_name varchar(50) NOT NULL, 
 
	employee_age smallint NOT NULL, 
 
	employee_sex char(1) NOT NULL, 
 
	PRIMARY KEY (employee_id) 
 
) 

--
-- Dumping data for table `employee`
--

INSERT INTO employee (employee_id, employee_name, employee_age, employee_sex) VALUES (1234567, 'Test1', 38, 'M');

INSERT INTO employee (employee_id, employee_name, employee_age, employee_sex) VALUES (234567, 'Test2', 39, 'M');

INSERT INTO employee (employee_id, employee_name, employee_age, employee_sex) VALUES (234568, 'Test3', 40, 'M');

INSERT INTO employee (employee_id, employee_name, employee_age, employee_sex) VALUES (234569, 'Test4', 41, 'F'); 

COMMIT;


