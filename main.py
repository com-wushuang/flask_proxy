from flask import Flask
import os
app = Flask(__name__)


@app.route("/health_check")
def hello():
    return "Hello World!"


@app.route("/docker/deploy/blog")
def deploy():
    code = os.system("bash deploy.sh")

    return "hello"

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
