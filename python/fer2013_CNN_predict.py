import numpy as np # linear algebra
import matplotlib.pyplot as plt
from numpy import asarray

import tensorflow as tf
from tensorflow import keras

# 保存した学習済モデルの読み込み
model = keras.models.load_model("fer2013_CNN-v2.h5")
#model.compile(loss='categorical_crossentropy', metrics=['accuracy'],optimizer='adam')
#model.summary()

model.summary()