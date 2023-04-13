from models.mynet_qnn import mynet_qnn_v1
from models.mynet import mynet
from models.vgg16_qnn import vgg16_qnn_v1
from models.vgg16 import vgg16
from models.lenet5_qnn import lenet5_qnn_v1
from models.lenet5 import lenet5
from tensorflow.keras import datasets, layers, models
import tensorflow as tf
import os

# Set the GPU index you want to use (0-based)
os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'

# Define the input shape of the network
input_shape = (28, 28, 1)
# Define the number of classes
num_classes = 10

model = mynet_qnn_v1(input_shape=input_shape, num_classes=num_classes)

# Load the MNIST dataset and preprocess the data
(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()

# Reshape the data to match the input shape of the model
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# Convert the labels to one-hot encoded vectors
y_train = tf.keras.utils.to_categorical(y_train, num_classes)
y_test = tf.keras.utils.to_categorical(y_test, num_classes)

# TensorBoard
log_dir = "logs/fit"
tb_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

# Train the model on the training data
model.fit(x_train, y_train, batch_size=128, epochs=30,
          validation_data=(x_test, y_test),
          callbacks=[tb_callback])

model.save_weights('qnn.h5')
