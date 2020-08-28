##Created by Mateo Lebrun

"""
    This file is used by the application in order to see 25 feautres maps from the 25 first layers( 1 feature per layer is visualized)
"""

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import re
import numpy as np
import imageio
import glob


import matplotlib.pyplot as plt

import tensorflow as tf
#print("Eager mode enabled: ", tf.executing_eagerly())
from tensorflow import keras
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array


#this methods  prepare the image before feeding it to the network
def preproces_img(path):
    img = load_img(path,target_size=(227,227))
    img=img_to_array(img)

    img = np.expand_dims(img,axis=0)
    img=img/255.
    return img


###The three next functions are different functions to display activations outputs
#First one will add all images on the same figure
#Second is not saving images
#Third saving images, so we use this one

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



def display_act_all(activations):
    print(len(activations))
    rows = int(np.sqrt(len(activations)))
    col = rows
    print(col*rows)
    fig=plt.figure(figsize=(rows,col))
    for i in  range (0,col*rows):
        fig.add_subplot(rows,col,i+1)
        plt.axis('off')
        plt.imshow(activations[i][0,:,:,2],cmap='gray')

    plt.show()

# the second parameter will define from how many layers we are going to extract feature map
#it will be the squared number , the max value is 12. default value is 5
def display_save_act_all(activations,number=5):
    rows = number
    col = rows
    print(col*rows)
    for i in  range (0,col*rows):
        fig =plt.figure(1)
        plt.axis('off')
        plt.suptitle(f"image de la couche {i}",fontsize=30)
        plt.imshow(activations[i][0,:,:,2],cmap='gray')
        fig.savefig('tmp/im{}.png'.format(i))
        plt.close(fig)

    plt.show()

def tryint(s):
    try:
        return int(s)
    except ValueError:
        return s
    
def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    return [ tryint(c) for c in re.split('([0-9]+)', s) ]

def sort_nicely(l):
    """ Sort the given list in the way that humans expect.
    """
    l.sort(key=alphanum_key)


##In this functions we are only focusing on the resnet50 part of our model
#We load our model then extract all outputs
#finally we call a function to save all images
#Images need to be sorted before creating the gif


def fin(path_img):
    with tf.device('/CPU:0'):

        img =preproces_img(path_img)
        loaded=tf.keras.models.load_model('./models/gender_train_2.h5')
        layer_outputs=[ layer.output for layer in loaded.layers[0].layers]
        res = loaded.layers[0]

        activation_model = Model(inputs=res.input, outputs=layer_outputs)
        activations=activation_model.predict(img)
        img = np.squeeze(img,axis=0)


        display_save_act_all(activations,10)

        images = []
        sorting_files = glob.glob("./tmp/*.png")
        sort_nicely(sorting_files)
        for file in sorting_files:
            images.append(imageio.imread(file))

        imageio.mimsave('./tmp/movie.gif', images,duration=0.5)


"""
    If you want to test this file alone, add an image named c.png in the same path 
"""

if __name__ =="__main__":
    fin('c.png')
    





