##building url dynamically
##flask variable and url building

from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to the youtube channel"

@app.route('/success/<int:score>')
def success(score):
    return "the person has passed and mark is "+str(score)

@app.route('/fail/<int:score>')
def fail(score) :
    return "the person has been failed in this examination"
   
@app.route('/result/<int:marks>')
def result(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result="success"
    return redirect(url_for(result,score=marks))
    return "the person has failed "


if __name__=="__main__":
    app.run(debug=True)