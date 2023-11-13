# this file needed to make python dil with this folder as a python package
# in this file i also config the flask instance - "app"

from flask import Flask



# create flask instance and some config
app = Flask(__name__, template_folder='../templates', static_folder='../static')




# Register the blueprints with the Flask app
from tools.numbers.simp import simp
from tools.numbers.comp import comp
from tools.col import col
app.register_blueprint(simp)
app.register_blueprint(comp)
app.register_blueprint(col)
