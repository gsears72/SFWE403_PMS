import mysql.connector
from datetime import date
from datetime import timedelta
from datetime import datetime

mydb = mysql.connector.connect(
        host = 'mysql-145311-0.cloudclusters.net',
        port = '18166',
        user = 'admin',
        passwd = 'FcCZds4d',
        db = 'PMS'
    )

mycursor = mydb.cursor()


def Expired30Day():
    #get todays date
    today = date.today()

    #notify expiration 30 days out
    t = timedelta(days= 30)

    #what is the notification cutoff date
    notifyDate = today + t
    
    #find all medication not expired yet but expiring in the next 30 days 
    mycursor.execute("SELECT * FROM Inventory WHERE expDate BETWEEN CAST(%s AS DATE) and CAST(%s AS DATE)", (today,notifyDate))
                      
    expiring_meds = mycursor.fetchall()

    # Initialize an empty list to store the formatted strings
    return_exp_meds = []

    for x in expiring_meds:
        # Format the string for each element in the list and append to the list
        formatted_string = "ID: %d, Name: %s, Strength: %s, Batch: %s \n" % (x[0], x[1], x[3], x[4])
        return_exp_meds.append(formatted_string)

    # Join the formatted strings into a single string
    result_string = ''.join(return_exp_meds)

    return result_string

def Expired():
    today = date.today()

    #need a second parameter for select in order for the execute statement to work, item_id will always be > 0 
    idHelper = 0

    mycursor.execute("SELECT * FROM Inventory WHERE expDate <= %s and item_id > %s", (today, idHelper))
    expired_meds = mycursor.fetchall()

    return_exp_meds = []

    for x in expired_meds:
        # Format the string for each element in the list and append to the list
        formatted_string = "ID: %d, Name: %s, Strength: %s, Batch: %s \n" % (x[0], x[1], x[3], x[4])
        return_exp_meds.append(formatted_string)

    # Join the formatted strings into a single string
    result_string = ''.join(return_exp_meds)

    return result_string


if __name__ == '__main__':

   # notifyDate = Expired30Day()
   # print(notifyDate.strftime("%B/%d/%Y")) // for testing if correct date is being returned 
   #getting all entries for easy check to see if functions are missing entries that should be returned
    mycursor.execute("SELECT * FROM Inventory")
    for x in mycursor:
        print(x)

    expiring = Expired30Day()

    print("WARNING: The following medications expire within the NEXT 30 DAYS \n")
    print(expiring)

    expired = Expired()

    print("WARNING: The following medications are EXPIRED. Do NOT use and DISPOSE IMMEDIATELY")
    print(expired)