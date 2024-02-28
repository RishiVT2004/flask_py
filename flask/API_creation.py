from flask import Flask,render_template,request
from flask import jsonify


app = Flask(__name__)

#using api (posting data and generating returns)
'''
Application Programming Interface -> is a set of rules and protocols that allows different software
,applications to communicate with each other. APIs define the methods and data formats 
that applications can use to request and exchange information.

->They are commonly used to enable interaction between different software systems,
->such as web applications, databases, and operating systems, by providing a standardized way for
,them to communicate and share data. APIs can be used to access functionality or data from a 
,remote system, integrate with third-party services, or build modular and scalable software applications.
'''

#using postman
# no get method in api

@app.route('/')
def home():
    return f"HOME-PAGE"

@app.route('/api', methods = ["POST"])
def calculate_mul():
    #create a json file and fetch data for api from there
    data = request.get_json()
    x_value = (dict(data))['x']
    y_value = (dict(data))['y']
    return jsonify(x_value*y_value)


if __name__ == "__main__":
    app.run(debug=True)

"""
to host an api -: 
1. go to postman
2. select method as post
3. go to body -> raw -> select json    
4. go to ur json file and copy the data
5.enter send api 
"""
