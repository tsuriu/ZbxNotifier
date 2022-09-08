from flask import Blueprint
from flask import current_app as app
from flask_restful import Api, reqparse

from .resources.internal import rabbitmqResource


# Blueprint Configuration
api_bp = Blueprint("api_bp", __name__)
api = Api(api_bp)

api.add_resource(rabbitmqResource, '/broker')