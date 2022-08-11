--To create database and see error output, use the following command in the terminal:
--sqlite3 "SOAP.db" ".read 'SOAP.sql'"

PRAGMA foreign_keys = ON;

DROP TABLE Agrees;
DROP TABLE Rental_Agreement;
DROP TABLE Agency;
DROP TABLE Office;

CREATE TABLE Office (
	Office_Name TEXT NOT NULL,
	City TEXT,
	State TEXT,
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

INSERT INTO Office VALUES('New England Regional Office', 'Boston', 'MA', 10000);
INSERT INTO Office VALUES('Northeast & Caribbean Regional Office', 'New York', 'NY', 20000);
INSERT INTO Office VALUES('Mid-Atlantic Regional Office', 'Philadelphia', 'PA', 15000);
INSERT INTO Office VALUES('Southeast Sunbelt Regional Office', 'Atlanta', 'GA', 25000);
INSERT INTO Office VALUES('Great Lakes Regional Office', 'Chicago', 'IL', 12000);
INSERT INTO Office VALUES('The Heartland Regional Office', 'Kansas City', 'MO', 10000);
INSERT INTO Office VALUES('Greater Southwest Regional Office', 'Ft. Worth', 'TX', 16000);
INSERT INTO Office VALUES('Rocky Mountain Regional Office', 'Denver', 'CO', 15000);
INSERT INTO Office VALUES('Pacific Rim Regional Office', 'San Francisco', 'CA', 20000);
INSERT INTO Office VALUES('Northwest & Arctic Regional Office', 'Auburn', 'WA', 15000);
INSERT INTO Office VALUES('National Capital Regional Headquarters', 'Washington', 'DC', 25000);
INSERT INTO Agency VALUES(1, 'Internal Revenue Service', 
	'12401 Tax St.', 'Houston', 'TX', '616-637-9827');
INSERT INTO Agency VALUES(2, 'Food and Drug Administration', 
	'34122 Central St.', 'Baltimore', 'MD', '541-552-5356');
INSERT INTO Agency VALUES(3, 'Federal Bureau of Investigation', 
	'54423 7th St.', 'Washington', 'DC', '152-987-8035');
INSERT INTO Agency VALUES(4, 'Centers for Disease Control', 
	'78901 2nd St.', 'San Francisco', 'CA', '456-789-0123');
INSERT INTO Agency VALUES(5, 'Central Intelligence Agency',
	'78412 Cherry Ln.', 'Boston', 'MA', '765-789-0981');
INSERT INTO Agency VALUES(6, 'Federal Aviation Administration', 
	'65175 Main St.', 'Tallahassee', 'FL', '142-908-7290');
INSERT INTO Agency VALUES(7, 'Federal Communications Exchange Commission', 
	'72893 5th St.', 'Albany', 'NY', '889-701-2036');
INSERT INTO Agency VALUES(8, 'National Institutes of Health', 
	'14023 Wellness St.', 'Boston', 'MA', '334-907-4522');
INSERT INTO Agency VALUES(9, 'Environmental Protection Agency', 
	'78418 Green Ln.', 'Atlanta', 'GA', '872-109-8089');
INSERT INTO Agency VALUES(10, 'National Security Agency', 
	'67392 Security Dr.', 'Charlestown', 'WV', '765-789-0981');

INSERT INTO Rental_Agreement VALUES(1, 'New England Regional Office', 10000, 
	DATE('2020-01-01'), DATE('2022-06-01'));
INSERT INTO Rental_Agreement VALUES(2, 'Northeast & Caribbean Regional Office', 15000,
	DATE('2019-01-01'), DATE('2022-12-01'));
INSERT INTO Rental_Agreement VALUES(3, 'Mid-Atlantic Regional Office', 20000,
	DATE('2021-01-01'), DATE('2023-06-01'));
INSERT INTO Rental_Agreement VALUES(4, 'Southeast Sunbelt Regional Office', 30000,
	DATE('2021-06-01'), DATE('2023-06-01'));
INSERT INTO Agrees VALUES(1, 1);
INSERT INTO Agrees VALUES(1, 2);
INSERT INTO Agrees VALUES(2, 1);
INSERT INTO Agrees VALUES(2, 3);
INSERT INTO Agrees VALUES(3, 4);
INSERT INTO Agrees VALUES(4, 5);







