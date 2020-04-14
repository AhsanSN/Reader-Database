
# Python code to demonstrate table creation and  
# insertions with SQL 
  
# importing module 
import sqlite3 
  
# connecting to the database  
connection = sqlite3.connect("myDatabase.db") 
  
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

    
def register_user(crsr, Registered_ID, gender, dob, interest, location, street, postal, city):
    sql_command = "INSERT INTO T_Registered(Registered_ID, Registered_gender, Registered_dateOfBirth, Registered_Location) VALUES ('"+Registered_ID+"', '"+gender+"', '"+dob+"', '"+location+"');"
    crsr.execute(sql_command)
    sql_command = "INSERT INTO T_Registered_AreaOfInterest VALUES ('"+Registered_ID+"', '"+interest+"');"
    crsr.execute(sql_command)
    sql_command = "INSERT INTO T_Registered_Address VALUES ('"+Registered_ID+"', '"+street+"' , '"+postal+"' , '"+city+"');"
    crsr.execute(sql_command)
    return True


def remove_register_user(crsr, Registered_ID):
    sql_command = "Delete from T_Registered where Registered_ID='"+str(Registered_ID)+"'"
    crsr.execute(sql_command)

    return True

def updateInfo(crsr, Registered_ID, gender, dob, address, interest, location):
    sql_command = "UPDATE T_Registered set Registered_gender='"+str(gender)+"', Registered_dateOfBirth ='"+str(dob)+"' , Registered_Location ='"+str(location)+"' where Registered_ID='"+str(Registered_ID)+"'"
    crsr.execute(sql_command)

    sql_command = "UPDATE T_Registered_AreaOfInterest set SingleRegArea='"+str(interest)+"' where Registered_ID='"+str(Registered_ID)+"'"
    crsr.execute(sql_command)

def addBook(crsr, Book_ID, BookTitle, authorName, Book_Price, Book_ISBN_Book_edition):
    sql_command = "INSERT INTO T_Book VALUES ('"+str(Book_ID)+"', '"+BookTitle+"', '"+authorName+"', '"+str(Book_Price)+"', '"+Book_ISBN_Book_edition+"');"
    crsr.execute(sql_command)

def removeBook(crsr, Book_ID):
    sql_command = "DELETE from T_Book where Book_ID='"+str(Book_ID)+"'"
    crsr.execute(sql_command)

def searchBook(crsr, authName, title, editor, ISBN, areaIfInterest):
    crsr.execute("SELECT * FROM T_Book b outer left join T_Book_AreaOfIntrest a on b.Book_ID=a.Book_ID where ( authorName='"+authName+"' OR  BookTitle='"+title+"' OR  Book_ISBN_Book_edition='"+ISBN+"' OR  a.SingleBookArea='"+areaIfInterest+"')")  
    ans = crsr.fetchall()  
    return(ans)

def generateReport(crsr, Manager_ID, report_date):
    sql_command = "INSERT INTO T_Manager values ('"+str(Manager_ID)+"', '"+str(report_date)+"')"
    crsr.execute(sql_command)

def orderBooks(crsr, Registered_ID, Book_ID, CreditCardNumber, ExpiryDate, TypeOfCreditCard, StateVerify):
    sql_command = "INSERT INTO T_Payment values ('"+str(Registered_ID)+"', '"+str(Book_ID)+"', '"+str(CreditCardNumber)+"', '"+str(ExpiryDate)+"', '"+str(TypeOfCreditCard)+"', '"+str(StateVerify)+"')"
    crsr.execute(sql_command)

def deliverBooks(crsr, Manager_ID, Book_ID, DeliveryDate, OrderNumber, location):
    sql_command = "INSERT INTO T_DeliveryBook values ('"+str(Manager_ID)+"', '"+str(Book_ID)+"', '"+str(DeliveryDate)+"', '"+str(OrderNumber)+"')"
    crsr.execute(sql_command)

def returnBook(crsr, Registered_ID, Manager_ID, Order_ID):
    sql_command = "INSERT INTO T_Return values ('"+str(Registered_ID)+"', '"+str(Manager_ID)+"', '"+str(Order_ID)+"')"
    crsr.execute(sql_command)
    
#prompt functions
def p_register_user(crsr):
    Registered_ID = str(input("Registered_ID? "))
    gender = str(input("gender? "))
    dob = str(input("dob? "))
    interest = str(input("interest? "))
    location = str(input("location? "))
    street = str(input("street? "))
    postal = str(input("postal? "))
    city = str(input("city? "))

    try:
        register_user(crsr, Registered_ID, gender, dob, interest, location, street, postal, city)
    except:
        print ("Err occurred.")

def p_remove_register_user(crsr):
    Registered_ID = str(input("User Registered_ID? "))
    try:
        remove_register_user(crsr, Registered_ID)
    except:
        print ("Err occurred.")

def p_updateInfo(crsr):
    Registered_ID = str(input("Registered_ID? "))
    gender = str(input("gender? "))
    dob = str(input("dob? "))
    interest = str(input("interest? "))
    location = str(input("location? "))
    try:
        updateInfo(crsr, Registered_ID, gender, dob, address, interest, location)
    except:
        print ("Err occurred.")

