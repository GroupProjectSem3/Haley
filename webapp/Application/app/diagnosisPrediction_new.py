import numpy as np # linear algebra
import pandas as pd

import tensorflow as tf
from keras.models import Sequential
#from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD


from sklearn import preprocessing
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import ShuffleSplit
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from keras.models import *
from keras.layers import Dense, Dropout, Activation
from keras.callbacks import *
from sklearn.model_selection import  ShuffleSplit, cross_val_score, cross_val_predict
from sklearn.metrics import confusion_matrix, classification_report
from django.conf import settings

class diagnosisPrediction_new:

    def predict(symptom):
        # for local
        df = pd.read_csv(settings.STATIC_ROOT+"/Training.csv")
        disease_prediction = tf.keras.models.load_model(settings.STATIC_ROOT+"/disease_prediction.h5") 

        #For deployment 
        #df = pd.read_csv("https://deployment-haley.ew.r.appspot.com/static/Training.csv")
        #disease_prediction = tf.keras.models.load_model("https://deployment-haley.ew.r.appspot.com/static/disease_prediction.h5") 
        #Splitting target and categorical attributes
        X = np.array(df.iloc[:, df.columns != 'Disease'])
        y = np.array(df.iloc[:, df.columns == 'Disease'])
        x_train, x_test, y_train, y_test = train_test_split(X,y,
                                                    test_size=.20,
                                                    random_state=42, stratify = y)
        values=np.unique(y_train)

        #Create Dictionary for mapping new inputs
        indices = [i for i in range(100)]
        symptoms = df.columns.values[:-1]

        dictionary = dict(zip(symptoms,indices))      
        #mapping inputs to respective columns
        prediction = []
        user_input_symptoms = symptom
        user_input_label = [0 for i in range(100)]
        for i in user_input_symptoms:
            idx = dictionary[i]
            user_input_label[idx] = 1

        user_input_label = np.array(user_input_label)
        user_input_label = user_input_label.reshape((-1,1)).transpose()
        #passing the inputs to predict function of the model
        ds = disease_prediction.predict(user_input_label)
        L = np.argsort(-ds, axis=1)
        #return(values[L[:,0]],"Percentage:",((ds[0,L[:,0]]*100)),values[L[:,1]],"Percentage:",(ds[0,L[:,1]]*100),values[L[:,2]],"Percentage:",(ds[0,L[:,2]]*100))
        # making a list to return
        outList = list()
        outList.append(values[L[:,0]][0]+'_'+str((ds[0,L[:,0]]*100)[0]))
        outList.append(values[L[:,1]][0]+'_'+str((ds[0,L[:,1]]*100)[0]))
        outList.append(values[L[:,2]][0]+'_'+str((ds[0,L[:,2]]*100)[0]))
        return outList




