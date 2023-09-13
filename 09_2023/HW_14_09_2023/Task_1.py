# Задание №_1 Создать html template и подключить к python, с использованием фрэймворка flask

from flask import Flask, render_template

app = Flask(__name__)
cat = ['PHILOSOPHY', 'ABOUT', 'WORK', 'CONTACT', 'SOCIAL']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/example')
def example():
    return 'Hello World'


app.run(debug=True)
