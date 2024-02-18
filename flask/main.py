from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'HOME PAGE !!!'

@app.route('/products')
def producr_page():
    return 'product page'

@app.route('/contents')
def content_page():
    return 'content page'

@app.route('/purchase')
def purchase_item():
    return 'proceed to purchase'


if __name__ == "__main__":
    app.run(debug=True, port=8000)



