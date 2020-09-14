from flask import Flask, jsonify, request
from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy
import os 
from flask_cors import CORS
from modelo import Desenho

app = Flask(__name__) 
CORS(app)
 
caminho = os.path.dirname(os.path.abspath(__file__))    
arquivobd = os.path.join(caminho, "desenhos.db") 

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+arquivobd 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
db = SQLAlchemy(app)