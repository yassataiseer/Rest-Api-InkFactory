import requests
BASE = "http://127.0.0.1:5000/"
string = "Syed Atuer Ali+6895 Apex Ct+Missisauga+75N 7H8+WORKS@HOTMAIL.COM+123 456 7890"
#string = string.split("+")
#print(string)
response = requests.get(BASE+"Client_Data_Editor/"+string)
#response = requests.get(BASE+"/All_orders")


#print(response.json())


