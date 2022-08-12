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
#              SOAP database and performs insertion, deletion, and
#              selection operations as well as custom SQL statements.
import sqlite3
from datetime import datetime

# menu_for_tables() displays a menu to interact with the databse
# Parameters:       None
# Return:           table name string
def menu_for_tables():
    print("Choose from the tables below:")
    print("A) Agency")
    print("B) Office")
    print("C) Rental Agreement")
    print("D) Agrees")
    ret_val = ""
    while(True):
        user_choice = input("Choice: ").upper()
        if user_choice == "A":
            ret_val = "Agency"
            break
        elif user_choice == "B":
            ret_val = "Office"
            break
        elif user_choice == "C":
            ret_val = "Rental_Agreement"
            break
        elif user_choice == "D":
            ret_val = "Agrees"
            break
        else:
            print("Invalid selection, please enter A, B, C, or D.")
    print("You chose the " + ret_val + " table.")
    return ret_val
    
# convert_to_date(dt_str) converts a string to a date
# Parameters: dt_str:     a date stored as a string
# Return:                 a date formatted as a date
def convert_to_date(dt_str):
    try:
        date = datetime.strptime(str(dt_str), "%Y-%m-%d").date()
    except ValueError:
        raise ValueError
    return date

# insert(table, cursor) inserts into a table
# Parameters:           table: the selected table name string
#                       cursor: object that helps execute query by fetching records from database
# Return:               None
def insert(table, cursor):
    if table == "Agency":
        try:
            agency_id   = int(input("Enter the agency id: "))
        except ValueError:
            print("Error: invalid type, enter an integer.")
            return
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
    if table == "Rental_Agreement":
        try:
            agreement_id = int(input("Enter agreement id: "))
        except ValueError:
            print("Error: invalid type, enter an integer.")
            return
        office_name = input("Enter the office name: ")
        try:
            rent_amount = float(input("Enter rent amount: "))
        except ValueError:
            print("Error: invalid type, enter a decimal number.")
            return
        try:
            begin_date = convert_to_date(input("Enter a begin date ? (in YYYY-MM-DD):  "))
        except ValueError:
            print("Error: invalid date format, enter a date in YYYY-MM-DD")
            return
        try:
            end_date = convert_to_date(input("Enter an end date ? (in YYYY-MM-DD):  "))
        except ValueError:
            print("Error: invalid date format, enter a date in YYYY-MM-DD")
            return
        row_to_insert = (agreement_id, office_name, rent_amount, begin_date, end_date)
        try:
            cursor.execute("insert into Rental_Agreement values(?,?,?,?,?)", row_to_insert)
        except sqlite3.Error as e:
            print("Error occurred: ", e)
    if table == "Agrees":
        try:
            agreement_id = int(input("Enter agreement id: "))
        except ValueError:
            print("Error: invalid type, enter an integer.")
            return
        try:
            agency_id = int(input("Enter the agency id: "))
        except ValueError:
            print("Error: invalid type, enter an integer.")
            return
        row_to_insert = (agreement_id, agency_id)
        try:
            cursor.execute("insert into Agrees values(?,?)", row_to_insert)
        except sqlite3.Error as e:
            print("Error occurred: ", e)

# delete(table, cursor) deletes an entry from a table
# Parameters:           table: the selected table name string
#                       cursor: object that helps execute query by fetching records from database
# Return:               None
def delete(table, cursor):
    if table == "Agency":
        user_choice = 1
        row_to_delete = []
        for item in cursor.execute("select * from Agency"):
            print("%d) "%user_choice, end="")
            print(item)
            user_choice += 1
            row_to_delete.append(item[0])
        user_choice = int(input("Pick a row to delete: "))
        if user_choice < 1 or user_choice > len(row_to_delete):
            print("Error: Index out of range.")
            return
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
        if user_choice < 1 or user_choice > len(row_to_delete):
            print("Error: Index out of range.")
            return
        try:
            cursor.execute("delete from Office where Office_Name =(?)", [row_to_delete[user_choice - 1]])
        except sqlite3.Error as e:
            print("Error occurred: ", e)
    elif table == "Rental_Agreement":
        user_choice = 1
        row_to_delete = []
        for item in cursor.execute("select * from Rental_Agreement"):
            print("%d) "%user_choice, end="")
            print(item)
            user_choice += 1
            row_to_delete.append(item[0])
        user_choice = int(input("Pick a row to delete: "))
        if user_choice < 1 or user_choice > len(row_to_delete):
            print("Error: Index out of range.")
            return
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
        if user_choice < 1 or user_choice > len(row_to_delete):
            print("Error: Index out of range.")
            return
        try:
            cursor.execute("delete from Agrees where Agreement_ID =(?) and Agency_ID = (?)", 
                [row_to_delete[user_choice - 1][0], row_to_delete[user_choice - 1][1]])
        except sqlite3.Error as e:
            print("Error occurred: ", e)

# select(table, cursor) selects an entry from a table
# Parameters:           table: the selected table name string
#                       cursor: object that helps execute query by fetching records from database
# Return:               None
def select(table, cursor):
    try:
        for item in cursor.execute("select * from " + table):
            print(item)
    except sqlite3.Error as e:
        print("Error occurred: ", e)

# sql_statement(statement, cursor) executes a sql statement on the database
# Parameters:                      statement: the sql statement string to be executed
#                                  cursor: object that helps execute query by fetching records from database
# Return:                          None
def sql_statement(statement, cursor):
    try:
        cursor.execute(statement)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print("Error occurred: ", e)

if __name__ == "__main__":
    connection = sqlite3.connect("SOAP.db")
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    while(True):
        user_choice = input("Enter (I): for insert (D): for delete (S): for select " + 
                            "(E): to enter SQL statement (Q): to quit: ").upper()
        if user_choice == "I":
            insert(menu_for_tables(), cursor)
            connection.commit()
        elif user_choice == "D":
            delete(menu_for_tables(), cursor) 
            connection.commit()
        elif user_choice == "S":
            select(menu_for_tables(), cursor)
            #No need to call connection.commit() because this function doesn't alter database.
        elif user_choice == "E":
            statement = input("Enter a SQL statement: ")
            sql_statement(statement, cursor)
            connection.commit()
        elif user_choice == "Q":
            print("Quitting...")
            break
        else:
            print("Invalid choice, please enter (I), (D), (S), (E), or (Q).")       
    connection.close()
