import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow
import cv2
import numpy as np


import math as m
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array


img = load_img('test_im/e.jpg',target_size=(227,227))
img=img_to_array(img)

img = np.expand_dims(img,axis=0)
img=img/255.
#print(img.shape)

loaded=tf.keras.models.load_model('models/gender_train.h5')


layer_outputs=[ layer.output for layer in loaded.layers[0].layers]
res = loaded.layers[0]

activation_model = Model(inputs=res.input, outputs=layer_outputs)
activations=activation_model.predict(img)
img = np.squeeze(img,axis=0)


def display_activation(activations,index_layer):

    act=activations[index_layer]
    shapes = act.shape
    rows =int(np.sqrt(shapes[-1]))
    columns = rows
    fig=plt.figure(figsize=(rows, columns))
    print(rows,columns)
    for i in range(0, columns*rows):
        
        fig.add_subplot(rows, columns, i+1)
        plt.axis('off')
        plt.imshow(act[0, :, :, i], cmap='gray')
    plt.show()


display_activation(activations,5)


















"""

layer_outputs=[]
for l in loaded.layers:
   # if l.name == 'resnet50':
    #    continue
    #else :
        #layer_outputs.append(l.output)
    layer_outputs.append(l.output)

print(layer_outputs[0])
print(loaded.input)

activation_model = Model(inputs=loaded.input, outputs=layer_outputs)
activations=activation_model.predict(img)

"""


#activation_model=Model(inputs=loaded.inputs,outputs=layer_outputs)



