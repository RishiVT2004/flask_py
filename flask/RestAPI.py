"""
A RESTful API (Representational State Transfer API) is an architectural style for designing networked
applications. It relies on a stateless, client-server communication protocol, most commonly HTTP, and 
uses standard HTTP methods like GET, POST, PUT, DELETE, etc., to perform operations on resources.

In a RESTful API, resources are identified by unique URLs, and interactions with these resources are
typically performed using standard HTTP methods. For example, to retrieve a resource, you would send
an HTTP GET request to its URL. To create a new resource, you would send an HTTP POST request with
the necessary data to the resource's URL.

RESTful APIs are designed to be simple, scalable, and easy to maintain.
They are commonly used in web development to build web services that can be accessed by various 
clients, including web browsers, mobile devices, and other applications.

"""

from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return f"welcome to home"

@app.route('/<int:a>/<int:b>/check')
def check_number(a,b):
    if a>b:
        result = {
            "number1":a,
            "number2":b,
            "is_a_greater":"True"
        }
    else:
        result = {
            "number1":a,
            "number2":b,
            "is_a_greater":"False"
        }
    return jsonify(result)
    

if __name__ == "__main__":
    app.run(debug=True,port=2024)

