import requests
BASE = "http://127.0.0.1:5000/"
string = "Taiseer+Mohammed+taiseer142@hotmail.com+56Operahouse+05-Oct-2015+2020-14-11"
#string = string.split("+")
#print(string)
response = requests.get(BASE+"Edit_Employee/"+string)
#response = requests.get(BASE+"/All_orders")


#print(response.json())


