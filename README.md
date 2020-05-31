# Hotel-Management-System-

Statement: 
We are creating a Customer Management System for Hotel Le Meridien.

Description:
The customer management system of Hotel uses the HTML forms to collect the customer information, MySQL database to store the information and Python programming to connect data from HTML forms to the database. It will act as a middleware to return the result value as well. 

Assumptions:

Please find the assumptions we have taken into account while creating our management system.
1) There will be 2 types of customers who will be coming to the Hotel i.e. 
•	The individual customers, who would be residing in the hotel alone and they have an entry in the main Customer table with Customer ID.
•	Customers who coming with family or in groups, for them there will be one primary customer whose information will be recorded in the Customer table and a CustomerID will be generated for them. 
And the rest of the members will be registered into the Dependents table related to main table with the Customer ID. These customer will take part in Room and Event but will not be allocated a Customer Id as they will be dependent once for main customer. 

2)  Only the primary customer is responsible for the 
•	Event booking, 
•	Room bookings
•	Payments. 
Hence all the tables are related to each other using the Customer ID.

3) In Customer table Customer ID is the primary key with auto increment starting from One. 

4) Room table has all the details about the room and will generate a booking id which is unique key auto incrementing from 10000 value. In this table Checking date and Room No is composite primary key enabling a constraint where no two primary customer can book one room at a time.

5) Event table has event room and start date as composite key enabling a constraint where no 2 primary customers can book 1 event at a time.

Added Constraints :- 
1) After booking if Any customer does not shows up then all entries related to this customer will be deleted. 

2) Total Room amount would be calculated as number of days stayed by the customer multiplied by the individual room amount 
