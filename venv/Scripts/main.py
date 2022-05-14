import http

from flask import Flask, render_template, request
import db_handler

app = Flask(__name__)

# Debug setting set to true
app.debug = True

@app.route('/')
def index():
    return "Greetings from GeeksforGeeks"

@app.route('/register', methods = ['POST'])
def register():
    print('register')
    try:
        data = request.form.to_dict()
        print(data)
        user = data['username']
        password = data['password']
        print(user,password)
    except Exception as e:
        print(e)
        return '3'
    try:
        dbconnection = db_handler.get_connection(db_handler.DEFAULT_USER,db_handler.DEFAULT_PASSWORD)
    except: return '3'
    cursor = dbconnection.cursor()
    try:
        cursor.callproc('register_user',[user,password])
        for i in cursor.stored_results():
            results = i.fetchone()
            print(results)
            print(type(results))
            return str(results[0])
    except: return '3'
    print('nothing works')
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
        for i in cursor.stored_results():
            results = i.fetchone()
            print(results)
            print(type(results))
            return str(results[0])
    except: return '3'
    print('nothing works')
    return '3'

if __name__ == '__main__':
    app.run()