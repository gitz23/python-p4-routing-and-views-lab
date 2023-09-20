#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:route>')
def print_string(route):
    print(route)
    return route

@app.route('/count/<int:number>')
def count(number):
    #empty str
    count = f''
    for num in range(number):
        count += f'{num}\n'
    return count

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = 0
    if operation == '+':
        result = num1 + num2
    
    elif operation == '-':
        result = num1 - num2
    
    elif operation == '*':
        result= num1 * num2
    
    elif operation == 'div':
        result = num1 / num2
    
    elif operation == '%':
        result= num1 % num2

    return str(result)