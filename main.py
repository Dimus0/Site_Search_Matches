from flask import Flask, redirect, url_for,render_template
from flask_sqlalchemy import SQLAlchemy
from URL.url import my_blueprint

app = Flask(__name__,template_folder='./template')
app.register_blueprint(my_blueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbtest.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == '__main__':
    app.run(debug=True)
