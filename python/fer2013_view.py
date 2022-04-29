import numpy as np
import matplotlib.pyplot as plt

X_train = np.load("train_x.npy")
X_test = np.load("test_x.npy")
y_train = np.load("train_y.npy")
y_test = np.load("test_y.npy")

shape_x = 48
shape_y = 48
nRows,nCols,nDims = X_train.shape[1:]
input_shape = (nRows, nCols, nDims)
classes = np.unique(y_train)
nClasses = len(classes)

plt.figure(figsize=(12,8))
plt.imshow(np.mean(X_train, axis=0).reshape(48,48))
plt.title("Average face")
#plt.show()

dic = { 0: "Angry",
       1: "Disgust",
       2:"Fear",
       3:"Happy",
       4:"Sad",
       5:"Surprise",
       6:"Neutral"}

fig, axes = plt.subplots(nrows=1, ncols=7, figsize=(22, 8))

for i, ax in enumerate(axes):
    ax.imshow(np.mean(X_train[np.argmax(y_train, axis=1) == i], axis=0).reshape(48,48))
    ax.set_title(dic[i])

plt.show()
