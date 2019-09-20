--TODO Son put this into another file
-- 00.CREATE DATABASE PSQL_INTERN
CREATE DATABASE PSQL_INTERN;

--TODO Son what database the below script will run on
-- 01.CREATE TABLE CUSTOMERS
--TODO Son column name in lowercase please
CREATE TABLE CUSTOMERS(
	ID TEXT PRIMARY KEY, --TODO Son id as autoincrease please
	NAME TEXT NOT NULL,
	BIRTH DATE,
	ADDRESS VARCHAR(50),
	PHONE VARCHAR(20)
);

-- 02.INSERT DATA INTO TABLE
INSERT INTO customers VALUES ('A01','Tran Minh Thy','19870514','An Giang'
							 ,'0987978932');
INSERT INTO customers VALUES ('A02','Nguyen Van Be','19820123','Sai Gon'
							 ,'0981128932'),
							 ('A03','Cao Thanh Truc','19921224','Vung Tau'
							 ,'0911122333'),
							 ('A04','Nguyen Tan Tai','19881101','An Giang'
							 ,'0932122333');
							 
-- 03.QUERRY DATA FROM CUSTOMERS TABLE
SELECT * FROM CUSTOMERS;

-- 04.QUERRY THE YOUNGEST CUSTOMER IN THE LIST
SELECT * FROM CUSTOMERS
WHERE birth = (SELECT max(birth) as EarliestDate FROM customers);
