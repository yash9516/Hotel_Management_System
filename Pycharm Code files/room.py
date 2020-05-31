#!C:\Users\epili\AppData\Local\Programs\Python\Python35\python.exe -u

print("Content-Type: text/html")
print()

import cgi, cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
cus_id = form.getvalue('custid')
roomno = form.getvalue('Room_No')
roomtype = form.getvalue('roomtype')
no_of_beds = form.getvalue('no_of_beds')
price = form.getvalue('price')
floor = form.getvalue('floor')
parking = form.getvalue('parking')
balcony = form.getvalue('balcony')
chkin = form.getvalue('startdate')
chkout = form.getvalue('enddate')
duration = form.getvalue('nodays')
print(price)
import pymysql

db = pymysql.connect("localhost","root","Ganga@123","hotel" )

cursor = db.cursor()
sql = "insert into rooms (CustomerID, RoomNo, RoomType, Price, Floor, Parking, Balcony, CheckinDate, CheckoutDate, Beds, Duration) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
cursor.execute(sql,(cus_id, roomno, roomtype, price, floor, parking, balcony, chkin, chkout, no_of_beds, duration))
db.commit()

cursor.execute("SELECT * FROM rooms")
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