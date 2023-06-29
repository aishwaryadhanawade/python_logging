from flask import Flask,has_request_context,request
from flask_restful import Api
import logging
from logging.handlers import RotatingFileHandler

app= Flask(__name__)

api = Api(app)

logger = logging.getLogger()


class NewFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote = request.remote_addr
        else:
            record.url = None
            record.remote = None
        return super().format(record)


logformat = NewFormatter('%(asctime)s-%(url)s-%(remote)s-%(levelname)s-%(message)s', datefmt="%Y-%m-%d %H:%M:%S")

consoleHandler=logging.StreamHandler()
consoleHandler.setFormatter(logformat)
logger.addHandler(consoleHandler)

fileHandler = RotatingFileHandler("log.log", backupCount=100, maxBytes=1024)
logger.addHandler(fileHandler)