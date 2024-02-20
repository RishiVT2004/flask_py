from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def e_shop():
    return render_template('index.html') #-> used to render html page
    #return "Home Page of Our e-Shop"

@app.route('/products')
def list_prod():
    return 'list of products...'

if __name__ == "__main__":
    app.run(debug="True",port=8800)
