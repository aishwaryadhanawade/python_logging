from flask import Blueprint, current_app
from flask_restful import Resource, Api
from project import app


logg = Blueprint('logg', __name__)
reg_api = Api(logg)




class Hello(Resource):
    def get(self):
        current_app.logger.info("From Api Logger....")

        print(p)
        return "Hello"


reg_api.add_resource(Hello, '/')
