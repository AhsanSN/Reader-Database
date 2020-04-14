
# Python code to demonstrate table creation and  
# insertions with SQL 
  
# importing module 
import sqlite3 
  
# connecting to the database  
connection = sqlite3.connect("myTable.db") 
  
# cursor  
crsr = connection.cursor() 

    
def create_initial_database(crsr):
    sql_command = """
    CREATE TABLE T_Registered
    (
    Registered_ID number not null PRIMARY KEY,
    Registered_gender VARCHAR2 (6),
    Registered_dateOfBirth Date,
    Registered_Location VARCHAR2(60)
    );
    """
    crsr.execute(sql_command)



    sql_command = """
    CREATE TABLE T_Registered_AreaOfInterest(
    Registered_ID REFERENCES T_Registered(Registered_ID),
    SingleRegArea VARCHAR2(40),
    CONSTRAINT reg_area_PK PRIMARY KEY(Registered_ID, SingleRegArea)
    );
    """
    crsr.execute(sql_command)

    sql_command = """
    CREATE TABLE T_Registered_Address(
    Registered_ID REFERENCES T_Registered(Registered_ID),
    street VARCHAR2(35),
    PostalCode number,
    City VARCHAR2(50),
    CONSTRAINT reg_address_pk PRIMARY KEY(Registered_ID)
    );
    """
    crsr.execute(sql_command)


    sql_command = """
    CREATE TABLE T_Manager(
    Manager_ID number not null PRIMARY KEY,
    report_date DATE
    );

    """
    crsr.execute(sql_command)

    sql_command = """
    CREATE TABLE T_Return(
    Registered_ID REFERENCES T_Registered(Registered_id),
    Manager_ID REFERENCES T_Manager(Manager_ID),
    Order_ID number not null,
    CONSTRAINT return_pk PRIMARY KEY(Registered_ID, Manager_ID)
    );

    """
    crsr.execute(sql_command)


    sql_command = """
    CREATE TABLE T_Book(
    Book_ID number not null PRIMARY KEY,
    BookTitle VARCHAR2(50),
    authorName VARCHAR2(50),
    Book_Price number,
    Book_ISBN_Book_edition VARCHAR2(80)
    );

    """
    crsr.execute(sql_command)



    sql_command = """
    CREATE TABLE T_Book_AreaOfIntrest(
    Book_ID REFERENCES T_Book(Book_ID),
    SingleBookArea VARCHAR2(40),
    CONSTRAINT book_areaOfInterest_pk PRIMARY KEY(Book_ID, SingleBookArea)
    );
    """
    crsr.execute(sql_command)


    sql_command = """
    CREATE TABLE T_DeliveryBook(
    Manager_ID REFERENCES T_Manager(Manager_ID),
    Book_ID REFERENCES T_Book(BOOK_ID),
    DeliveryDate DATE,
    OrderNumber number,
    CONSTRAINT deliveryBook_pk PRIMARY KEY(Manager_ID, Book_ID)
    );

    """
    crsr.execute(sql_command)

    sql_command = """
    CREATE TABLE T_Payment(
    Registered_ID REFERENCES T_Registered(Registered_ID),
    Book_ID REFERENCES T_Book(Book_ID),
    CreditCardNumber number,
    ExpiryDate DATE,
    TypeOfCreditCard VARCHAR2(15),
    StateVerify VARCHAR2(15),
    CONSTRAINT payment_pk PRIMARY KEY(Registered_ID, Book_ID)
    );


    """
    crsr.execute(sql_command)


#create_initial_database(crsr)

    
''' 
  
# SQL command to insert the data in the table 
sql_command = """INSERT INTO emp VALUES (23, "Rishabh", "Bansal", "M", "2014-03-28");"""
crsr.execute(sql_command) 
  
# another SQL command to insert the data in the table 
sql_command = """INSERT INTO emp VALUES (1, "Bill", "Gates", "M", "1980-10-28");"""
crsr.execute(sql_command) 
'''
def register_user(crsr):
    unq_id = str(input("Unique Id? ")) #eg 3
    
    gender = str(input("Gender? ")) #eg Male
    dob = str(input("Date of Birth? ")) #eg 25-09-2020
    location = str(input("location? ")) #eg Karachi

    
    sql_command = "INSERT INTO T_Registered(Registered_ID, Registered_gender, Registered_dateOfBirth, Registered_Location) VALUES ('"+unq_id+"', '"+gender+"', '"+dob+"', '"+location+"');"
    #sql_command = "INSERT INTO T_Registered VALUES ("+unq_id+","+gender+","+dob+","+location+");"
    crsr.execute(sql_command)


    crsr.execute("SELECT * FROM T_Registered")  
    ans = crsr.fetchall()  
    print("Registered Users:", ans) 

    
    

    interest = str(input("Area of Interest? "))
    sql_command = "INSERT INTO T_Registered_AreaOfInterest VALUES ('"+unq_id+"', '"+interest+"');"
    crsr.execute(sql_command)
    
    
    street = str(input("Street? "))
    postal = str(input("Postal? "))
    city = str(input("City? ")) 
    sql_command = "INSERT INTO T_Registered_Address VALUES ('"+unq_id+"', '"+street+"' , '"+postal+"' , '"+city+"');"
    crsr.execute(sql_command)

    print("User Registered")


    
#main
def main(crsr):
    register_user(crsr)



    
main(crsr)
# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
connection.commit() 
  
# close the connection 
connection.close() 
