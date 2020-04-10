##
## EPITECH PROJECT, 2020
## bootstrap
## File description:
## __init__
##

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views