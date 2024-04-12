from flask import Flask, request

app = Flask(__name__)

@app.route("/saludar")
def saludar():
    return "<h1>hola, mundo</h1>"

@app.route("/factorial")
def factorial():
    fact = 1
    num = int(request.args.get('num'))
    for i in range(1, num + 1):
        fact *= i

    return str(fact)