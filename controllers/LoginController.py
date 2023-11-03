from controllers.DatabaseController import Connect


def Login(userID,Password):
    conn = None
   
    sql = """SELECT * FROM PMS_Staff WHERE StaffID = %s and password = %s"""
    values = (userID,Password)
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
    