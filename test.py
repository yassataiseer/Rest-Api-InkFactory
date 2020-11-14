import requests
BASE = "http://127.0.0.1:5000/"
string = "3+Eshal+Taiseer+Samsung+A10S+Android+yyyyyy+Charger+$100+Pending+Cracked Screen+Give discount+Feb+Dec"
#string = string.split("+")
#print(string)
response = requests.get(BASE+"order_builder/"+string)
#response = requests.get(BASE+"/All_orders")


#print(response.json())


