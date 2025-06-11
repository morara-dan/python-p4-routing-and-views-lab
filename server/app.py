#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    title = "Python Operations with Flask Routing and Views"
    return f"<h1>{title}</h1>"


@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return parameter


@app.route('/count/<parameter>')
def count(parameter):
    num = int(parameter)
    if num < 1:
        return "Please enter a number greater than 0"
    numbers = []
    for i in range(num):
        numbers.append(str(i))
    return "\n".join(numbers) + "\n"


@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    try:
        a = float(num1)
        b = float(num2)
    except ValueError:
        return "Invalid number format", 400

    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == 'div':
        if b == 0:
            return "Cannot divide by zero", 400
        result = a / b
        # Always return as a float string for the division route.
        return str(result)
    elif operation == '%':
        if b == 0:
            return "Cannot modulo by zero", 400
        result = a % b
    else:
        return "Operation not supported", 400

    # For non-division operations, return integer string if result is whole.
    if isinstance(result, float) and result.is_integer():
        return str(int(result))
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
