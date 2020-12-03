import requests
BASE = "http://127.0.0.1:5000/"
string = "Bill Gates+fake st+None+l9E 1k5+test@gmail.com+1234567890"
#string = string.split("+")
#print(string)
response = requests.get('http://inkfactory.pythonanywhere.com/Validate_Employee/taiseer142@hotmail.com+56Operahouse')
#response = requests.get(BASE+"/All_orders")


print(response.json())
