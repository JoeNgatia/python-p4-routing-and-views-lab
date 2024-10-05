from flask import Flask

app = Flask(__name__)

# Home page route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print a string route
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print the string in the console
    return f'Printed: {parameter}'  # Show the printed string in the browser

# Count route
@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '<br>'.join(str(i) for i in range(parameter + 1))  # Join numbers with line breaks
    return f'Counting to {parameter}:<br>{numbers}'  # Show the numbers

# Math operation route
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero"
    elif operation == '%':
        result = num1 % num2
    else:
        return "Error: Unsupported operation"
    
    return f'Result of {num1} {operation} {num2} = {result}'  # Show the result

# Run the application
if __name__ == '__main__':
    app.run(port=5555, debug=True)
