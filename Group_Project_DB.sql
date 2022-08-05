--To create database and see error output, use the following command in the terminal:
--sqlite3 "Group_Project.db" ".read 'Group_Project_DB.sql'"

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

INSERT INTO Office VALUES('Northeast Office', 'New York City', 2000);
INSERT INTO Office VALUES('West Office', 'San Francisco', 4000);
INSERT INTO Agency VALUES(1, 'Northeast Office', 'Rhode Island Agency', 
	'1234 Cherry Ln.', 'Providence', 'RI', '1234567890');
INSERT INTO Agency VALUES(2, 'Northeast Office', 'New York Agency', 
	'9876 Times Sq.', 'New York City', 'NY', '2345678901');
INSERT INTO Agency VALUES(3, 'West Office', 'Los Angeles Agency', 
	'5432 Main St.', 'Los Angeles', 'CA', '3456789012');
INSERT INTO Agency VALUES(4, 'West Office', 'San Francisco Agency', 
	'7890 Central St.', 'San Francisco', 'CA', '4567890123');
INSERT INTO Rental_Agreement VALUES(1, 'Northeast Office', 10000, 
	DATE('2020-01-01'), DATE('2022-06-01'));
INSERT INTO Rental_Agreement VALUES(2, 'Northeast Office', 15000,
	DATE('2019-01-01'), DATE('2022-12-01'));
INSERT INTO Rental_Agreement VALUES(3, 'West Office', 20000,
	DATE('2021-01-01'), DATE('2023-06-01'));
INSERT INTO Agrees VALUES(1, 1);
INSERT INTO Agrees VALUES(1, 2);
INSERT INTO Agrees VALUES(2, 1);
INSERT INTO Agrees VALUES(2, 3);
INSERT INTO Agrees VALUES(3, 4);
