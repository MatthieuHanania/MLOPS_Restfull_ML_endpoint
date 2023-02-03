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

I modify the app.py file before putting it on the docker image, now it print the type of the prediction ( the mnist dataset).
And in order to connect postman with the docker container, we have to specify in the dockerfile, the port 5000:5000, and to put 0.0.0.0 in the app.py
```python
class_names = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt',
               'Sneaker','Bag','Ankle boot']
def classify():
    image_data = request.get_json()
    query = pd.DataFrame(image_data)
    query = query/255
    prediction = model.predict(query).tolist()
    print(prediction)

    max = np.argmax(prediction)
    type = class_names[max]

    dic={"Type":type,"values":prediction}
    return dic

if __name__ =="__main__":
    app.run(host='0.0.0.0',debug=True)

```

So, when I try it on postman I get:

![alt text](https://github.com/MatthieuHanania/TP7_MLOS_API/blob/main/pict/app%20on%20docker.png)

And we can see on docker the prediction printed

![alt text](https://github.com/MatthieuHanania/TP7_MLOS_API/blob/main/pict/dockerPostRequest.png)
