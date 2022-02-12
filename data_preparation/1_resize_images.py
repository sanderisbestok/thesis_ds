import os
import shutil
from PIL import Image

# Delete folder if it exists
if (os.path.isdir("./resized")):
    shutil.rmtree("./resized")

os.mkdir("./resized")

for subdir, dirs, files in os.walk("./11k_hands/Hands/"):
    for file in files:
        image = Image.open("./11k_hands/Hands/" + file)
        resized_image = image.resize((160,160))
        resized_image.save("./resized/" + file)
        