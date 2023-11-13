from controllers.DatabaseController import Connect


def Login(userID,Password,Secret):
    conn = None
   
    sql = """SELECT * FROM PMS_Staff WHERE StaffID = %s and password = %s and highschool = %s"""
    values = (userID,Password,Secret)
    results = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        results = cursor.fetchone()
        cursor.close
        conn.close

    except:
        print("Error retriving Login")

    finally:
        del values,sql,conn
        return results
    
def Loginstrike (userID):
    
    conn = None 
    sql = """SELECT * FROM PMS_Staff WHERE StaffID = %s"""
    values = (userID,)
    results = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        results = cursor.fetchone()
        strikecount = results[6]
        if strikecount >=5:
            sql = "UPDATE `PMS_Staff` SET `lockout` = '1' WHERE StaffID = %s"
            cursor.execute(sql,values)
            conn.commit() 
        else:
            strikecount = strikecount+1
            sql = "UPDATE `PMS_Staff` SET `strikecount` = %s WHERE StaffID = %s"
            values = (strikecount,userID)
            cursor.execute(sql,values)
            conn.commit() 
        cursor.close
        conn.close

    except:
       print("Error retriving Login")

    finally:
        del sql,conn,values
        return results
    
    
def Resetstrike (userID):
    
    conn = None
   
    sql = """UPDATE `PMS_Staff` SET `strikecount` = '0' WHERE StaffID = %s"""
    values = (userID,)
    results = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close
        conn.close

    except:
        print("Error retriving Login")

    finally:
        del values,sql,conn
        return results