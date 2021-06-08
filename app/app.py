import os
from flask import Flask
from pymemcache.client.base import Client
from flask import request

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

def fibonacci(count):
    previous_number = 1
    current_number = 2
    for i in range(count - 3):
        next_number = current_number + previous_number
        previous_number, current_number = current_number, next_number
    return current_number

@app.route('/')
def main():
    k = request.args.get('k')
    if k is not None:
        k = int(k)
    else:
        return "Вы не указали номер числа Фибоначчи"
    client = Client(('localhost', 11211))
    result = client.get(str(k))
    if result is None:
        result = fibonacci(k)
        client.set(str(k), str(result))
    return "{} число Фибоначчи = {}".format(k, result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
