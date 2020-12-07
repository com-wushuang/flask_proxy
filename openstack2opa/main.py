import requests
from flask import Flask, request
import json
from target import Parser

app = Flask(__name__)


@app.route("/health_check")
def hello():
    return "Hello World!"


@app.route("/stack/policy/check", methods=["POST"])
def check_without_param():
    input_opa = {
        "input": {}
    }
    form = request.form
    input_opa["input"]["credentials"] = json.loads(form["credentials"])
    input_opa["input"]["rule"] = json.loads(form["rule"])
    target = Parser(json.loads(form["target"]))
    input_opa["input"]["target"] = target

    resp = check_in_opa(input_opa)
    if resp["allow"]:
        return "True"
    else:
        return "False"


def check_in_opa(input_opa):
    url = "http://192.168.9.207:31365/v1/data/openstack/policy"
    resp = requests.post(url=url, data=json.dumps(input_opa))
    result = resp.json()["result"]
    return result


if __name__ == "__main__":
    app.run("0.0.0.0", port=1323, debug=True)
