# -*- coding: utf-8 -*-
"""use_saved_mnist_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w-_7Ntprv4QX8wvbRLT0NtDmk9Skb1S8
"""

!ls

!wget https://github.com/futurexskill/ml-model-deployment/raw/main/mnistmodel.zip

!ls

!unzip mnistmodel.zip

!ls

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import RMSprop
import matplotlib.pyplot as plt

(mnist_train_images, mnist_train_labels), (mnist_test_images, mnist_test_labels) = mnist.load_data()

train_images = mnist_train_images.reshape(60000, 784)
test_images = mnist_test_images.reshape(10000, 784)
train_images = train_images.astype('float32')
test_images = test_images.astype('float32')
train_images /= 255
test_images /= 255

train_labels = keras.utils.to_categorical(mnist_train_labels, 10)
test_labels = keras.utils.to_categorical(mnist_test_labels, 10)

from tensorflow.keras.models import load_model

mnist_new_model = load_model('image_classifier_model/1/')

test_image = test_images[5233,:].reshape(1,784)
predicted_cat = mnist_new_model.predict(test_image).argmax()
label = test_labels[5233].argmax()
plt.title('Prediction: %d Label: %d' % (predicted_cat, label))
plt.imshow(test_image.reshape([28,28]), cmap=plt.get_cmap('gray_r'))
plt.show()

test_image = test_images[3245,:].reshape(1,784)
predicted_cat = mnist_new_model.predict(test_image).argmax()
label = test_labels[3245].argmax()
plt.title('Prediction: %d Label: %d' % (predicted_cat, label))
plt.imshow(test_image.reshape([28,28]), cmap=plt.get_cmap('gray_r'))
plt.show()

