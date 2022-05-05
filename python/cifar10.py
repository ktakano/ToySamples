import pickle
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Download cifar-10-python.tar.gz from the following site.
# https://www.cs.toronto.edu/~kriz/cifar.html

def unpickle(file):

    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

label_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

data1 = unpickle("dataset/cifar-10-batches-py/" + "data_batch_1")

img1 = data1[b'data']
label1 = data1[b'labels']

#print (label1[0])
#print (img1[0].reshape(3, 32, 32))

label = label1[0]
image = img1[0].reshape(3, 32, 32)

image = image.transpose(1,2,0)

# Display the image
# matplotlib
plt.imshow(image)
plt.title(label_names[label])
plt.show()

# PIL
pil_img = Image.fromarray(np.uint8(image))
pil_img.show()

print("Done.")
