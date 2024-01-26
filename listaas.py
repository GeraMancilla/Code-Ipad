
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def saludar():
    nombre = request.form['nombre']
    return render_template('saludo.html', nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
