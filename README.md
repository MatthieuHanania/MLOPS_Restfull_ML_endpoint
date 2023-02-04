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

The Jenkinfile has 4 pipelines : 
- Print hello word
- Test the model by directly call it
- Build a docker image and run it, the docker container contains the app.py file and it is possible to do an API request
- testing the API request and test the model

This repo is composed of : 

- the dockerfile that is used to build the docker image
- the jenkinsfile to build the docker image
- the app.py file
- fashion-mnist_test.csv is a csv used to test the IA model
- mnistModel.h5 : the model
- model_creation.ipynb used to create the model
- model_upgrage.ipynb improove the model with another dataset
- model_test.ipynb to try the model on a choosen image
- requirements.txt used to install all librairies
- test_main.py the unittest file
- restAPI_test.py is a file executed by jenkins and it test the prediction of an image by calling the API

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


To try the API on the docker file, I also used the model_test file. 
```python
 jsonToSent = [X_train.iloc[0].to_dict()] #the first image : a T shirt
 
#Test the request
URL = 'http://localhost:5000/classify'
r = requests.post(URL, json = jsonToSent)
r.json()
```

 Then I can compare is the prediction if the prediction is good or not on a test
 ```python
pred = np.argmax(r.json()['values'][0])
if pred ==Y_train.loc[0]:
    print("nice good pred !")
```
In our case, the model predict a T shirt
![alt text](https://github.com/MatthieuHanania/TP7_MLOS_API/blob/main/pict/T%20shirt%20image.png)

And finally, I create the restAPI_test.py that is called by the jenkinsfile to test the API and if the model is good or not.
