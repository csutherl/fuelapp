from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/foo")
def foo():
    return "For all of your car comparison needs!"

# Testing where the templates dir should go, this works
@app.route('/hi/')
@app.route('/hi/<name>')
def hi(name=None):
    return render_template('test/hello.html', name=name)


if __name__ == "__main__":
    app.run()

