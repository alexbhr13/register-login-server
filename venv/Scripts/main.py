import http

from flask import Flask, render_template, request
import db_handler
import json

app = Flask(__name__)

# Debug setting set to true
app.debug = True

@app.route('/')
def index():
    return "Greetings"

@app.route('/register', methods = ['POST'])
def register():
    print('register')
    try:
        data = request.form.to_dict()
        user = data['username']
        password = data['password']
    except Exception as e:
        print(e)
        return '3'
    try:
        dbconnection = db_handler.get_connection(db_handler.DEFAULT_USER,db_handler.DEFAULT_PASSWORD)
    except: return '3'
    cursor = dbconnection.cursor()
    try:
        cursor.callproc('register_user',[user,password])
        dbconnection.commit()
        for i in cursor.stored_results():
            results = i.fetchone()
            return str(results[0])
    except: return '3'
    return '3'

@app.route('/login', methods = ['POST'])
def login():
    print('login')
    try:
        data = request.form.to_dict()
        user = data['username']
        password = data['password']
    except Exception as e:
        print(e)
        return '3'
    try:
        dbconnection = db_handler.get_connection(db_handler.DEFAULT_USER,db_handler.DEFAULT_PASSWORD)
    except: return '3'
    cursor = dbconnection.cursor()
    try:
        cursor.callproc('check_user',[user,password])
        dbconnection.commit()
        for i in cursor.stored_results():
            results = i.fetchone()
            return str(results[0])
    except: return '3'
    return '3'

@app.route('/add_lol_account', methods = ['POST'])
def add_lol_account():
    print('add lol account')
    try:
        data=request.form.to_dict()
        user=data['username']
        lol_account=data['lol_account']
    except Exception as e:
        print(e)
    try:
        dbconnection = db_handler.get_connection(db_handler.DEFAULT_USER,db_handler.DEFAULT_PASSWORD)
    except: return '3'
    cursor = dbconnection.cursor()
    try:
        cursor.callproc('add_lol_account',[user,lol_account])
        dbconnection.commit()
        for i in cursor.stored_results():
            results = i.fetchone()
            return str(results[0])
    except: return '4'
    return '5'

@app.route('/get_lol_account', methods = ['POST'])
def get_lol_account():
    try:
        data=request.form.to_dict()
        user=data['username']
    except Exception as e:
        print(e)
    try:
        dbconnection = db_handler.get_connection(db_handler.DEFAULT_USER,db_handler.DEFAULT_PASSWORD)
    except: return '3'
    cursor = dbconnection.cursor()
    func = 'SELECT get_lol_account(%s)'
    try:
        result = cursor.execute(func,[user])
        val=cursor.fetchone()
        return str(val)
    except: return '4'
    return '5'

if __name__ == '__main__':
    app.run()