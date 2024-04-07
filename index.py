from flask import Flask

app = Flask(__name__)


@app.get("/")
def index():
    return "<h1>Hello From Flask</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("3000"), debug=True)
