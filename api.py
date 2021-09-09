from unicodedata import name
from flask import Flask,request, url_for, redirect, render_template
from pandas.io.pytables import Table
from sklearn.externals import joblib
import Extractor
import pickle
import numpy as np
from wsgiref import simple_server
from flask import jsonify
import pandas as pd
from tabulate import tabulate
app = Flask(__name__)

# model=pickle.load(open('XGBoostClassifier.pickle.dat','rb'))


@app.route('/',methods=['GET'])
def hello_world():
    return render_template("index.html", len1 = 0 )


# @app.route('/predict',methods=['POST','GET'])
# def predict():

#     print("Working")
#     classifier = joblib.load('XGBoostClassifier.pickle.dat')
#     #input url
#     print("enter url")
#     url = "venturegroupit.com"
#     # print(url)
#     # print(url)

#     # #checking and predicting
    # checkprediction = URLFeatureExtraction.featureExtraction(url)
#     prediction = classifier.predict(checkprediction)
#     # print(checkprediction.count(1))
#     # print(prediction)
#     # if prediction == 1:
#     #     print("Y")
#     # else:
#     #     print("N")
#     if prediction==1:
#         return render_template('index.html',pred="Legitimate")
#     else:
#         return render_template('index.html',pred="Phishy")
@app.route('/testing',methods=['GET','POST'])
def getURL():
    if request.method == 'POST':
        print("in work")
        url = request.form.get('my_url')
        print(url)
        classifier = joblib.load('Save_models/rf_final.pkl')
        checkprediction = Extractor.main(url)
        prediction = classifier.predict(checkprediction)
        dataset = pd.read_csv("datasets/phishcoop.csv")
        df=pd.DataFrame(dataset)
        df.drop(df.columns[[0, 31]], axis = 1, inplace = True)
        zip_iterator = zip(df.columns, checkprediction[0])
        a_dictionary = dict(zip_iterator)
        for i in a_dictionary:
            print("{}\t{}".format(i,a_dictionary[i]))

        print(df.columns)
        print(prediction)
        print(checkprediction)
        
        # api code
        
        # if(prediction[0]== -1 ):
        #     sol = "Legitimate"
        # else:
        #     sol = "Phishing"
        # print(sol) 
        # print("its working")
        # return jsonify(
        #             message= sol ,
        #         )
        
        # api code end
        # print(df1)
        if prediction == -1:    
            value = "Legitimate"
            return render_template("index.html",error=value,dic=a_dictionary , len1 =1 ,my_url=url)
        else:
            value = "Phishy"
            return render_template("index.html",error=value,dic=a_dictionary , len1 =1, my_url=url )

if __name__ == '__main__':
    app.run(debug=True)
    # host = '0.0.0.0'
    # port = 8000
    # httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    # httpd.serve_forever()