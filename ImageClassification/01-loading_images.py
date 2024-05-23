#%%

from pathlib import Path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras import layers
from keras import Sequential

# Create a path
cat_dir = Path("ImageClassification/Data/cat/")
print(cat_dir.absolute())
cat_files = list(cat_dir.glob("*.png"))

print(f"cat_files list: {cat_files}")

print(f"There are {len(cat_files)} cat pictures:")
#%%



cat_img = Image.open(str(cat_files[0]))

print(f"Our first cat image is size {cat_img.size}. It's mode is {cat_img.mode}, and it's format is {cat_img.format}")

plt.imshow(cat_img)
plt.show()


# %%
cat_array = np.array(cat_img)
print(cat_array)
print(f"The shape of the cat array is {cat_array.shape}")

new_cat_array = np.where(cat_array < 100 , 255, cat_array)
new_cat_image = Image.fromarray(new_cat_array)
plt.imshow(new_cat_image)
plt.show()
print(keras.backend.image_data_format())
rolled_cat_array = np.rollaxis(new_cat_array, 2, 0)


# %%

mutated_cat_array = new_cat_array * 0.33
mutated_cat_array = mutated_cat_array.astype(np.uint8)
mutated_cat_image = Image.fromarray(mutated_cat_array)
plt.imshow(mutated_cat_image)
plt.show()

mutated_cat_file = Path("ImageClassification/Data/mutated/cat1.png")
mutated_cat_file.parent.mkdir(exist_ok=True)
mutated_cat_image.save(mutated_cat_file, "PNG")

# %%


cat_img = Image.open(str(cat_files[0]))
cat_array = np.array(cat_img)


# %%



cat_images_array = cat_array.reshape((1,) + cat_array.shape)
print(f"Cat_images_array's shape is {cat_images_array.shape}")

image_augmentation = Sequential(
    [
        layers.RandomFlip("horizontal", input_shape=(cat_array.shape)),
        layers.RandomRotation(0.1),
        layers.RandomZoom(0.1)
    ]
)

for i in range(10):
    print(f"Image #{i}:")
    augmented_images = image_augmentation(cat_images_array)

    augmented_image = augmented_images[0]
    plt.imshow(augmented_image.numpy().astype(np.uint8))
    plt.show()



# %%
