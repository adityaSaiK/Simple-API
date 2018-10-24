# Assume Error Codes -
# 200 - OK
# 290 - Missing Parameter
# 291 - denominator 0

from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Add(Resource):
    def post(self):
        data = request.get_json()
        if("x" not in data or "y" not in data):
            return jsonify({
                "message" : "Parameters missing",
                "status" : 290
            })
        num1 = data["x"]
        num2 = data["y"]
        num1 = int(num1)
        num2 = int(num2)
        sum = num1 + num2
        returnJson = {
            "Message" : sum,
            "status" : 200
        }
        return jsonify(returnJson)

class Subtract(Resource):
    def post(self):
        data = request.get_json()
        if("x" not in data or "y" not in data):
            return jsonify({
                "message" : "Parameters missing",
                "status" : 290
            })
        num1 = int(data["x"])
        num2 = int(data["y"])
        sub = num1 - num2
        return jsonify({
            "message" : sub,
            "status" : 200
        })


class Multiply(Resource):
    def post(self):
        data = request.get_json()
        if("x" not in data or "y" not in data):
            return jsonify({
                "message" : "Parameters missing",
                "status" : 290
            })
        num1 = int(data["x"])
        num2 = int(data["y"])
        mul = num1 * num2
        return jsonify({
            "message" : mul,
            "status" : 200
        })

class Divide(Resource):
    def post(self):
        data = request.get_json()
        if("x" not in data or "y" not in data):
            return jsonify({
                "message" : "Parameters missing",
                "status" : 290
            })
        num1 = int(data["x"])
        num2 = int(data["y"])
        if(num2 == 0):
            return jsonify({
                "message" : "denominator is 0",
                "status" : 291
            })
        sub = num1 / num2
        return jsonify({
            "message" : sub,
            "status" : 200
        })

api.add_resource(Add, '/add')
api.add_resource(Subtract, '/subtract')
api.add_resource(Multiply, '/multiply')
api.add_resource(Divide, '/divide')

@app.route('/')
def hello_world():
    return "hello_world"

if __name__ == "__main__":
    app.run(debug = True)
