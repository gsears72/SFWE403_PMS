from controllers.DatabaseController import Connect
from datetime import datetime

# Function to log user login events
def LoginLog(userID):
    conn = None
   
    # SQL query to insert log into the PMS_LOGS table
    sql = """INSERT INTO PMS_LOGS (`EventType`,`Description`) VALUES (%s,%s)"""

    # Setting the event type to "Login"
    eventType = "Login"

    # Creating the log description with the user ID and timestamp
    descrption = "User {} Logged into the system at {}"
    timeStamp = datetime.now()
    descrption = descrption.format(userID,timeStamp)

    # Creating a tuple of values to be inserted into the database
    values = (eventType,descrption)

    # Establishing a database connection, creates a cursor, executes the SQL query with the provided values
    # committs the changes to the database, then closes the cursor, and database connection
    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close
        conn.close

    #Error handing
    except:
        print("Error recording Log")

    #Cleans up left over resources 
    finally:
        del values,sql,conn,eventType,descrption,timeStamp


# Function to log user logout events
def LogoutLog(userID):
    conn = None
   
   # SQL query to insert log into the PMS_LOGS table
    sql = """INSERT INTO PMS_LOGS (`EventType`,`Description`) VALUES (%s,%s)"""

    # Setting the event type to "Logout"
    eventType = "Logout"

    # Creating the log description with the user ID and timestamp
    descrption = "User {} Logged out of the system at {}"
    timeStamp = datetime.now()
    descrption = descrption.format(userID,timeStamp)

    # Creating a tuple of values to be inserted into the database
    values = (eventType,descrption)

    # Establishing a database connection, creates a cursor, executes the SQL query with the provided values
    # committs the changes to the database, then closes the cursor, and database connection
    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close
        conn.close

    #Error handing
    except:
        print("Error recording Log")

    #Cleans up left over resources 
    finally:
        del values,sql,conn,eventType,descrption,timeStamp


# Function to log transaction events
def TransactionLog(userID, total):
    try:
        conn = None

        # SQL query to insert log into the PMS_LOGS table
        sql = """INSERT INTO PMS_LOGS (`EventType`,`Description`,`total`) VALUES (%s,%s,%s)"""

        # Setting the event type to "Transaction"
        eventType = "Transaction"

        # Creating the log description with the user ID, customer ID, total, and timestamp
        descrption = "User {} completed a transaction for a total of {} at {}"
        timeStamp = datetime.now()
        descrption = descrption.format(userID,total,timeStamp)

        # Creating a tuple of values to be inserted into the database
        values = (eventType,descrption,total)

        # Establishing a database connection, creates a cursor, executes the SQL query with the provided values
        # committs the changes to the database, then closes the cursor, and database connection
        
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close
        conn.close

    #Error handing
    except:
        print("Error recording Log")

    #Cleans up left over resources 
    finally:
        del values,sql,conn,eventType,descrption,timeStamp


# Function to log user modification to inventory events    
def InventoryLog(userID):
    conn = None
   
    # SQL query to insert log into the PMS_LOGS table
    sql = """INSERT INTO PMS_LOGS (`EventType`,`Description`) VALUES (%s,%s)"""

    # Setting the event type to "Inventory"
    eventType = "Inventory"

    # Creating the log description with the user ID and timestamp
    descrption = "User {} modify the inventory at {}"
    timeStamp = datetime.now()
    descrption = descrption.format(userID,timeStamp)

    # Creating a tuple of values to be inserted into the database
    values = (eventType,descrption)

    # Establishing a database connection, creates a cursor, executes the SQL query with the provided values
    # committs the changes to the database, then closes the cursor, and database connection
    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close
        conn.close

    #Error handing
    except:
        print("Error recording Log")

    #Cleans up left over resources 
    finally:
        del values,sql,conn,eventType,descrption,timeStamp


# Function to log prescription fill events
def PrescriptionFilledLog(userID,prescription_id):
    conn = None
   
    # SQL query to insert log into the PMS_LOGS table
    sql = """INSERT INTO PMS_LOGS (`EventType`,`Description`) VALUES (%s,%s)"""

    # Setting the event type to "Prescription"
    eventType = "Prescription"

    # Creating the log description with the user ID, prescription ID, and timestamp
    descrption = "User {} filled prescription {} at {}"
    timeStamp = datetime.now()
    descrption = descrption.format(userID,prescription_id,timeStamp)

    # Creating a tuple of values to be inserted into the database
    values = (eventType,descrption)

    # Establishing a database connection, creates a cursor, executes the SQL query with the provided values
    # committs the changes to the database, then closes the cursor, and database connection
    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close
        conn.close
    
    #Error handing
    except:
        print("Error recording Log")

    #Cleans up left over resources 
    finally:
        del values,sql,conn,eventType,descrption,timeStamp


# Function to log prescription picked up events
def PrescriptionPickedUpLog(userID,prescription_id,customer_id):
    conn = None
   
    # SQL query to insert log into the PMS_LOGS table
    sql = """INSERT INTO PMS_LOGS (`EventType`,`Description`) VALUES (%s,%s)"""

    # Setting the event type to "Prescription"
    eventType = "Prescription"

    # Creating the log description with the user ID, prescription ID, and timestamp
    descrption = "Customer {} picked up prescription {} from user {} at {}"
    timeStamp = datetime.now()
    descrption = descrption.format(customer_id,prescription_id,userID,timeStamp)

    # Creating a tuple of values to be inserted into the database
    values = (eventType,descrption)

    # Establishing a database connection, creates a cursor, executes the SQL query with the provided values
    # committs the changes to the database, then closes the cursor, and database connection
    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close
        conn.close
    
    #Error handing
    except:
        print("Error recording Log")

    #Cleans up left over resources 
    finally:
        del values,sql,conn,eventType,descrption,timeStamp
