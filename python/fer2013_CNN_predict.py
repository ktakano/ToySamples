import numpy as np # linear algebra
import matplotlib.pyplot as plt
from numpy import asarray
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import tensorflow as tf
from tensorflow import keras

# 保存した学習済モデルの読み込み
model = keras.models.load_model("fer2013_CNN-v2.h5")
#model.summary()


df = pd.read_csv("fer2013.csv")
output_label = ['Anger', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

#Convert the df['pixels'] str type to array and reshape
def string2array(x):
  return np.array(x.split(' ')).reshape(48, 48, 1).astype('float32')

X= df['pixels'].apply(lambda x: string2array(x))
X = np.array(X)
X = np.stack(X, axis = 0)
X = X/255.0
y = np.array(df['emotion'])

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size = 0.25, shuffle = True)

predictions = model.predict(x_test)

prediction = predictions[1].argmax()
print(prediction)
print(output_label[prediction])

img = x_test[1].reshape(48,48)
plt.figure()
plt.title(output_label[y_test[1].argmax()])
plt.imshow(img, cmap = 'gray')

plt.show()
