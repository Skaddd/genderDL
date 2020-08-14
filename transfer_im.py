import functools
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from matplotlib import gridspec
from PIL import Image

print("TF Version: ", tf.__version__)
print("TF-Hub version: ", hub.__version__)
print("Eager mode enabled: ", tf.executing_eagerly())

def crop_center(image):
  """Returns a cropped square image."""
  shape = image.shape
  new_shape = min(shape[1], shape[2])
  offset_y = max(shape[1] - shape[2], 0) // 2
  offset_x = max(shape[2] - shape[1], 0) // 2
  image = tf.image.crop_to_bounding_box(
      image, offset_y, offset_x, new_shape, new_shape)
  return image


@functools.lru_cache(maxsize=None)
def load_image(image, image_size=(256, 256), preserve_aspect_ratio=True):

  """Loads and preprocesses images."""
  # Cache image file locally.
  
  # Load and convert to float32 numpy array, add batch dimension, and normalize to range [0, 1].
  img = plt.imread(image).astype(np.float32)
  img = np.expand_dims(img,axis=0)

  if img.max() > 1.0:
    img = img / 255.
  if len(img.shape) == 4:
    img =img[:,:,:,:3]


  img = crop_center(img)
  img = tf.image.resize(img, image_size, preserve_aspect_ratio=True)
  return img


def styleT(con_image,sty_image):

  output_image_size = 512  

  content_img_size = (output_image_size, output_image_size)
  # The style prediction model was trained with image size 256 and it's the 
  # recommended image size for the style image (though, other sizes work as 
  # well but will lead to different results).
  style_img_size = (256, 256)  # Recommended to keep it at 256.

  content_image = load_image(con_image, content_img_size)
  style_image = load_image(sty_image, style_img_size)


  style_image = tf.nn.avg_pool(style_image, ksize=[3,3], strides=[1,1], padding='SAME')



  with tf.device('/CPU:0'):
    hub_handle = 'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'
    hub_module = hub.load(hub_handle)

    outputs = hub_module(tf.constant(content_image), tf.constant(style_image))
    stylized_image = outputs[0]
    plt.imsave('transfer.jpg',stylized_image[0].numpy())


    """
    plt.figure()
    plt.axis('off')
    plt.imshow(stylized_image[0])
    plt.show()
    """





if __name__ =="__main__":

  con_image = 'pictures/turtle.jpg'
  sty_image = 'pictures/flames.jpg'
  styleT(con_image,sty_image)