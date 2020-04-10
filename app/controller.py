##
## EPITECH PROJECT, 2020
## bootstrap
## File description:
## controller
##

from flask import Flask, request, redirect, url_for
from flask_login import current_user, login_user
from app import app
import pymysql as sql

@app.route('/signin', methods=['POST'])
def signin_user(data):
    print(data)
    return ('0')