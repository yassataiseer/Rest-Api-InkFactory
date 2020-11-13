from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
names = {"Yassa":{"Age":15,"Gender":"Male"},
"Tim":{"Age":19,"Gender":"Male"}}
class HelloWorld(Resource):
    def get(self,name):
        return names[name]

api.add_resource(HelloWorld,"/helloworld/<string:name>")
 

if __name__ == "__main__":
	app.run(debug=True)
    