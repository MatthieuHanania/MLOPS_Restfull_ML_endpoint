import unittest
import keras
import pandas
from app import *


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)


    def test_classify(self):
        response = self.app.get('/classify')
        self.assertEqual(response.status_code, 200)
        
        #Testing if the model is good or not
        model = keras.models.load_model('mnistModel.h5')
        
        df_test = pd.read_csv("fashion-mnist_test.csv")
        X_test = df_test.loc[0][1:]/255
        Y_test = df_test.loc[0].label
        
        prediction= model.predict(X_test).tolist()
        self.assertEqual(response.json['name'], 'ben')
        max = np.argmax(prediction)
        self.assertEqual(max, 0)

if __name__ == '__main__':
    unittest.main()
