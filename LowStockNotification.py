import mysql.connector
import numpy as np

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
    mycursor.execute("SELECT * FROM Inventory")
    allStock = mycursor.fetchall()


    stockArray = []
    i = 0
    for x in allStock:
        stockArray.append(x)
    stockArray = np.array(stockArray)

    stockNameArray = []
    i = 0
    for x in stockArray:
        stockNameArray.append(stockArray[i][1]) #name array
        i+=1
    stockNameArray = np.array(stockNameArray)

    stockStrengthArray = []
    i = 0
    for x in stockArray:
        stockStrengthArray.append(stockArray[i][3]) #strength array
        i+=1
    stockStrengthArray = np.array(stockStrengthArray)

    #combines name array and strength array into single 2d array
    stockNameStrengthArray = np.vstack((stockNameArray, stockStrengthArray)).T

    count = []
    for x in range(len(stockArray)):
        count.append(0)
    count = np.array(count)

    #combines name array and strength array into single 2d array
    stockNameStrengthArray = np.vstack((stockNameArray, stockStrengthArray, count)).T
    #stockNameStrengthArray = np.vstack((stockNameArray, stockStrengthArray)).T

    #stockNameStrengthArray format: [name, strength, counted(0 no, 1 yes)]
    print(stockNameStrengthArray)


    #in counted, we have name, strength, count #. when checking duplicates, we set count to 1 so that we only add 1 to count number if we
    #approach a new prescription (0)
    stockLength = len(stockNameStrengthArray)
    counted = []
    for i in range(stockLength):
        temp = 0
        k = i + 1
        for j in range(k, stockLength): #MIGHT BE STOCKLENGTH -1
            if ((stockNameStrengthArray[i][2] == '0') and
                (stockNameStrengthArray[i][0] == stockNameStrengthArray[j][0]) and 
                    (stockNameStrengthArray[i][1] == stockNameStrengthArray[j][1])):
                temp += 1
                stockNameStrengthArray[j][2] = int(stockNameStrengthArray[i][2]) + 1 #so that we do not add it later on.
                
        if (stockNameStrengthArray[i][2] == '0'):
            stockNameStrengthArray[i][2] = int(stockNameStrengthArray[i][2]) + 1 + temp
            counted.append(stockNameStrengthArray[i])

    counted = np.array(counted)

    print(counted , "hi")


    print("WARNING: The following medications are low in stock:")

    for i in range(len(counted)):
        #low in stock if value less than 5
        if (int(counted[i][2]) < 5):
            print(counted[i][0], counted[i][1], "-",  int(counted[i][2]), "remaining")


    #return all medications with quantity 1 through 5
    #return all_low_stock


if __name__ == '__main__':


    mycursor.execute("SELECT * FROM Inventory")
    for x in mycursor:
        print(x)

    lowStock = LowStock()
