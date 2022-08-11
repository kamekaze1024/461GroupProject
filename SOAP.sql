--To create database and see error output, use the following command in the terminal:
--sqlite3 "SOAP.db" ".read 'SOAP.sql'"

PRAGMA foreign_keys = ON;

DROP TABLE Agrees;
DROP TABLE Rental_Agreement;
DROP TABLE Agency;
DROP TABLE Office;

CREATE TABLE Office (
	Office_Name TEXT NOT NULL,
	Office_City TEXT,
	Square_Footage INTEGER,
	PRIMARY KEY(Office_Name)
);

CREATE TABLE Agency (
	Agency_ID INTEGER NOT NULL,
	Office_Name TEXT NOT NULL,
	Agency_Name TEXT,
	Street TEXT,
	City TEXT,
	State TEXT,
	Phone_Number TEXT,
	PRIMARY KEY(Agency_ID),
	FOREIGN KEY(Office_Name) REFERENCES Office(Office_Name)
);

CREATE TABLE Rental_Agreement (
	Agreement_ID INTEGER NOT NULL,
	Office_Name TEXT NOT NULL,
	Rent_Amount NUMERIC,
	Begin_Date DATE,
	End_Date DATE,
	PRIMARY KEY(Agreement_ID),
	FOREIGN KEY(Office_Name) REFERENCES Office(Office_Name)
);

CREATE TABLE Agrees (
	Agreement_ID INTEGER NOT NULL,
	Agency_ID INTEGER NOT NULL,
	PRIMARY KEY(Agreement_ID, Agency_ID),
	FOREIGN KEY(Agreement_ID) REFERENCES Rental_Agreement(Agreement_ID),
	FOREIGN KEY(Agency_ID) REFERENCES Agency(Agency_ID)
);

INSERT INTO Office VALUES('East Office', 'Frederick', 40000);
INSERT INTO Office VALUES('West Office', 'San Diego', 25000);
INSERT INTO Office VALUES('North Office', 'New York City', 30000);
INSERT INTO Office VALUES('South Office', 'Jacksonville', 10000);
INSERT INTO Agency VALUES(1, 'South Office', 'IRS', 
	'1240 Tax St.', 'Houston', 'TX', '616-637-9827');
INSERT INTO Agency VALUES(2, 'East Office', 'FBI', 
	'3412 Central St.', 'Baltimore', 'MD', '541-552-5356');
INSERT INTO Agency VALUES(3, 'East Office', 'NCI', 
	'5442 7th St.', 'Frederick', 'MD', '152-987-8035');
INSERT INTO Agency VALUES(4, 'West Office', 'NIH', 
	'7890 Central St.', 'San Francisco', 'CA', '456-789-0123');
INSERT INTO Agency VALUES(5, 'North Office', 'CIA', 
	'7841 Cherry Ln.', 'Boston', 'MA', '765-789-0981');
INSERT INTO Rental_Agreement VALUES(1, 'South Office', 10000, 
	DATE('2020-01-01'), DATE('2022-06-01'));
INSERT INTO Rental_Agreement VALUES(2, 'East Office', 15000,
	DATE('2019-01-01'), DATE('2022-12-01'));
INSERT INTO Rental_Agreement VALUES(3, 'West Office', 20000,
	DATE('2021-01-01'), DATE('2023-06-01'));
INSERT INTO Rental_Agreement VALUES(4, 'North Office', 30000,
	DATE('2021-06-01'), DATE('2023-06-01'));
INSERT INTO Agrees VALUES(1, 1);
INSERT INTO Agrees VALUES(1, 2);
INSERT INTO Agrees VALUES(2, 1);
INSERT INTO Agrees VALUES(2, 3);
INSERT INTO Agrees VALUES(3, 4);
INSERT INTO Agrees VALUES(4, 5);

