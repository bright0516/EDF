#coding=utf-8
from flask import Flask
import sys
sys.path.append("D:\python_wgm\IntelligentConsultation")
# from models.book import db

def create_app():
    app = Flask(__name__)
    app.config.from_object("setting")
    app.config.from_object("secure")
    app.config['JSON_AS_ASCII'] = False
    # 加载蓝图
    register_blueprint(app)

def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
