#%%
from pathlib import Path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras import layers
from keras import Sequential
import tensorflow as tf

# Configuration
data_dir = Path("./Data/flower_images")
print(data_dir.absolute())



# %%
image_count = len(list(data_dir.glob('*/*.jpg')))
print(f"We have {image_count} .jpg files in our data folder.")

# %%
roses = list((data_dir / "roses").glob("*.jpg"))
print(roses)


for i in range(5):
    print(f"Image #{i}:")
    my_image = Image.open(str(roses[i]))
    plt.imshow()
    plt.show()


# %%

BATCH_SIZE = 32

IMG_HEIGHT = 180
IMG_WIDTH = 180

VALIDAION_SPLIT = 0.2

# Create our dataset

train_ds = keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=VALIDAION_SPLIT,
    subset="training",
    seed=123,
    image_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE
)

val_ds=keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=VALIDAION_SPLIT,
    subset="validation",
    seed=123,
    image_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE
)

class_names = train_ds.class_names
num_classes = len(class_names)
print(f"We have {num_classes} classes:")
print(class_names)


plt.figure(figsize=(10,10))

for images, labels in train_ds.take(1):
    print("One image batch")
    print(images.shape)
    print("One label batch:")
    print(labels.shape)
    for i in range(9):
        ax = plt.subplot(3,3,)
        plt.imshow(images[i].numpy().astype(np.uint8))
        plt.title(class_names[labels[i]])
        plt.axis=("off")
    plt.show()




# %%

AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size = AUTOTUNE)

normalization_layer = layers.Rescaling(1./255, input_shape = (IMG_HEIGHT, IMG_WIDTH, 3))



# %%
model = Sequential([
    normalization_layer
])