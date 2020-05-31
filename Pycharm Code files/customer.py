#!C:\Users\epili\AppData\Local\Programs\Python\Python35\python.exe -u

print("Content-Type: text/html")
print()

import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
fname = form.getvalue('name')
age = form.getvalue('age')
idtype = form.getvalue('idtype')
idno= form.getvalue('idnumber')
email = form.getvalue('email')
phone = form.getvalue('phone')

import pymysql

db = pymysql.connect("localhost","root","Ganga@123","hotel" )

cursor = db.cursor()
# sql = "insert into customers (firstname, lastname, CustomerID, age, email, phone) VALUES (%s, %s,%s, %s,%s, %s);"
sql = "insert into customers (CustomerName, Age, IDType,IDNumber, Email, Phone) VALUES (%s, %s, %s, %s,%s, %s)"
cursor.execute(sql,(fname,age,idtype,idno,email,phone))
db.commit()

cursor.execute("SELECT * FROM customers;")
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