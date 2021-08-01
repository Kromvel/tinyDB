1. Создание и загрузка форм в базу:
from flask import Flask, request, jsonify
from tinydb import TinyDB, Query


# Server
app = Flask(__name__)

# Database
db = TinyDB('db.json')

Base = Query()
headers = {'content-type': 'application/json'}

db.insert_multiple(
    [
{'name':'My_Form_1', 'email': 'john@gmail.com', 'phone': '+7 921 543 43 31', 'date': '22.07.2021', 'message': 'Hello World!'},
 {'name':'My_Form_2','email': 'steve@gmail.com', 'phone': '+7 911 765 54 49', 'date': '19.07.2021', 'message': 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'},
{'name':'My_Form_3', 'email': 'kate@gmail.com', 'phone': '+7 911 373 23 37', 'date': '20.07.2021', 'message': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'},
{'name':'My_Form_4', 'email': 'george@gmail.com', 'phone': '+7 901 322 73 67', 'date': '24.07.2021', 'message': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.'},
{'name':'My_Form_5', 'email': 'george@gmail.com', 'phone': '+7 911 452 83 27', 'date': '21.07.2021', 'message': 'Duis aute irure dolor in reprehenderit in voluptate velit.'}

    ]
    
)

2. Проверка на наличие формы:
import requests 
api_url = 'http://127.0.0.1:5000/form-example'
requestData = {'email':'kate@gmail.com','phone': '+7 911 373 23 37','date': '20.07.2021','message': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'}
r = requests.post(url=api_url, params = requestData)
print(r.text)