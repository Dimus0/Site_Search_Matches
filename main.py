from flask import Flask, redirect, url_for,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder='../template')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Player(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100),n)
    numbers_player = db.Column(db.Integer)

    def __repr__(self):
        return f'<Player: {self.name}, {self.numbers_player}>'

@app.route('/')
def hello_world():
    return 'Hello world', 200

def login():
    return render_template("index.html")
@app.route("/api/v1/hello-world-<name>")
def user(name):
    return f"Hello world, {name}"

if __name__ == '__main__':
    app.run(debug=True)



