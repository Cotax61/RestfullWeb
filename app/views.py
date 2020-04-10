##
## EPITECH PROJECT, 2020
## bootstrap
## File description:
## view
##

from app import app
from . import controller
from . import models
from flask import render_template, jsonify
import pymysql as sql

@app.route('/', methods=['GET'])
def route_index():
    return render_template("main.html")

@app.route('/test', methods=['POST'])
def route_test():
    print("got a call")
    return jsonify(render_template('login.html'))

@app.route('/user')
def route_all_user():
    result = ""
    try:
        connect = sql.connect('localhost',
                            'Cotax',
                            'oof',
                            'db1')
        cursor = connect.cursor()
        cursor.execute("SELECT CURRENT_USER();")
        result = cursor.fetchall()
        cursor.close()
        connect.close()
    except Exception as err:
        print('Caught an exception : ', err)
    return (format(result[0]))