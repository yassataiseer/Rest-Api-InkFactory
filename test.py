import requests
BASE = "http://127.0.0.1:5000/"
string = "2+Yassa+Taiseer+Iphone+X Max+Apple+yyyyyy+Charger+$100+Pending+Cracked Screen+Give discount+Feb+Dec"
#string = string.split("+")
#print(string)
#response = requests.get(BASE+"order_editor/"+string)
response = requests.get(BASE+"/All_orders")


print(response.json())


