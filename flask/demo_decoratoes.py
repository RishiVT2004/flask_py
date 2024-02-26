from flask import Flask,render_template
#WSGI Aplication
app = Flask(__name__)  #initializing in flask

#decorator -> format(decorator.route(rule,options=""))
#rule -> string -> specify url


@app.route('/')
def home_page():
    return render_template('portfolio.html')

@app.route('/social')
def social_page():
    return render_template('social.html')

if __name__ == "__main__": #main method -> execution starts here
    app.run(debug=True,port=8000) # debug = True -> helps to update page without re running...
