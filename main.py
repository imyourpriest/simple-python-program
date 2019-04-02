#!/usr/bin/env python
"""This script does a simple render of an html form page,
then takes the inputs and multiplies them"""

from flask import Flask, request, render_template
APP = Flask(__name__)

@APP.route('/')
def my_form():
    """Defines which html page to render"""
    return render_template("home.html")


@APP.route('/', methods=['POST'])
def my_form_post():
    """Takes user input from form, converts to float
    then converts result to string and displays"""
    wage = request.form['wage']
    hours = request.form['hours']
    multiply_text = float(hours) * float(wage)
    return str(multiply_text)


if __name__ == '__main__':
    APP.run(debug=True)
