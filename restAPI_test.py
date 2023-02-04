#importing librairies
import pandas as pd
import numpy as np
import requests
import json

#read csv
df_test = pd.read_csv("fashion-mnist_test.csv")

#Data Preparation
Y_train = df_test.label
X_train = df_test.drop("label",axis=1)

#get the first line and pass it to a 
jsonToSent = [X_train.iloc[0].to_dict()]

#Test the request
URL = 'http://localhost:5000/classify'
r = requests.post(URL, json = jsonToSent)

pred = np.argmax(r.json()['values'][0])
print("Predicted :", pred,class_names[pred])
print("real : ", class_names[Y_train.loc[0]])

if pred ==Y_train.loc[0]:
    print("nice good pred !")
else:
    print("not good")
    assert False
