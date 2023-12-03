from controllers.DatabaseController import Connect
from datetime import *

def SalesReport(startDate, endDate):
    conn = None
    sql = """SELECT * FROM `PMS_LOGS` WHERE EventType = "Transaction" and TimeStamp BETWEEN CAST(%s AS DATE) and CAST(%s AS DATE)"""
    values = (startDate,endDate)
    results = None
    total = 0
    timeStamp = 0
    description =" "
    xtotal = 0
    print(sql)

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        results = cursor.fetchall()
        cursor.close
        conn.close
        FileName = "Sales Report %s.txt" % date.today()
        print(FileName)
        reportfile = open(FileName,"a")
        for x in results:
            #reportfile.write(results[x]+"\n")
            timeStamp = x[1]
            description = x[3]
            xtotal = x[4]
            toWrite = str(timeStamp)+"   "+str(description)+" "+str(xtotal)
            reportfile.write(toWrite)
            total = total+x[4]
        reportfile.write("\n")
        reportfile.write("Total Sales: "+str(total))
        reportfile.close()


    except:
        print("Error Generating Sales Report")
        return 1

    finally:
        del sql,conn
        return 0
    
if __name__ == "__main__":
   SalesReport("2023-11-16","2023-11-19")  