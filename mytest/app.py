from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

@app.route('/html')
def html_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
