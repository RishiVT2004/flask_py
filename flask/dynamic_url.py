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

#bulding url dynamically -; 

@app.route('/cgpa/<float:cgpa>') #parametric values, building url dynamically...
def calculate(cgpa): 
    return f"cgpa of the person is "+str(cgpa)

@app.route('/cgpa/<float:cgpa>/checkresult')
def check_pass_fail(cgpa):
    result = ""
    if cgpa>7.5:
        result="eligible to appear for intern"
    else:
        result="not-eligible to appear for intern"

    return f'<html><body><h1>judgement based on marks : </h1></body></html>'+str(result)        
    


if __name__ == "__main__": #main method -> execution starts here
    app.run(debug=True,port=8000) # debug = True -> helps to update page without re running...




if __name__ == "__main__": #main method -> execution starts here
    app.run(debug=True,port=8000) # debug = True -> helps to update page without re running...

