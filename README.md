# TP7_MLOS_API
the TP7 of MLOPS, I create a ml api


Firsly, I train a Deep learning model using the mnist dataset. (model_creation.ipynb) and I saved the model (mnistModel)


Then, we wanted to build an api that will use this model

So I develop an app.py file 

```python
@app.route('/classify', methods=['POST'])
def classify():
    image_data = request.get_json()
    query = pd.DataFrame(image_data)
    query = query/255
    prediction = model.predict(query).tolist()
    print(prediction)
    return prediction
```
To test it, we have to send a new line. ( from ImageToPredict.txt)  

We can use postman, and get a result
![alt text](https://github.com/MatthieuHanania/TP7_MLOS_API/blob/main/pict/Screenshot_1.png)

or dev it in python

![alt text](https://github.com/MatthieuHanania/TP7_MLOS_API/blob/main/pict/Screenshot_2.png)

The objective is to put the app.py file on docker.

So I developp a dockerfile that execute the app.py file, used to get the POST API, and a jenkinsfile that build the docker image and run it.


This repo is composed of : 

- the dockerfile that is used to build the docker image
- the jenkinsfile to build the docker image
- the app.py file
- fashion-mnist_test.csv is a csv used to test the IA model
- mnistModel.h5 : the model
- model_creation.ipynb used to create the model
- model_upgrage.ipynb improove the model with another dataset
- requirements.txt used to install all librairies
- test_main.py the unittest file
