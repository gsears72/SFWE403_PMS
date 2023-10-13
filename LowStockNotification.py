import mysql.connector

mydb = mysql.connector.connect(
        host = 'mysql-145311-0.cloudclusters.net',
        port = '18166',
        user = 'admin',
        passwd = 'FcCZds4d',
        db = 'PMS'
    )

mycursor = mydb.cursor()


def LowStock():
    
    #find all medication where quantity is 10 or less, not 0.
    mycursor.execute("SELECT * FROM Inventory WHERE quantity <= 10 and quantity > 0")
    all_low_stock = mycursor.fetchall()

    #return all medications with quantity 1 through 5
    return all_low_stock

def OutOfStock():

    #find all medication where quantity is 0.
    mycursor.execute("SELECT * FROM Inventory WHERE quantity = 0")
    all_out_of_stock = mycursor.fetchall()

    return all_out_of_stock


if __name__ == '__main__':

   # notifyDate = Expired30Day()
   # print(notifyDate.strftime("%B/%d/%Y")) // for testing if correct date is being returned 
   #getting all entries for easy check to see if functions are missing entries that should be returned
    mycursor.execute("SELECT * FROM Inventory")
    for x in mycursor:
        print(x)

    lowStock = LowStock()

    print("WARNING: The following medications are low in stock (5 or less) \n")
    print(lowStock)

    outOfStock = OutOfStock()

    print("WARNING: The following medications out of stock")
    print(outOfStock)