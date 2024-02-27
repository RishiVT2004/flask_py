'''

get requests -> 
post requests -> 

'''



from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)

'''
@app.route('/',methods = ["GET"])
def prsonal_portfolio():
    return render_template('portfolio.html')

@app.route('/s',methods = ["GET"])
def social_info():
    return render_template('social.html')

@app.route('/about',methods=["GET"])
def about_user():
    return '<html><body>...This is made by Rishi...</body></html>'
'''


@app.route('/')
def home_page():
    return " ----- WELCOME TO HOME PAGE ----- "

#Variable Rule -: 
@app.route('/success/<float:score>')
def success(score):
    return "The person has passed and his/her score is : "+str(score)

@app.route('/fail/<float:score>')
def fail(score):
    return "The person has failed and his/her score is : "+str(score)

@app.route('/form',methods = ["GET","POST"])
def form():
    if request.method == "GET":
        return render_template('form.html')
    else:
        CSW = float(request.form['CSW'])
        ALA = float(request.form['ALA'])
        COA = float(request.form['COA'])

        average_mark = round((CSW+COA+ALA)/3,3)

        #return render_template('form.html',score = average_mark)
        #<h3>Average Marks = {{score}}</h3> -> jinja2 implementaion
    
    result = ""
    if average_mark>=70:
        result = "success"
    else:
        result = "fail"

    return redirect(url_for(result,score=average_mark))


if __name__ == "__main__":
    app.run(debug=True)
