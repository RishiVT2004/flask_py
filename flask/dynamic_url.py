from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('portfolio.html')

@app.route('/social')
def social_page():
    return render_template('social.html')

@app.route('/img')
def image_page():
    return render_template('img.html')

if __name__ == "__main__": #main method -> execution starts here
    app.run(debug=True,port=8000) # debug = True -> helps to update page without re running...
