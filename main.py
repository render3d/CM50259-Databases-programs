# DATABASES LAB 3.2 SUBMISSION
# https://repl.it/@render3d/Lab-32#main.py

import sqlite3

# Define DBOperation class to manage all data into the database. 
# Give a name of your choice to the database

class DBOperations:
  sql_create_table_firsttime = 'CREATE TABLE IF NOT EXISTS "Employees" ( \
  "EmployeeID"	Integer NOT NULL, \
	"empTitle"	Text, \
	"forename"	Text NOT NULL, \
	"surname"	Text NOT NULL, \
	"email"	Text, \
	"salary"	Real NOT NULL DEFAULT 0.0, \
	PRIMARY KEY("EmployeeID"), \
	CONSTRAINT "unique_EmployeeID" UNIQUE("EmployeeID"));'

  sql_create_table = 'CREATE TABLE "Employees" ( \
  "EmployeeID"	Integer NOT NULL, \
	"empTitle"	Text, \
	"forename"	Text NOT NULL, \
	"surname"	Text NOT NULL, \
	"email"	Text, \
	"salary"	Real NOT NULL DEFAULT 0.0, \
	PRIMARY KEY("EmployeeID"), \
	CONSTRAINT "unique_EmployeeID" UNIQUE("EmployeeID"));'

  sql_insert = "INSERT INTO Employees (EmployeeID,empTitle,forename,surname,email,salary) VALUES (?,?,?,?,?,?)"
  sql_select_all = "select * from Employees"
  sql_search = "select * from Employees where EmployeeID = ?"
  sql_update_data = "UPDATE Employees SET empTitle = ?,forename = ?,surname = ?,email = ?,salary = ? WHERE EmployeeID = ?"
  sql_delete_data = "DELETE FROM Employees WHERE EmployeeID = ?"
  sql_drop_table = "DROP TABLE IF EXISTS Employees" # Extra functionality
 
  def __init__(self):
    """ This function initialises the program and creates the table when it is first run """
    try:
      self.conn = sqlite3.connect("EmployeeData.db")
      self.cur = self.conn.cursor()
      self.cur.execute(self.sql_create_table_firsttime)
      self.conn.commit()
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def get_connection(self):
    """ This function establishes the connection and cursor """
    self.conn = sqlite3.connect("EmployeeData.db")
    self.cur = self.conn.cursor()

  def create_table(self):
    """ This function creates the table """
    try:
      self.get_connection()
      try:
        self.cur.execute(self.sql_create_table)
        self.conn.commit()
        print("Table created successfully")
      except:
        print("\nThis table is already created")      
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def insert_data(self):
    """ This function enables insertion of data to the table """
    try:
      self.get_connection()

      var_EmpIDn = input("Enter Employee ID: ")
      var_EmpTtl = input("Enter Employee Title: ")
      var_EmpPnm = input("Enter Employee Forename: ")
      var_EmpNom = input("Enter Employee Surname: ")
      var_EmpEml = input("Enter Employee Email Address: ")
      var_EmpSal = input("Enter Employee Salary: ")

      print("\n========================================================================\n")
      print("Employee ID:      ", var_EmpIDn)
      print("Employee Title:   ", var_EmpTtl)
      print("Employee Name:    ", var_EmpPnm)
      print("Employee Surname: ", var_EmpNom)
      print("Employee Email:   ", var_EmpEml)
      print("Employee Salary:  ", var_EmpSal)
      print("\n========================================================================\n")

      emp = Employee()
      emp.set_employee_id(int(var_EmpIDn))
      emp.set_employee_title(var_EmpTtl)
      emp.set_forename(var_EmpPnm)
      emp.set_surname(var_EmpNom)
      emp.set_email(var_EmpEml)
      emp.set_salary(float(var_EmpSal))

      self.cur.execute(self.sql_insert,tuple(str(emp).split("\n")))

      self.conn.commit()
      print("Inserted data successfully")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def select_all(self):
    """ This funtion displays all data in all rows of the table """
    try:
      self.get_connection()
      self.cur.execute(self.sql_select_all)
      results = self.cur.fetchall()

      # think how you could develop this method to show the records
      print("\n========================================================================\n")
      for record in results:
        print("Employee ID:       ", record[0])
        print("Employee Title:    ", record[1])
        print("Employee Name:     ", record[2])
        print("Employee Surname:  ", record[3])
        print("Employee Email:    ", record[4])
        print("Employee Salary:   ", record[5])
        print("\n======================================================================\n")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()
    
  def search_data(self):
    """ This function allows the user to search for an entry in the table """
    try:
      self.get_connection()
      employeeID = int(input("Enter Employee ID: "))
      print("")
      self.cur.execute(self.sql_search,tuple(str(employeeID)))
      result = self.cur.fetchone()
      if type(result) == type(tuple()):
        print("Search result:")
        for index, detail in enumerate(result):
          if index == 0:
            print("Employee ID:       " + str(detail))
          elif index == 1:
            print("Employee Title:    " + detail)
          elif index == 2:
            print("Employee Name:     " + detail)
          elif index == 3:
            print("Employee Surname:  " + detail)
          elif index == 4:
            print("Employee Email:    " + detail)
          else:
            print("Employee Salary:   "+ str(detail))
      else:
        print ("No Record")
            
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def update_data(self):
    """ This function allows the user to update data in a row in the table """
    try:
      self.get_connection()

      var_EmpIDn = input("Enter Employee ID: ")
      var_EmpTtl = input("Enter Employee Title: ")
      var_EmpPnm = input("Enter Employee Forename: ")
      var_EmpNom = input("Enter Employee Surname: ")
      var_EmpEml = input("Enter Employee Email Address: ")
      var_EmpSal = input("Enter Employee Salary: ")

      print("\n========================================================================\n")
      print("Employee ID:       ", var_EmpIDn)
      print("Employee Title:    ", var_EmpTtl)
      print("Employee Name:     ", var_EmpPnm)
      print("Employee Surname:  ", var_EmpNom)
      print("Employee Email:    ", var_EmpEml)
      print("Employee Salary:   ", var_EmpSal)
      print("\n========================================================================\n")

      emp = Employee()
      emp.set_employee_id(int(var_EmpIDn))
      emp.set_employee_title(var_EmpTtl)
      emp.set_forename(var_EmpPnm)
      emp.set_surname(var_EmpNom)
      emp.set_email(var_EmpEml)
      emp.set_salary(float(var_EmpSal))
        
      tup = (emp.empTitle,emp.forename,emp.surname,emp.email,emp.salary,emp.employeeID)

      # Update statement
      self.cur = self.conn.cursor()
      result = self.cur.execute(self.sql_update_data,tup)
                  
      if result.rowcount != 0:
        print ("\n"+str(result.rowcount)+ " Row(s) updated.")
        self.conn.commit()
      else:
        print ("\nCannot find this record in the database")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  # Define Delete_data method to delete data from the table. The user will need to input the employee id to delete the corrosponding record. 
  def delete_data(self):
    """ This function allows the user delete all data in a row in the table """
    try:
      self.get_connection()

      employeeID = int(input("Enter Employee ID: "))
      tupID = (employeeID,)

      result = self.cur.execute(self.sql_delete_data,tupID)
      
      if result.rowcount != 0:
        print ("\n"+str(result.rowcount)+" Row(s) deleted.")
        self.conn.commit()
      else:
        print ("\nCannot find this record in the database")

    except Exception as e:
      print(e)
    finally: 
      self.conn.close()

  def drop_table(self):
    """ This function allows the user to delete ALL the data in the table """
    try:
      self.get_connection()
      try:
        self.cur.execute(self.sql_drop_table)
        self.conn.commit()
        print("\nTable dropped successfully")
      except:
        print("Table does not exist.")      
    except Exception as e:
      print(e)
    finally:
      self.conn.close()
    
