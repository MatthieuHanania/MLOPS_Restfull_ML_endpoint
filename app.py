from flask import Flask, request
from tensorflow import keras
import numpy as np
import pandas as pd


app = Flask(__name__)

model = keras.models.load_model('mnistModel.h5')

@app.route('/classify', methods=['POST'])
def classify():
    image_data = request.get_json()
    query = pd.DataFrame(image_data)
    query = query/255
    prediction = model.predict(query).tolist()
    print(prediction)
    return prediction

if __name__ =="__main__":
    app.run(debug=True)

