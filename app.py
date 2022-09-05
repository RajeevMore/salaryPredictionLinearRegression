from flask import Flask,app,jsonify,url_for, render_template, request
import pickle
import numpy as np

app=Flask(__name__)

@app.route("/")
def fun1():
    return render_template("info.html")
'''
@app.route("/predict", methods = ["post"])
def fun2():
    nm = request.form['name']
    exp = float(request.form['exp'])
    mymodel = pickle.load(open('model1.pkl', "rb"))
    sal = round(mymodel.predict([[exp]])[0],2)
    return "<h1> hi {} <br/> your predicted salary is {} </h1>".format(nm,sal)
'''
@app.route("/predict", methods = ["post"])
def fun2():
    data = request.json['data']
    print(data)
    #print(np.array(list(data.values())).reshape(1,-1))
    new_data = np.array(list(data.values())).reshape(1,-1)
    mymodel = pickle.load(open('model1.pkl', "rb"))
    sal = round(mymodel.predict([[new_data]])[0],2)
    return jsonify (sal[0])

if __name__ == "__main__" :
     app.run(debug=True)

