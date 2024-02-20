from flask import Flask
app = Flask(__name__)

app.route('/')
def even_no():
    return "even numbers are divisible by 2"
    

if __name__ == '__main__':
    app.run(debug=True,port=8800)

