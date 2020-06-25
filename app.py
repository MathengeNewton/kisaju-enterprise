from flask import Flask,render_template,request,url_for,redirect
from config import *

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route('/')
def main_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()