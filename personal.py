from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/curriculo')
def curriculo():
    return  render_template('curriculo.html')

if __name__ == '__main__':
    app.run(debug=True)