from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def prsonal_portfolio():
    return render_template('portfolio.html')

@app.route('/socials')
def social_info():
    return render_template('socials.html')

if __name__ == "__main__":
    app.run(debug="True",port=8000)

