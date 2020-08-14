import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf


import cv2
import numpy as np


import math as m
import matplotlib.pyplot as plt

from tensorflow import keras
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array

import sklearn
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler



from detection.face_alignment import face_ali_detec
from detection.face_alignment import date
COUNT=0

age_class = {'(0, 2)': 0,
                '(4, 6)': 1,
                '(8, 12)': 2,
                '(15, 20)': 3,
                '(25, 32)': 4,
                '(38, 43)': 5,
                '(48, 53)': 6,
                '(60, 100)': 7}

def prediction(path_image):
    print("starting the process")
    new_model=tf.keras.models.load_model('./models/gender_train_2.h5')
    model2=tf.keras.models.load_model('./models/age_train_0.h5')
    print(path_image)
    raw_img=cv2.imread(path_image)
    boundaries_b = face_ali_detec(path_image)
    results=[]
    ages=[]
    faces_dir = './detection/images/aligned/'
    for filename in os.listdir(faces_dir):
        if filename.endswith(".png"):
            
            print(filename)
            path = os.path.join(faces_dir,filename)
            img = cv2.imread(path)
            img=cv2.resize(img,(227,227))
            img = np.array(img).astype(np.float32)/255.
            img = np.expand_dims(img,axis=0)
            result =new_model.predict(img)
            result_age=model2.predict(img)

            ages = displayAge(result_age,ages)
            results.append(result)
            continue
        else:
            continue
    genders=displayGender(results)
    #print(len(genders))
    #print(len(ages))
    for k,box in  enumerate(boundaries_b) :
        cv2.rectangle(raw_img, (box.left(), box.top()), (box.right(), box.bottom()), (36,255,12), 2)
        #print(box.left(),box.right(),box.top(),box.bottom())
        cv2.putText(raw_img, genders[k], (box.left(), box.top()-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36,255,12), 2)
        cv2.putText(raw_img, ages[k], (box.left()+60, box.top()-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36,255,12), 2)
    outfile_2= 'detection/images/detected/im-'+date+'.png'
    cv2.imwrite(outfile_2,raw_img)

    
    """
    files = './detection/images/aligned/*'
    for f in files :
        print(f)
        os.remove(f)
    """



def displayGender(results):

    genders=[]
    for _ in results:
        if _<0.5 :
            genders.append('Male')
        else :
            genders.append('Female')
    return genders

# load the model we saved
#model = load_model('model.h5')

def displayAge(results_age,ages):
    #print(results_age)
    pred = max(results_age[0])
    get_key = list(results_age[0]).index(pred)
    list_keys = list(age_class.keys())
    #print(list_keys[get_key])
    ages.append(list_keys[get_key])
    return ages


if __name__ == "__main__":
    path_image ='pictures/c.jpg'
    prediction(path_image)