def p_addBook(crsr):
    Book_ID = str(input("Book_ID? "))
    BookTitle = str(input("BookTitle? "))
    authorName = str(input("authorName? "))
    Book_Price = str(input("Book_Price? "))
    Book_ISBN_Book_edition = str(input("Book_ISBN_Book_edition? "))
    try:
        addBook(crsr, Book_ID, BookTitle, authorName, Book_Price, Book_ISBN_Book_edition)
    except:
        print("Err occurred.")    

def p_removeBook(crsr):
    Book_ID = str(input("Book_ID? "))
    try:
        removeBook(crsr, Book_ID)
    except:
        print("Err occurred.")

def p_searchBook(crsr):
    authName = str(input("authName? "))
    title = str(input("title? "))
    editor = str(input("editor? "))
    ISBN = str(input("ISBN? "))
    areaIfInterest = str(input("areaIfInterest? "))
    try:
        searchBook(crsr, authName, title, editor, ISBN, areaIfInterest)
    except:
        print("Err occurred.")

def generateReport(crsr):
    Manager_ID = str(input("Manager_ID? "))
    report_date = str(input("report_date? "))
    try:
        generateReport(crsr, Manager_ID, report_date)
    except:
        print("Err occurred.")

def p_orderBooks(crsr):
    Registered_ID = str(input("Registered_ID? "))
    Book_ID = str(input("Book_ID? "))
    CreditCardNumber = str(input("CreditCardNumber? "))
    ExpiryDate = str(input("ExpiryDate? "))
    TypeOfCreditCard = str(input("TypeOfCreditCard? "))
    StateVerify = str(input("StateVerify? "))
    try:
        orderBooks(crsr, Registered_ID, Book_ID, CreditCardNumber, ExpiryDate, TypeOfCreditCard, StateVerify)
    except:
        print("Err occurred.")


def p_deliverBooks(crsr):
    Manager_ID = str(input("Manager_ID? "))
    Book_ID = str(input("Book_ID? "))
    DeliveryDate = str(input("DeliveryDate? "))
    OrderNumber = str(input("OrderNumber? "))
    location = str(input("location? "))
    try:
        deliverBooks(crsr, Manager_ID, Book_ID, DeliveryDate, OrderNumber, location)
    except:
        print("Err occurred.")

def p_returnBook(crsr):
    Registered_ID = str(input("Registered_ID? "))
    Manager_ID = str(input("Manager_ID? "))
    Order_ID = str(input("Order_ID? "))
    try:
        returnBook(crsr, Registered_ID, Manager_ID, Order_ID)
    except:
        print("Err occurred.")

        
#main
def main(crsr):
    print("""
        --------------READER SOFTWARE--------------
        Press the folliwing keys for operation.

        (1)  > Register User
        (2)  > Remove User
        (3)  > Update User Info
        (4)  > Add Book
        (5)  > Remove Book
        (6)  > Search Book
        (7)  > Generate Report
        (8)  > Order Book
        (9)  > Deliver Books
        (0)  > Return Books
        (d)  > Initialize Database
        (-1) > Quit
         ------------------------------------------
    """
          )
    inp = str(input("Enter Command: "))
    if(inp=="1"):
        p_register_user(crsr)
    elif(inp=="2"):
        p_remove_register_user(crsr)
    elif(inp=="3"):
        p_updateInfo(crsr)
    elif(inp=="4"):
        p_addBook(crsr)
    elif(inp=="5"):
        p_removeBook(crsr)
    elif(inp=="6"):
        p_searchBook(crsr)
    elif(inp=="7"):
        p_generateReport(crsr)
    elif(inp=="8"):
        p_orderBooks(crsr)
    elif(inp=="9"):
        p_deliverBooks(crsr)
    elif(inp=="0"):
        p_returnBook(crsr)        
    elif(inp=="d"):
        create_initial_database(crsr)
    elif(inp=="-1"):
        quit()
    main(crsr)
        

    
    #create_initial_database(crsr) #run once
    #remove_register_user(crsr, 1)
    #updateInfo(3, "Female", "21-5-1749", "Lahore", "Fishing", "Lahore")
    #addBook(crsr, 1, "Hello World", "Osama", 24, "AD2dAd1")
    #removeBook(crsr, 0)
    #print(searchBook(crsr, "Osama", "Seawater", "edit27", "21767dAs387", "Jumping"))
    #generateReport(crsr, 1, "12-9-2012")
    #orderBooks(crsr, 3, 1, "123123213", "24-7-2020", "Current", "y")
    #deliverBooks(crsr, 1, 1, "12-9-2019", 42, "Karachi")
    #returnBook(crsr, 1, 1, 1)
    
main(crsr)
# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
connection.commit() 
  
# close the connection 
connection.close()

'''
README:

There was no name column for registered users in database, hence i am using registered_id instead of name.
there was no address in database
add book function in uml had no paramaters
no editor in database
There are some functionalities in the system diagram for which there is no function in the UML.
verifycreditcard(): what does this function verifies against if there are is table for storing credit cards before a payment is completed.
how do you verify postalServices? there is no table in database for that
what's order number? shouldnt it have a seperate table on its own where orderNumber is primary key? There is no way to get registered_ID of user from an orderID as there is no relation.
deliverBooks table has no location in the database. so how is the record kept that where a book goes?
'''
