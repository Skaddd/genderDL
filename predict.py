##Created by Mateo Lebrun


"""
    This file is used by the application to load the models, predicit the results and display them on the image
"""


import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf


import cv2
import numpy as np
import time
import glob

import matplotlib.pyplot as plt

from tensorflow import keras
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array

import sklearn
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler



from face_alignment import face_ali_detec, resource_path

COUNT=0

age_class = {'(0, 2)': 0,
                '(4, 6)': 1,
                '(8, 12)': 2,
                '(15, 20)': 3,
                '(25, 32)': 4,
                '(38, 43)': 5,
                '(48, 53)': 6,
                '(60, 100)': 7}

#This function loads the tmp/ folder remove everthing in it, then creates the new images
#It also loads the pre-trained models
#As always we pre process the image before feeding it to the network for the predictions
#We call the function face_ali_detec used to recognize and crop all faces in the raw_image
#We save all the cropped/aligned faces then for each faces detected we predicit the result values, then store and display them
def prediction(path_image):
    date=time.strftime("%Y-%m-%d-%H-%M")
    with tf.device('/CPU:0'):
        faces_dir = 'detection\\images\\aligned\\tmp\\'
        path_test=faces_dir+'*'
        for file in glob.glob(resource_path(path_test)):
            os.remove(file)
        print("starting the process")
        new_model=tf.keras.models.load_model(resource_path('models\\gender_train_2.h5'))
        model2=tf.keras.models.load_model(resource_path('models\\age_train_0.h5'))
        raw_img=cv2.imread(path_image) 
        boundaries_b = face_ali_detec(path_image)
        results=[]
        ages=[]
        list_max_ages =[]

        for filename in os.listdir(resource_path(faces_dir)):
            if filename.endswith(".png"):
                
                path = os.path.join(resource_path(faces_dir),filename)
                img = cv2.imread(path)
                img = cv2.resize(img,(227,227))
                img = np.array(img).astype(np.float32)/255.
                img = np.expand_dims(img,axis=0)

                result =new_model.predict(img)
                result_age=model2.predict(img)
                ages = displayAge(result_age,ages)
                results.append(result[0][0])
                list_max_ages.append(np.amax(result_age))
                
                continue
            else:
                continue
        genders=displayGender(results)
        for k,box in  enumerate(boundaries_b) :
            cv2.rectangle(raw_img, (box.left(), box.top()), (box.right(), box.bottom()), (254,181,119), 2)
            #print(box.left(),box.right(),box.top(),box.bottom())
            cv2.putText(raw_img, genders[k], (box.left(), box.top()-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (254,181,119), 2)
            cv2.putText(raw_img, ages[k], (box.left()+60, box.top()-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (254,181,119), 2)
        outfile_2= 'detection\\images\\detected\\im-'+date+'.png'
        cv2.imwrite(resource_path(outfile_2),raw_img)
        return list_max_ages,results
        
        

#These two next function transforms probability into String
def displayGender(results):
    genders=[]
    for _ in results:
        if _<0.5 :
            genders.append('Male')
        else :
            genders.append('Female')
    return genders


def displayAge(results_age,ages):
    pred = max(results_age[0])
    get_key = list(results_age[0]).index(pred)
    list_keys = list(age_class.keys())
    ages.append(list_keys[get_key])
    return ages


if __name__ == "__main__":
    path_image ='c.jpg'
    prediction(path_image)
