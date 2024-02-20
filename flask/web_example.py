from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

#creating a database and using sql-alchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASES_URI'] = "sqlite:///portfolio.db" #sqlite database
db = SQLAlchemy(app)

@app.route('/')
def e_shop():
    return render_template('portfolio.html')

if __name__ == "__main__":
    app.run(debug="True",port=8000)

