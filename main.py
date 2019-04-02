#!/usr/bin/env python
from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/')
def my_form():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def my_form_post():
    wage = request.form['wage']
    hours = request.form['hours']
    multiply_text = float(hours) * float(wage)
    return str(multiply_text)
if __name__ == '__main__':
    app.run(debug=True)
