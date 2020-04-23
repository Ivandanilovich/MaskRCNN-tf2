import tensorflow as tf
from ResNet import resnet_graph

input_image = tf.keras.layers.Input((320, 320, 3))
x = resnet_graph(input_image, False)
model = tf.keras.Model(input_image,x)
d = 4
