from flask import Flask, request, render_template, os
app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))
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
    app.run(host='0.0.0.0', port=port, debug=True)
