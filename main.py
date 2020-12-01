from flask import Flask,request
import os

app = Flask(__name__)


@app.route("/health_check")
def hello():
    return "Hello World!"


@app.route("/docker/deploy/blog", methods=["POST"])
def deploy():
    code = os.system("bash deploy.sh")
    if code == 0:
        return "ok"
    else:
        return "failed"

@app.route("/stack/policy/check",methods=["POST"])
def check_without_param():
    print request.from
    return "True"

@app.route("/stack/param/<name>",methods=["POST"])
def check_with_param(name):
    print name
    print request.from
    return "True"



if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
