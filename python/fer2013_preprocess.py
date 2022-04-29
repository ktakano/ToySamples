import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype


def transform_x(data_frame):
    data_frame = data_frame['pixels']  # Selecting Pixels Only
    data_frame = data_frame.values  # Converting from Panda Series to Numpy Ndarray
    data_frame = data_frame.reshape((data_frame.shape[0], 1))  # Reshape for the subsequent operation
    # convert pixels from string to ndarray
    data_frame = np.apply_along_axis(lambda x: np.array(x[0].split()).astype(dtype=float), 1, data_frame)
    data_frame = data_frame.reshape((data_frame.shape[0], 48, 48, 1))  # reshape to NxHxWxC
    return data_frame


def transform_y(data_frame):
    data_frame = data_frame['emotion']  # Selecting Emotion Only
    emotion_type = CategoricalDtype(categories=list(range(7)))
    data_frame = data_frame.astype(emotion_type)
    data_frame = pd.get_dummies(data_frame)
    data_frame = data_frame.values
    return data_frame

df = pd.read_csv("fer2013.csv")

train_x = df.loc[df['Usage'].isin(['Training', 'PublicTest']), ['pixels']]
train_y = df.loc[df['Usage'].isin(['Training', 'PublicTest']), ['emotion']]
train_x = transform_x(train_x)
train_y = transform_y(train_y)

test_x = df.loc[df['Usage'] == 'PrivateTest', ['pixels']]
test_y = df.loc[df['Usage'] == 'PrivateTest', ['emotion']]
test_x = transform_x(test_x)
test_y = transform_y(test_y)

np.save('train_x', train_x)
np.save('train_y', train_y)
np.save('test_x', test_x)
np.save('test_y', test_y)
