import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow
import cv2
import numpy as np


import math as m
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Conv2D, Flatten,Dropout, Dense, AveragePooling2D, GlobalAveragePooling2D
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.preprocessing.image import ImageDataGenerator


import sklearn
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler



def gpu_dynamic_mem_growth():
    # Check for GPUs and set them to dynamically grow memory as needed
    # Avoids OOM from tensorflow greedily allocating GPU memory
    try:
        gpu_devices = tf.config.list_physical_devices('GPU')
        if len(gpu_devices) > 0:
            for gpu in gpu_devices:
                tf.config.experimental.set_memory_growth(gpu, True)
    except AttributeError:
        print('Upgrade your tensorflow to 2.x to have the gpu_dynamic_mem_growth feature.')


print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

#PARSING DATA

base_dir=os.path.join(os.getcwd(),'data')
print(base_dir)
files_list = ['fold_0_data.txt', 'fold_1_data.txt', 'fold_2_data.txt', 'fold_3_data.txt', 'fold_4_data.txt']

Width =227
Height=227
global COUNT
COUNT = 1
EPOCHS = 5
BATCH_SIZE = 16

with tf.device('/CPU:0'):
    

    all_data =[]
    for txt in files_list:
        with open(os.path.join(base_dir,txt),'r') as file:
            lines=file.readlines()[1:]
            for line in lines:
                data=line.strip().split('\t')
                all_data.append([data[0],data[2]+'.'+data[1],data[3],data[4]])
    #print(all_data[0])





    age_class = {'(0, 2)': 0,
                    '(4, 6)': 1,
                    '(8, 12)': 2,
                    '(15, 20)': 3,
                    '(25, 32)': 4,
                    '(38, 43)': 5,
                    '(48, 53)': 6,
                    '(60, 100)': 7}
    gender_class = {'m': 0.0, 'f': 1.0}




    age_data = []
    gender_data = []
    age_gender_data = []
    i=0
    prefix = ''
    for data in all_data:
        try:
            if data[2] == '(38, 42)' or data[2] == '(38, 48)':
                data[2] = '(38, 43)'

            if data[2] == '(27, 32)':
                data[2] = '(25, 32)'

            if data[2] not in age_class and data[2]is not None:
                age = int(data[2])
                if 0 <= age <= 3:
                    data[2] = '(0, 2)'
                elif 4 <= age <= 7:
                    data[2] = '(4, 6)'
                elif 8 <= age <= 14:
                    data[2] = '(8, 12)'
                elif 15 <= age <= 24:
                    data[2] = '(15, 20)'
                elif 25 <= age <= 37:
                    data[2] = '(25, 32)'
                elif 38 <= age <= 47:
                    data[2] =  '(38, 43)'
                elif 48 <= age <= 59:
                    data[2] = '(48, 53)'
                elif 60 <= age <= 100:
                    data[2] = '(60, 100)'
            if data[2] is not None and data[3]!='u':
                age_gender_data.append((os.path.join(base_dir, 'aligned/' + data[0] + '/landmark_aligned_face.' + data[1]),age_class[data[2]], gender_class[data[3]]))
                age_data.append((os.path.join(base_dir, 'aligned/' + data[0] + '/landmark_aligned_face.' + data[1]),age_class[data[2]]))
                gender_data.append((os.path.join(base_dir, 'aligned/' + data[0] + '/landmark_aligned_face.' + data[1]),gender_class[data[3]]))

        except:
            pass




    #Splitting the data into  train validation and test sets
    train_df,temp = train_test_split(gender_data,test_size=0.5)

    temp_=None

    train_labels_gen =[]
    train_labels_age=[]


    #DATA PROCESSING

    def one_hot_code(list1):
        n = len(list1)
        out = np.zeros((n,8))
        print(max(list1))
        for k in range (n):
            out[k][int(list1[k])] =1.0
        return out

    def unzipdata(train_df):
        if COUNT ==0:
            print("You picked age only")
            train_df,train_labels_age =map( list,zip(*train_df))

            labels = one_hot_code(train_labels_age)
        
        else:
            print("You picked gender only")
            train_df,train_labels_gen =map( list,zip(*train_df))
            labels=np.resize(np.array(train_labels_gen),(len(train_labels_gen),1))

        return train_df,labels,

    def preproc( path_img):
        im =cv2.imread(path_img)
        im =cv2.resize(im,(227,227))
        return im



    train_df,labels=unzipdata(train_df)

    print("Precrossing the data")

    for _ in range (len(train_df)):
        train_df[_]= preproc(train_df[_])


    

    images = np.array(train_df)


    print(images.shape)
    print(labels.shape)



    images = images.astype(np.float32)/255.0
    train_images,test_images,train_labels,test_labels = train_test_split(images,labels,test_size=0.1)



    train_images,val_images,train_labels,val_labels = train_test_split(train_images,train_labels,test_size = 0.2)





