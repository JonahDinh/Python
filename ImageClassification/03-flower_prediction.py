from pathlib import Path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras import layers
from keras import Sequential
import tensorflow as tf

# Define some constants:

IMG_HEIGHT = 180
IMG_WIDTH = 180
CLASSES = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']

model_path = Path("ImageClassification/Data/models/flower_model.keras")
flower_model = keras.models.load_model(model_path)
print(flower_model.summary())

while True:
    flower_file = input("Enter the path of an image you'd like us to identify:\n")
    flower_file_path = Path(flower_file)
    if not flower_file_path.is_file():
        print(f"{flower_file} is not a file. Please enter the path to the image you want to test.")
        continue
    # We'll use a keras utility to load in the file:
    try:
        img = keras.utils.load_img(flower_file_path, target_size=(IMG_HEIGHT, IMG_WIDTH))
    except Exception:
        raise
    print("Predicting...")

    # We want to transform the image into a numpy array
    img_array = np.array(img)
    # Keras also expects us to be passing in an array of images, not just
    # a single image! So let •s wrap that image in a 4th dimension
    
    img_array = img_array.reshape((1,) + (IMG_HEIGHT, IMG_WIDTH, 3))

    predictions = flower_model.predict(img_array)
    print(predictions)

    # Let's transform it into a "score"
    score = tf.nn.softmax(predictions[0]) * 100
    print(score)

    predicted_class = CLASSES[np.argmax(score)]
    confidence = round(np.max(score))
    print(f"This image mst likely belongs to {predicted_class} with a {confidence}% confidence.")