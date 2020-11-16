from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from order_classes import order_writer
from clients_class import client
from employees_classes import employees
conn = sqlite3.connect('orders.db', check_same_thread=False)
c = conn.cursor()
app = Flask(__name__)
api = Api(app)
c = conn.cursor()

""" order.db classes for api """
class Order_builder(Resource):
    def get(self,order_data):
        order_writer.data_entry(order_data)
        return "Done!"

class Order_finder(Resource):
    def get(self,order_number):
        print("number"+order_number)
        a = order_writer.order_finder(order_number)
        return jsonify(a)

class Order_Editor(Resource):
    def get(self,change_data):
        order_writer.update_data(change_data)
        return "DB edited"
class All_orders(Resource):
    def get(self):
        a = order_writer.data_fetcher()
        return jsonify(a)
class Last_order(Resource):
    def get(self):
        a =order_writer.ticket_builder()
        return a  
""" clients.db classes for api """
class Client_data(Resource):
    def get(self):
        a = client.data()
        return jsonify(a)

class Specific_Client_Data(Resource):
    def get(self,name):
        a =  client.client_data(name)
        return jsonify(a)
class Client_Name(Resource):
    def get(self):
        a = client.name_data()
        return jsonify(a)
class Client_Data_Editor(Resource):
    def get(self,new_data):
        new_data = new_data.split("+")
        client.clients_rewrite(new_data[0],new_data[1],new_data[2],new_data[3],new_data[4],new_data[5])
        return "done succesfully"

class Add_client(Resource):
    def get(self,new_creds):
        new_creds = new_creds.split("+")
        print(new_creds[0])
        a = client.data_entry(new_creds[0],new_creds[1],new_creds[2],new_creds[3],new_creds[4],new_creds[5])
        return a
""" employees.db classes for the api"""
class Certain_Worker_data(Resource):
    def get(self,email):
        a = employees.Certain_Employee_Data(email)
        return jsonify(a)
class Edit_Employee(Resource):
    def get(self,new_client_creds):
        new_client_creds=new_client_creds.split("+")
        a = employees.write(new_client_creds[0],new_client_creds[1],new_client_creds[2],new_client_creds[3],new_client_creds[5])
        return "done succesfully!"
class Validate_Employee(Resource):
    def get(self,email_and_password):
        email_and_password = email_and_password.split("+")
        a = employees.validate_user(email_and_password)
        return a

api.add_resource(Order_builder,"/order_builder/<string:order_data>")
api.add_resource(Order_Editor,"/order_editor/<string:change_data>")
api.add_resource(Order_finder,"/Order_finder/<string:order_number>")
api.add_resource(All_orders,"/All_orders")
api.add_resource(Last_order,"/Last_order")
api.add_resource(Client_data,"/Client_data")
api.add_resource(Client_Name,"/Client_Name")
api.add_resource(Specific_Client_Data,"/Specific_Client_Data/<string:name>")
api.add_resource(Client_Data_Editor,"/Client_Data_Editor/<string:new_data>")
api.add_resource(Certain_Worker_data,"/Certain_Worker_data/<string:email>")
api.add_resource(Edit_Employee,"/Edit_Employee/<string:new_client_creds>")
api.add_resource(Validate_Employee,"/Validate_Employee/<string:email_and_password>")
api.add_resource(Add_client,"/Add_client/<string:new_creds>")


if __name__ == "__main__":
	app.run(debug=True)