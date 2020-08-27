import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

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




def preproces_img(path):
    img = load_img(path,target_size=(227,227))
    img=img_to_array(img)

    img = np.expand_dims(img,axis=0)
    img=img/255.
    return img


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




def display_save_act_all(activations):
    rows = 5
    col = rows
    print(col*rows)
    for i in  range (0,col*rows):
        fig =plt.figure(1)
        plt.axis('off')
        plt.imshow(activations[i][0,:,:,2],cmap='gray')
        fig.savefig('tmp/im{}.png'.format(i))
        plt.close(fig)

    plt.show()


def fin(path_img):
    with tf.device('/CPU:0'):

        img =preproces_img(path_img)
        loaded=tf.keras.models.load_model('models/gender_train_2.h5')
        layer_outputs=[ layer.output for layer in loaded.layers[0].layers]
        res = loaded.layers[0]

        activation_model = Model(inputs=res.input, outputs=layer_outputs)
        activations=activation_model.predict(img)
        img = np.squeeze(img,axis=0)


        display_save_act_all(activations)

        images = []
        size=(64,64)
        for file in glob.glob("./tmp/*.png"):
            #print(file)
            images.append(imageio.imread(file))
        imageio.mimsave('movie.gif', images,duration=0.5)

   


if __name__ =="__main__":
    fin('c.png')
    





