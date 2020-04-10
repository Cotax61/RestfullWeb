from app import app
from . import controller
from flask import render_template
import pymysql as sql

def update_render():
    is_connected = False
    username = ""
    return (render_template("main.html"))