def modelGA():
    backbone = ResNet50(input_shape=(227,227,3),weights='imagenet', include_top=False)
    model = Sequential()
    model.add(keras.Input(shape=(227,227,3)))
    model.add(backbone)
    model.add(GlobalAveragePooling2D())
    model.add(Dropout(0.5))
    model.add(Dense(256,activation='relu'))
    model.add(Dropout(0.5))
    if COUNT ==0:
        model.add(Dense(8,activation='softmax'))
        model.compile(optimizer='sgd',loss='categorical_crossentropy',metrics=['accuracy'])
    else:
        model.add(Dense(1,activation='sigmoid'))
        model.compile(optimizer='sgd',loss='binary_crossentropy',metrics=['accuracy'])
    return model
    
#CALLBACKS
    
checkpoint_path = "training_test/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
cp_callback1 = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,save_best_only=True, monitor="val_loss",
                                                    save_weights_only=True,verbose=1)


#es =keras.callbacks.EarlyStopping(monitor='val_loss',min_delta=1e-2,patience=2,verbose=1)
#te =tf.keras.callbacks.TensorBoard(log_dir='C:/Users/LD/Documents/Age_gender_Clas/logs', write_graph=True,write_images=True)


#Learning Rate Shceduler

initial_lr=0.001
lr_schedule = keras.optimizers.schedules.ExponentialDecay(initial_lr,decay_steps=100000,decay_rate=0.96,staircase=True)


def main():

    with tf.device('/GPU:0'):

    
    
        datagen=ImageDataGenerator(width_shift_range=0.1,height_shift_range=0.1,horizontal_flip=True,rotation_range=6)
        mymodel = modelGA()
        history = mymodel.fit(datagen.flow(train_images,
                    train_labels,batch_size=BATCH_SIZE),
                    steps_per_epoch=int(len(train_labels)/BATCH_SIZE),
                    epochs=EPOCHS,
                    callbacks=[cp_callback1],
                    validation_data =(val_images,val_labels),
                    validation_steps=int(len(val_labels)/BATCH_SIZE))
        #tf.saved_model.save(mymodel,"tmp/model/1/")
        mymodel.save('models/age_gender_3.h5')
        results = mymodel.evaluate(test_images,test_labels)
        print("test loss, test acc:", results)
        acc = history.history['accuracy']
        val_acc = history.history['val_accuracy']

        loss=history.history['loss']
        val_loss=history.history['val_loss']

        epochs_range = range(10)

        plt.figure(figsize=(8, 8))
        plt.subplot(1, 2, 1)
        plt.plot(epochs_range, acc, label='Training Accuracy')
        plt.plot(epochs_range, val_acc, label='Validation Accuracy')
        plt.legend(loc='lower right')
        plt.title('Training and Validation Accuracy')

        plt.subplot(1, 2, 2)
        plt.plot(epochs_range, loss, label='Training Loss')
        plt.plot(epochs_range, val_loss, label='Validation Loss')
        plt.legend(loc='upper right')
        plt.title('Training and Validation Loss')
        plt.show()



if __name__=="__main__" :

    main()


