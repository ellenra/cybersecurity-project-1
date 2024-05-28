from os import getenv
from flask import Flask
import logging

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

''' Flaw 4: Not logging website activity '''
''' Fix 4:
logging.basicConfig(filename='record.log', level=logging.DEBUG) '''

import routes
