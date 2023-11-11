from flask import Flask, redirect, url_for,render_template

app = Flask(__name__)

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



