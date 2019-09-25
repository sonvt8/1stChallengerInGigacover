-- 01.CREATE TABLE CUSTOMERS IN DATABASE PSQL_INTERN
DROP TABLE if exists customers;
CREATE TABLE CUSTOMERS(
	id serial PRIMARY KEY,
	name TEXT NOT NULL,
	birth DATE,
	address VARCHAR(50),
	phone VARCHAR(20)
);

-- 02.INSERT DATA INTO TABLE
INSERT INTO customers VALUES (default,'Tran Minh Thy','19870514','An Giang'
							 ,'0987978932'),
							 (default,'Nguyen Van Be','19820123','Sai Gon'
							 ,'0981128932'),
							 (default,'Cao Thanh Truc','19921224','Vung Tau'
							 ,'0911122333'),
							 (default,'Nguyen Tan Tai','19881101','An Giang'
							 ,'0932122333');
							 
-- 03.QUERRY DATA FROM CUSTOMERS TABLE
SELECT * FROM customers;

-- 04.QUERRY THE YOUNGEST CUSTOMER IN THE LIST
SELECT * FROM customers
WHERE birth = (SELECT max(birth) as EarliestDate FROM customers);
