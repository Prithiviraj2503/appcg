from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='text-alighn:center;color:darkblue'>Hello World!<h1>"
    return "<h2 style='text-alighn:center;color:red'>Welcome To Cloud Computing Lab!<h2>"

if __name__ == "__main__":
    app.run()
