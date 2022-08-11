# File: Group_project_pyscript.py
# Authors: Sabila Bernard
#          Obinna Ezejiofor
#          Talha Hussain
#          Raj Karsalia
#          Quinn Mood
#          Sneha Philip
#          Nicholas Stommel
#          Ulfina Wakjira
#          Scott Witschey
# Date: 8/8/2022
# Section: 01
# Description: python sqlite3 application that accesses the
#              SOAP database and perform insertion, deletion, and
#              selection operations.
import sqlite3
from datetime import datetime

# menu_for_tables() displays a menu to interact with the databse
# Parameters:       None
# Return:           None
def menu_for_tables():
    print("Choose from the tables below:")
    print("A) Agency")
    print("B) Office")
    print("C) Rental Agreement")
    print("D) Agrees")
    while(True):
        user_choice = input("Choice: ").upper()
        if user_choice == "A":
            return "Agency"
        elif user_choice == "B":
            return "Office"
        elif user_choice == "C":
            return "Rental_Agreement"
        elif user_choice == "D":
            return "Agrees"
        else:
            print("Invalid selection, please enter A, B, C, or D.")
        
# convert_to_date(dt_str) converts a string to a date
# Parameters: dt_str:     a date stored as a string
# Return:                 a date formatted as a date
def convert_to_date(dt_str):
    date = datetime.strptime(str(dt_str), "%Y-%m-%d").date()
    return date

# Insert(table, cursor) inserts into a table
# Parameters:           table: the selected table
#                       cursor: object that helps execute query by fetching records from database
# Return:               None
def Insert(table,cursor):
    print(table)
    if table == "Agency":
         agency_id   = int(input("Enter the agency id: "))
         agency_name = input("Enter the agency name: ")
         street = input("Enter the street address of the agency: ") 
         city = input("Enter the city of the agency: ")
         state  = input("Enter the State of the agency: ")
         phone_number= input("Enter the Phone number of the agency: ")
         # This is the tuple that is going to be inserted into the table
         row_to_insert = (agency_id, agency_name, street, city, state, phone_number)
         try:
            cursor.execute("insert into Agency values (?,?,?,?,?,?)", row_to_insert)
         except sqlite3.Error as e:
            print("Error occurred: ", e)
    if table == "Office":
        office_name = input("Enter the name of the office: ")
        city = input("Enter the city of the office: ")
        state = input("Enter the state of the office: ")
        square_footage = int(input("Enter the square footage of the office: "))
        row_to_insert = (office_name, city, state, square_footage)
        try:
            cursor.execute("insert into Office values(?,?,?,?)", row_to_insert)
        except sqlite3.Error as e:
            print("Error occurred: ", e)
    if table == "Rental Agreement":
        agreement_id = int(input("Enter agreement id: "))
        office_name = input("Enter the office name: ")
        rent_amount = float(input("Enter rent amount: "))
        begin_date = convert_to_date(input("Enter a begin date ? (in YYYY-MM-DD):  "))
        end_date = convert_to_date(input("Enter an end date ? (in YYYY-MM-DD):  "))
        row_to_insert = (agreement_id, office_name, rent_amount, begin_date, end_date)
        try:
            cursor.execute("insert into Rental_Agreement values(?,?,?,?,?)", row_to_insert)
        except sqlite3.Error as e:
            print("Error occurred: ", e)
    if table == "Agrees":
        agreement_id = int(input("Enter agreement id: "))
        agency_id = int(input("Enter the agency id: "))
        row_to_insert = (agreement_id, agency_id)
        try:
            cursor.execute("insert into Agrees values(?,?)", row_to_insert)
        except sqlite3.Error as e:
            print("Error occurred: ", e)

# Delete(table, cursor) deletes an entry from a table
# Parameters:           table: the selected table
#                       cursor: object that helps execute query by fetching records from database
# Return:               None
def Delete(table,cursor):
    if table == "Agency":
        user_choice = 1
        row_to_delete = []
        for item in cursor.execute("select * from Agency"):
            print("%d) "%user_choice, end="")
            print(item)
            user_choice += 1
            row_to_delete.append(item[0])
        user_choice = int(input("Pick a row to delete: "))
        try:
            cursor.execute("delete from Agency where Agency_ID=(?)", [row_to_delete[user_choice - 1]])
        except sqlite3.Error as e:
             print("Error occurred: ", e)           
    elif table == "Office":
        user_choice = 1
        row_to_delete = []
        for item in cursor.execute("select * from Office"):
            print("%d) "%user_choice, end="")
            print(item)
            user_choice += 1
            row_to_delete.append(item[0])
        user_choice = int(input("Pick a row to delete: "))
        try:
            cursor.execute("delete from Office where Office_Name =(?)", [row_to_delete[user_choice - 1]])
        except sqlite3.Error as e:
            print("Error occurred: ", e)
    elif table == "Rental Agreement":
        user_choice = 1
        row_to_delete = []
        for item in cursor.execute("select * from Rental_Agreement"):
            print("%d) "%user_choice, end="")
            print(item)
            user_choice += 1
            row_to_delete.append(item[0])
        user_choice = int(input("Pick a row to delete: "))
        try:
            cursor.execute("delete from Rental_Agreement where Agreement_ID =(?)", [row_to_delete[user_choice - 1]])
        except sqlite3.Error as e:
            print("Error occurred: ", e)
    elif table == "Agrees":
        user_choice = 1
        row_to_delete = []
        for item in cursor.execute("select * from Agrees"):
            print("%d) "%user_choice, end="")
            print(item)
            user_choice += 1
            row_to_delete.append([item[0], item[1]])
        user_choice = int(input("Pick a row to delete: "))
        try:
            cursor.execute("delete from Agrees where Agreement_ID =(?) and Agency_ID = (?)", 
                [row_to_delete[user_choice - 1][0], row_to_delete[user_choice - 1][1]])
        except sqlite3.Error as e:
            print("Error occurred: ", e)

# Select(table, cursor) selects an entry from a table
# Parameters:           table: the selected table
#                       cursor: object that helps execute query by fetching records from database
# Return:               None
def Select(table,cursor):
    try:
        for item in cursor.execute("select * from " + table):
            print(item)
    except sqlite3.Error as e:
        print("Error occurred: ", e)

# SQL_statement(statement, cursor) executes a sql statement on the database
# Parameters:                      statement: the sql statement to be executed
#                                  cursor: object that helps execute query by fetching records from database
# Return:                          None
def SQL_statement(statement,cursor):
    try:
        cursor.execute(statement)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print("Error occurred: ", e)

if __name__ == "__main__":
    conn = sqlite3.connect("SOAP.db")
    c = conn.cursor()

    while(True):
        user_choice = input("Enter I: for insert D: for delete S: for select " + 
                            "E: to enter SQL statement Q: to quit: ").upper()
        if user_choice == "I":
            Insert(menu_for_tables(), c)
            conn.commit()
        elif user_choice == "S":
            Select(menu_for_tables(), c)
            conn.commit()
        elif user_choice == "D":
            Delete(menu_for_tables(), c) 
            conn.commit()
        elif user_choice == "E":
            statement = input("Enter a SQL statement: ")
            SQL_statement(statement, c)
            conn.commit()
        elif user_choice == "Q":
            print("Quitting...")
            break
        else:
            print("Invalid choice, please select I, D, S, E, or Q.")
        
    conn.close()
