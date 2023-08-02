### Integrate HTML with flask
###HTTP verb GET and POST
from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
#route is used to specify the url of the web page
@app.route("/")
def welcome():
    render_template('index.html')
@app.route('/success/<int:score>')
def success(score):
     res=""
     if score>=50:
         res="Pass"
     else:
         res="fail"    
     return render_template('res.html',result=res)

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

###Result checker  submit html page
@app.route('/submit',methods=['POST',"GET"])
def submit():
    total_score=0
    if request.method=="POST":
        science=float(request.form['scinece'])
        math=float(request.form['math'])
        total_score=(science+math)/2
        
        res=""
        if total_score>=50:
            res="success"
        else:
            res="fail"
        return redirect(url_for(res,score=total_score))


if __name__=="__main__":
    app.run(debug=True)