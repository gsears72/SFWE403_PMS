from controllers.DatabaseController import *
from datetime import datetime

def LoginLog(userID):
    conn = None
   
    sql = """INSERT INTO PMS_LOGS (`EventType`,`Description`) VALUES (%s,%s)"""
    eventType = "Login"
    descrption = "User {} Logged into the system at {}"
    timeStamp = datetime.now()
    descrption = descrption.format(userID,timeStamp)
    values = (eventType,descrption)

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close
        conn.close

    except:
        print("Error recording Log")

    finally:
        del values,sql,conn

def LogoutLog(userID):
    conn = None
   
    sql = """INSERT INTO PMS_LOGS (`EventType`,`Description`) VALUES (%s,%s)"""
    eventType = "Logout"
    descrption = "User {} Logged out of the system at {}"
    timeStamp = datetime.now()
    descrption = descrption.format(userID,timeStamp)
    values = (eventType,descrption)

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close
        conn.close

    except:
        print("Error recording Log")

    finally:
        del values,sql,conn


def TransactionLog(userID,customerID,total):
    conn = None
    sql = """INSERT INTO PMS_LOGS (`EventType`,`Description`,`total`) VALUES (%s,%s,%s)"""
    eventType = "Transaction"
    descrption = "User {} completed a transaction for customer {} for a total of {} at {}"
    timeStamp = datetime.now()
    descrption = descrption.format(userID,customerID,total,timeStamp)
    values = (eventType,descrption,total)

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close
        conn.close

    except:
        print("Error recording Log")

    finally:
        del values,sql,conn

    
def InventoryLog(userID):
    conn = None
   
    sql = """INSERT INTO PMS_LOGS (`EventType`,`Description`) VALUES (%s,%s)"""
    eventType = "Inventory"
    descrption = "User {} modify the inventory at {}"
    timeStamp = datetime.now()
    descrption = descrption.format(userID,timeStamp)
    values = (eventType,descrption)

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close
        conn.close

    except:
        print("Error recording Log")

    finally:
        del values,sql,conn
