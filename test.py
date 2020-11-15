import requests
BASE = "http://127.0.0.1:5000/"
string = "adil@theinkfactory.ca+1234567890"
#string = string.split("+")
#print(string)
response = requests.get(BASE+"Validate_Employee/"+string)
#response = requests.get(BASE+"/All_orders")


#print(response.json())


