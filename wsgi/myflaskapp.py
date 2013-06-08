from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/fuelapp")
def hello():
    return "For all of your car comparison needs!"

if __name__ == "__main__":
    app.run()

