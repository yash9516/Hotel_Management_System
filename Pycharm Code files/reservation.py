#!C:\Users\epili\AppData\Local\Programs\Python\Python35\python.exe -u

print("Content-Type: text/html")
print()

import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
cust_id = form.getvalue('custid')
booking_id = form.getvalue('bookid')
totamt = form.getvalue('totamt')
paymethod = form.getvalue('paymethod')

import pymysql;
# Open connection to the database

db = pymysql.connect("localhost","root","Ganga@123","hotel" );
# Start a cursor object using cursor() method
cursor = db.cursor()

# Execute a SQL query using execute() method. This should return all the columns of heroes that use swords.
sql = "Insert into reservations (CustomerID, BookingID, Amount, Payment_Type) VALUES (%s,%s,%s,%s);"

cursor.execute(sql,(cust_id,booking_id,totamt,paymethod))
db.commit()

cursor.execute("SELECT * FROM reservations")
data = cursor.fetchall()

#print (data)
#clm=('firstname', 'lastname', 'CustomerID', 'age', 'email', 'phone')

#data1=np.array(data)
#num_fields = len(data)
field_names = [i[0] for i in cursor.description]

print("<style>table { font-family: arial, sans-serif; border-collapse: collapse; width: 100%; } td, th { border: 1px solid #dddddd; text-align: left; padding: 8px; } tr:nth-child(even) { background-color: #dddddd; } </style>")
print("<table><tr>")

for columns in field_names:
    print("<th>",columns,"</th>")
print ("</tr>")

for rows in data:
    print ("<tr>");
    for subrows in rows:
        print("<td>",subrows,"</td>")
    print ("</tr>")
print("</table>")
# Fetch all the rows using fetchall() method.

db.commit()