"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq6582qv2dcb939cpg-a.oregon-postgres.render.com",
        database="todo_ug6r",
        user="todo_ug6r_user",
        password="tVnw5TeA1TZUP8Zhh3Q0EESJwoH1XJqP")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
