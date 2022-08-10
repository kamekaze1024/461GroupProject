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

from msilib.schema import Error
import sqlite3
from datetime import datetime

# menu_for_tables() displays a menu to interact with the databse
# Parameters:       None
# Return:           None
def menu_for_tables():
    print("Choose from the tables below:\n")
    print("A) Agency\n")
    print("B) Office\n")
    print("C) Rental Agreement\n")
    user_choice = input("Choice: ")
    if user_choice.upper() == "A":
        return "Agency"
    elif user_choice.upper() == "B":
        return "Office"
    elif user_choice.upper() == "C":
        return "Rental Agreement"

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
         Agency_ID   = int(input("Enter the Agency Id: "))
         Office_Name = input("Enter the Office name: ")
         Agency_Name = input("Enter the Agency name: ")
         Street = input("Enter the street of the address: ") 
         City = input("Enter the city of the Agency: ")
         State  = input("Enter the State of the Agency: ")
         Phone_Number= input("Enter the Phone number of the Agency: ")
         # This is the tuple that is going to be inserted into the table
         row_to_insert = (Agency_ID, Office_Name, Agency_Name, Street, City, State, Phone_Number)
         try:
            cursor.execute("insert into Agency values (?,?,?,?,?,?,?)", row_to_insert)
         except sqlite3.Error as e:
            print("error occured: ", e)
    if table == "Office":
        Office_Name = input("Enter the name of the office: ")
        Office_City = input("Enter the city of the office: ")
        Square_Footage = int(input("Enter the square footage of the office: "))
        row_to_insert = (Office_Name, Office_City, Square_Footage)
        try:
            cursor.execute("insert into Office values(?,?,?)",row_to_insert)
        except sqlite3.Error as e:
            print("error occured: ", e)
    if table == "Rental Agreement":
        Agreement_ID = int(input("Enter agreement id: "))
        Off_name = input("Enter the office name: ")
        Rent_amount = float(input("Enter rent amount: "))
        Begin_date = convert_to_date(input("Enter a begin date ? (in YYYY-MM-DD):  "))
        End_date = convert_to_date(input("Enter an end date ? (in YYYY-MM-DD):  "))
        row_to_insert = (Agreement_ID, Off_name, Rent_amount, Begin_date, End_date)
        try:
            cursor.execute("insert into Rental_Agreement values(?,?,?,?,?)", row_to_insert)
        except sqlite3.Error as e:
            print("error occured: ", e)

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
        print(row_to_delete[user_choice - 1])
        try:
            cursor.execute('delete from Agency where Agency_ID=(?)', [row_to_delete[user_choice - 1]])
        except sqlite3.Error as e:
             print("error occured: ", e)           
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
            cursor.execute('delete from Office where Office_Name =(?)', [row_to_delete[user_choice - 1]])
        except sqlite3.Error as e:
            print("error occured: ", e)
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
            cursor.execute('delete from Rental_Agreement where Agreement_ID =(?)', [row_to_delete[user_choice - 1]])
        except sqlite3.Error as e:
            print("error occured: ", e)

# Select(table, cursor) selects an entry from a table
# Parameters:           table: the selected table
#                       cursor: object that helps execute query by fetching records from database
# Return:               None
def Select(table,cursor):
    if table == "Agency":
        for item in cursor.execute("select * from Agency"):
            print(item)
    elif table == "Office":
        for item in cursor.execute("select * from Office"):
            print(item)
    elif table == "Rental Agreement":
        for item in cursor.execute("select * from Rental_Agreement"):
            print(item)

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
        print("error occured: ", e)

if __name__ == "__main__":
    conn = sqlite3.connect("SOAP.db")
    c = conn.cursor()
    user_choice = ""

    while(user_choice.upper() != 'Q'):
        user_choice = input("Enter I: for insert D: for delete S: for select " + 
                            "E: to enter SQL statement Q: to quit: ")
        if user_choice.upper() == 'I':
            Insert(menu_for_tables(), c)
            conn.commit()
        elif user_choice.upper() == 'S':
            Select(menu_for_tables(), c)
            conn.commit()
        elif user_choice.upper() == 'D':
            Delete(menu_for_tables(), c) 
            conn.commit()
        elif user_choice.upper() == 'E':
            statement = input("Enter a SQL statement: ")
            SQL_statement(statement, c)
            conn.commit()
    conn.close()
