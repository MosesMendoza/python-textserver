import sys
from flask import Flask
from flask import request
from handler import Handler

app = Flask(__name__)

handler = Handler()

@app.route("/", methods = ['POST'])
def serve():
  handler.handle(request)


