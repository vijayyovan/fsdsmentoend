from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route('/success/<int:score>')
def success(score):
    return "the person is passed and the score is "+str(score)

@app.route('calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])

        average_marks=(maths+science)/2
        

        if average_marks>50:


        return render_template('result.html',results=average_marks)



if __name__=='__main__':
    app.run(debug=True)