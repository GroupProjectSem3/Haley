from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import csv
import numpy as np
import pandas as pd
import os
from django.conf import settings


class DiagnosisPrediction:

    #data = pd.read_csv("/content/drive/My Drive/Group_Project/Training.csv")
    def predict(symptom):
        #data = pd.read_csv(os.path.join(settings.STATIC_URL, "Training.csv"))
        #For local deployment
        #data = pd.read_csv(settings.STATIC_ROOT+"/Training.csv")
        #For deployment only
        data = pd.read_csv("https://final-haley.nw.r.appspot.com/static/styles/Training.csv")
        
        df = pd.DataFrame(data)
        cols = df.columns
        cols = cols[:-1]
        x = df[cols]
        y = df['Disease']
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.33, random_state=42)

        print("DecisionTree")
        dt = DecisionTreeClassifier()
        clf_dt = dt.fit(x_train, y_train)
        #print ("Acurracy: ", clf_dt.score(x_test,y_test))

        indices = [i for i in range(100)]
        symptoms = df.columns.values[:-1]

        dictionary = dict(zip(symptoms, indices))

        user_input_symptoms = symptom
        user_input_label = [0 for i in range(100)]
        for i in user_input_symptoms:
            idx = dictionary[i]
            user_input_label[idx] = 1

        user_input_label = np.array(user_input_label)
        user_input_label = user_input_label.reshape((-1, 1)).transpose()
        return(dt.predict(user_input_label))


#def dosomething(symptom):
#  user_input_symptoms = symptom
#   user_input_label = [0 for i in range(100)]
#    for i in user_input_symptoms:
#         idx = dictionary[i]
#         user_input_label[idx] = 1

#     user_input_label = np.array(user_input_label)
#     user_input_label = user_input_label.reshape((-1, 1)).transpose()
#     return(dt.predict(user_input_label))

#print(dosomething(['Sneezing', 'Sore Throat', 'Stuffy Nose' ]))
#prediction = []
#for i in range(7):
#    pred = dosomething(['Sneezing', 'Sore Throat', 'Stuffy Nose'])
#    prediction.append(pred)
#print(prediction)
