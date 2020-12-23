# Welcome To The Rest-Api-InkFactory project
## This is a continuation of the "Infactory CRM" and is a Rest-Api that communicates with the DataBases

### Requirements:

##### -In order to install all dependencies see 'requirements.txt' make sure pip is installed.
##### -For Mac and Linux it is 'pip3'. For clone simily use git clone https://github.com/yassataiseer/Rest-Api-InkFactory.git

#### This project was made with the Flask Web Library and Python

### Setup Files:
* flask_app.py: run this file to work with the file
* For customization purposes delete all .db files and use the files in the folder "db_generator" to recreate the databases

### Things open-source members can help with:
* Rewriting Error Handling in certain areas
* Converting certain function's return into json format
* Make smoother user experience
* Fix Bugs
* Make a tester

## How to use:
 ### run "python flask_app.py"
 ### go to 127.0.0.1:5000 to view project

## Api Endpoints:
### 127.0.0.1:5000/order_builder/Order_No+Client+Employee+Product+Brand+Serial_No.+Accesories+Amount+Status+Description+Comments+Add_date+Recent_data --> builds orders into orders.db

### 127.0.0.1:5000/order_editor/New Credentials(same formula as order_builder) --> Edits orders in orders.db

### 127.0.0.1:5000/order_finder/Order_Number --> Takes order number and returns the full order's detail

### 127.0.0.1:5000/All_orders --> Returns all the orders in orders.db

### 127.0.0.1:5000/Last_order --> Returns the last order's number in orders.db this helps make the next ticket number in order 

### 127.0.0.1:5000/Client_data --> Returns all the data from clients.db

### 127.0.0.1:5000/Client_Name --> Returns the names column from clients.db 

### 127.0.0.1:5000/Specific_Client_Data/name --> Returns the data of specific client from clients.db from the given name

### 127.0.0.1:5000/Certain_Worker_data --> Returns the data of specific worker from employees.db

### 127.0.0.1:5000/Edit_Employee/first_name+lastname+Email+password+date -->Rewrites employees.db data for specific employee with given argument

### 127.0.0.1:5000/Validate_Employees/Employee Creds -->Rewrites employees.db data for specific employee with given argument

### 127.0.0.1:5000/Add_client/New Client Creds -->Rewrites employees.db data for specific employee with given argument


## Basic Structure of Databases:
### Clients.db :
* Name
* Address1
* Address2
* Postal Code
* Email
* Phone

### employees.db :
* FirstName
* LastName
* Email
* Password
* Date Added
* Last date updated

### employees.db :
* FirstName
* LastName
* Email
* Password
* Date Added
* Last date updated

##### All endpoints are considered as strings 


###### This project's api can be viewed here @ inkfactory.pythonanywhere.com/<Rest of the credentials>
###### This project was made by Yassa Taiseer for inquiries and question open a pull request or email yassataiseer@gmail.com