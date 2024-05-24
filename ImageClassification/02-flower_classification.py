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
data_dir = Path("ImageClassification/Data/flower_images/")
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
    plt.imshow(my_image)
    plt.show()

#%%
# There's a lot of images in here. Let's use a keras utility to load it in as a dataset
# It'll take in the whole directory in just a couple of lines of code.
# We definitely could do this from scratch, using tensorflow's data module, if we wanted
# finer grained control

# Let's define some parameters:
BATCH_SIZE = 32
# Note that our sample images are not uniform in dimension. Let's load them all in as the same size
IMG_HEIGHT = 180
IMG_WIDTH = 180

# We're going to split the data into validation data and training data. We'll use 20% of the data for validation.
VALIDATION_SPLIT = 0.2

# Create our datasets
train_ds = keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=VALIDATION_SPLIT,
    subset="training",
    seed=123,
    image_size=(IMG_WIDTH,IMG_HEIGHT),
    batch_size=BATCH_SIZE
)

val_ds = keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=VALIDATION_SPLIT,
    subset="validation",
    seed=123,
    image_size=(IMG_WIDTH,IMG_HEIGHT),
    batch_size=BATCH_SIZE
)

# image_dataset_from_directory will automatically use the directories as "class names" which is usually
# what we want
class_names = train_ds.class_names
num_classes = len(class_names)
print(f"We have {num_classes} classes:")
print(class_names)

#%%
# Let's visualize some of the data loaded in, by displaying the first nine images
# from the training dataset:
plt.figure(figsize=(10,10))
# We'll take 1 batch of 32 images from our dataset:
for images, labels in train_ds.take(1):
    print("One image batch:")
    print(images.shape)
    print("One label batch:")
    print(labels.shape)
    for i in range(9):
        ax = plt.subplot(3,3, i+1)
        plt.imshow(images[i].numpy().astype(np.uint8))
        plt.title(class_names[labels[i]])
        plt.axis("off")
    plt.show()

#%%
# When loading in our data we'll want to configure for performance at least some.
# Two important settings for performance:
#   - We'll want to cache data in our dataset to keep some images in memory after they're loaded from disk
#   - We'll want to make sure we're prefetching so we overlap data preprocessing and model execution while training
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

# We're also going to need to standardize the array, RBG channel values run from 0-255. This isn't
# ideal for a neural network! Ideally, we'd have values from 0 to 1. We can use a rescaling layer
# to normalize our values to be in the 0 to 1 range.
normalization_layer = layers.Rescaling(1./255)

# We could apply this layer right nore using Dataset.map, but we'll just throw it in at the start
# of our model instead.

#%%
# Let's do some data augmentation
# Data augmentation generates additional training data from existing examples.
# Keras helpfully provides some pre-processing layers to help us do this:
data_augmentation = Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.1),

])

#Let's visualize this so we can see what types of transforamtions are being applied:
plt.figure(figsize=(10,10))
for images, _ in train_ds.take(1):
    for i in range(3):
        for j in range(1,4):
            augmented_images = data_augmentation(images)
            ax = plt.subplot(3,3,i*3 + j)
            plt.imshow(augmented_images[i].numpy().astype("uint8"))
            plt.axis("off")
plt.show()

#%%
# Our next step is to build the model
model = Sequential([
    layers.Input(shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
    normalization_layer,
    data_augmentation,
    layers.Conv2D(16,3,padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32,3,padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64,3,padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Dropout(0.2),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_classes)
])

# We can now compile it
model.compile(optimizer='adam',
              loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
print(model.summary())

# %%
# Let's train the model:

epochs = 10
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs
)

# %%
# Let's visualize the training results arnd create a plot
# of the loss and accuracy on both the training and validation sets:

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8,8))

plt.subplot(1,2,1)
plt.plot(epochs_range, acc, label="Training Accuracy")
plt.plot(epochs_range, val_acc, label="Validation Accuracy")
plt.legend(loc="upper right")
plt.title("Training and Validation accuracy")

plt.subplot(1,2,2)
plt.plot(epochs_range, loss, label="Training Loss")
plt.plot(epochs_range, val_loss, label="Validation Loss")
plt.legend(loc="upper right")
plt.title("Training and Validation Loss")

plt.show()

# %%
# Let's save our model
model_path = Path("ImageClassification/Data/models/flower_model.keras")
model_path.parent.mkdir(exist_ok=True, parents=True)
model.save(model_path)
# %%