class Employee:
  """ This class formats the entries of user into compatible format amongst other things """
  def __init__(self):
    self.employeeID = 0
    self.empTitle = ''
    self.forename = ''
    self.surname = ''
    self.email = ''
    self.salary = 0.0

  def set_employee_id(self, employeeID):
    self.employeeID = employeeID

  def set_employee_title(self, empTitle):
    self.empTitle = empTitle

  def set_forename(self,forename):
   self.forename = forename
  
  def set_surname(self,surname):
    self.surname = surname

  def set_email(self,email):
    self.email = email
  
  def set_salary(self,salary):
    self.salary = salary
  
  def get_employee_id(self):
    return self.employeeId

  def get_employee_title(self):
    return self.empTitle
  
  def get_forename(self):
    return self.forename
  
  def get_surname(self):
    return self.surname
  
  def get_email(self):
    return self.email
  
  def get_salary(self):
    return self.salary

  def __str__(self):
    return str(self.employeeID)+"\n"+self.empTitle+"\n"+ self.forename+"\n"+self.surname+"\n"+self.email+"\n"+str(self.salary)

# The main function will parse arguments. 
# These argument will be definded by the users on the console.
# The user will select a choice from the menu to interact with the database.
db_ops = DBOperations() # This has been moved out of the infinite loop so that it is not repeated each time there is an input to the menu

while True:
  """ This infinitie loop allows continuous display of the menu and entry of program commands until the user decides to terminate the program in any number of way """
  try:
    print ("\n Menu:")
    print ("**********")
    print (" 1. Create table EmployeeUoB")
    print (" 2. Insert data into EmployeeUoB")
    print (" 3. Select all data in EmployeeUoB")
    print (" 4. Search an employee")
    print (" 5. Update data some records")
    print (" 6. Delete data some records")
    print (" 7. Drop the table EmployeeUoB")
    print (" 8. Exit (or press Ctrl + C or Ctrl + D)\n") # Extra functionality: exit program on Ctrl + C or Ctrl + D
    
    __choose_menu = int(input("Enter your choice: "))
  
    if __choose_menu == 1:
      db_ops.create_table()
    elif __choose_menu == 2:
      db_ops.insert_data()
    elif __choose_menu == 3:
      db_ops.select_all()
    elif __choose_menu == 4:
      db_ops.search_data()
    elif __choose_menu == 5:
      db_ops.update_data()
    elif __choose_menu == 6:
      db_ops.delete_data()
    elif __choose_menu == 7:
      db_ops.drop_table()
    elif __choose_menu == 8:
      print("\nEmployee data management program stopped.\n")
      break
    else:
      print ("Invalid Choice")
  except KeyboardInterrupt: # Extra functionality: exit program on Ctrl + C
    print("\n")
    print("Employee data management program stopped.\n")
    break
  except EOFError: # Extra functionality: exit program on Ctrl + D
    print("\n")
    print("Employee data management program stopped.\n")
    break