from flask import Flask,request,render_template
import pickle
import numpy as np
 


app=Flask(__name__)


with open("model1.pkl","rb") as model_file:
    ml_model=pickle.load(model_file)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process",methods=["POST"])
def process():
    if(request.method=="POST"):
        features=[
            float(request.form['Pregnancies']),
            float(request.form['Glucose']),
            float(request.form['BloodPressure']),
            float(request.form['SkinThickness']),
            float(request.form['Insulin']),
            float(request.form['BMI']),
            float(request.form['DiabetesPedigreeFunction']),
            float(request.form['Age'])
        ]
        input_data=np.array(features).reshape(1,-1)
        result=ml_model.predict(input_data)[0]
        diagnosis="Diabetic" if result==1 else "Non Diabetic"
        print("Predicted result :",diagnosis)
        
        return render_template("myresult.html",prediction=diagnosis)

if(__name__=="__main__"):
    app.run(debug=True)







































































