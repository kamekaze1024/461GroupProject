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
	Agency_Name TEXT,
	Street TEXT,
	City TEXT,
	State TEXT,
	Phone_Number TEXT,
	PRIMARY KEY(Agency_ID)
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


