# -*- coding: utf-8 -*-

#importing libraries
from sklearn.externals import joblib
import Extractor

#load the pickle file
classifier = joblib.load('Save_models/rf_final.pkl')

#input url
print("enter url")
url = input()

#checking and predicting
checkprediction = Extractor.main(url)
prediction = classifier.predict(checkprediction)
print(prediction)
