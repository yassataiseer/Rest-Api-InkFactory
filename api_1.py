from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import sqlite3

from order_classes import order_writer
conn = sqlite3.connect('orders.db', check_same_thread=False)
c = conn.cursor()
app = Flask(__name__)
api = Api(app)
c = conn.cursor()
class Order_builder(Resource):
    def get(self,order_data):
        order_writer.data_entry(order_data)
        return "yay"

class Order_finder(Resource):
    def get(self,order_number):
        print("number"+order_number)
        a = order_writer.order_finder(order_number)
        return jsonify(a)

class Order_Editor(Resource):
    def get(self,change_data):
        order_writer.update_data(change_data)
        return "DB edited"


api.add_resource(Order_builder,"/order_builder/<string:order_data>")
api.add_resource(Order_Editor,"/order_editor/<string:change_data>")
api.add_resource(Order_finder,"/Order_finder/<string:order_number>")

print("yay")
if __name__ == "__main__":
	app.run(debug=True)