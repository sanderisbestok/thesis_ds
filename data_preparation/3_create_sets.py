import os
import shutil
import random
import numpy as np

# Get the folders
dirlist = [ item for item in os.listdir("./sorted") if os.path.isdir(os.path.join("./sorted", item)) ]

# Shuffle the folders with a seed
random.Random(1200).shuffle(dirlist)

# Split in train and test set
train, val, test = np.split(dirlist, [int(len(dirlist)*0.8),int(len(dirlist)*0.9)])

# Delete folder if it exists, then create it again
if (os.path.isdir("./sets")):
    shutil.rmtree("./sets")

# Sets 
os.mkdir("./sets")
os.mkdir("./sets/train")
os.mkdir("./sets/val")
os.mkdir("./sets/test")

# Move the folders from sorted to correct set folder
for folder in train:
    shutil.copytree("./sorted/" + folder, "./sets/train/" + folder)

for folder in val:
    shutil.copytree("./sorted/" + folder, "./sets/val/" + folder)

for folder in test:
    shutil.copytree("./sorted/" + folder, "./sets/test/" + folder)
