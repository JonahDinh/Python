#%%

from pathlib import Path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras import layers
from keras import Sequential

# Create a path
animal_dir = Path("Image Classification/Data/")

animal_files = list(animal_dir.glob("*/*./*.png"))

for animal_file in animal_files:
    animal_name = animal_file.name
    parent_dir = animal_file.parent.name
    print(f"{animal_name}'s parent directroy is {parent_dir}")
    animal_image = Image.open(str(animal_file))

    animal_array = np.array(animal_image)
    bw_animal_array = np.average(animal_array, axis=2)
    plt.imshow(Image.fromarray(bw_animal_array))
    plt.show()

    bw_animal_array = bw_animal_array.astype(np.uint8)
    Path(f"Image Classification/Data/monochrome/{parent_dir}").mkdir(exist_ok=True, parents=True)
    bw_file_path = Path(f"Image Classification/Data/monochrome/{parent_dir}/{animal_name}")
    bw_animal_array.save(bw_file_path, "PNG")
    











#%%