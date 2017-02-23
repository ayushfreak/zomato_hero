from flask import Flask
from app.api.routes import mod
app = Flask(__name__)
app.register_blueprint(mod)
app.secret_key = 'development key'
