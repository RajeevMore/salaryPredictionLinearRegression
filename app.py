from flask import Flask,app,jsonify,url_for, render_template, request
import pickle
import numpy as np

app=Flask(__name__)

@app.route("/")
def fun1():
    return render_template("info.html")

@app.route("/predict", methods = ["post"])
def fun2():
    nm = request.form['name']
    exp = float(request.form['exp'])
    mymodel = pickle.load(open('model1.pkl', "rb"))
    sal = round(mymodel.predict([[exp]])[0],2)
    return "<h1> hi {} <br/> your predicted salary is {} </h1>".format(nm,sal)

if __name__ == "__main__" :
     app.run(host='0.0.0.0')

