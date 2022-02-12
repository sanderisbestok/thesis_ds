import pandas as pd
import os
import shutil
import random
import numpy as np

# Read in the annotations
df = pd.read_csv("./11k_hands/HandInfo.txt")

# Sort by id column
grouped = df.groupby('id')

# Delete folder if it exists
if (os.path.isdir("./age")):
    shutil.rmtree("./age")

os.makedirs("./age/old_test/")
os.makedirs("./age/old_test/train")
os.makedirs("./age/old_test/val")
os.makedirs("./age/old_test/test")

color = {}

# Create and sort folders based on person identifier and skin color
for name, group in grouped:
    for index, row in group.iterrows():
        # Create folders, and copy files.
        # Check if we have accessories, nailPolish or irregularities. If so don't add them.      
        if not (row["accessories"] or row["nailPolish"] or row["irregularities"]):
            
            if row['age'] <= 30:
                if (row['aspectOfHand']) == "dorsal left":
                    if not (os.path.isdir("./age/old_test/train/" + str(name) + "_left_dorsal")):
                        os.mkdir("./age/old_test/train/" + str(name) + "_left_dorsal")

                    shutil.copyfile("./resized/" + row["imageName"], "./age/old_test/train/" + str(name) + "_left_dorsal/" + row["imageName"])

                if (row['aspectOfHand']) == "dorsal right":
                    if not (os.path.isdir("./age/old_test/train/" + str(name) + "_right_dorsal")):
                        os.mkdir("./age/old_test/train/" + str(name) + "_right_dorsal")

                    shutil.copyfile("./resized/" + row["imageName"], "./age/old_test/train/" + str(name) + "_right_dorsal/" + row["imageName"])

                if (row['aspectOfHand']) == "palmar right":
                    if not (os.path.isdir("./age/old_test/train/" + str(name) + "_right_palmar")):
                        os.mkdir("./age/old_test/train/" + str(name) + "_right_palmar")

                    shutil.copyfile("./resized/" + row["imageName"], "./age/old_test/train/" + str(name) + "_right_palmar/" + row["imageName"])

                if (row['aspectOfHand']) == "palmar left":
                    if not (os.path.isdir("./age/old_test/train/" + str(name) + "_left_palmar")):
                        os.mkdir("./age/old_test/train/" + str(name) + "_left_palmar")

                    shutil.copyfile("./resized/" + row["imageName"], "./age/old_test/train/" + str(name) + "_left_palmar/" + row["imageName"])

            elif row['age'] >= 60:
                if (row['aspectOfHand']) == "dorsal left":
                    if not (os.path.isdir("./age/old_test/test/" + str(name)+ "_left_dorsal")):
                        os.mkdir("./age/old_test/test/" + str(name) + "_left_dorsal")

                    shutil.copyfile("./resized/" + row["imageName"], "./age/old_test/test/" + str(name) + "_left_dorsal/" + row["imageName"])

                if (row['aspectOfHand']) == "dorsal right":
                    if not (os.path.isdir("./age/old_test/test/" + str(name)+ "_right_dorsal")):
                        os.mkdir("./age/old_test/test/" + str(name) + "_right_dorsal")

                    shutil.copyfile("./resized/" + row["imageName"], "./age/old_test/test/" + str(name) + "_right_dorsal/" + row["imageName"])

                if (row['aspectOfHand']) == "palmar right":
                    if not (os.path.isdir("./age/old_test/test/" + str(name)+ "_right_palmar")):
                        os.mkdir("./age/old_test/test/" + str(name) + "_right_palmar")

                    shutil.copyfile("./resized/" + row["imageName"], "./age/old_test/test/" + str(name) + "_right_palmar/" + row["imageName"])

                if (row['aspectOfHand']) == "palmar left":
                    if not (os.path.isdir("./age/old_test/test/" + str(name)+ "_left_palmar")):
                        os.mkdir("./age/old_test/test/" + str(name) + "_left_palmar")

                    shutil.copyfile("./resized/" + row["imageName"], "./age/old_test/test/" + str(name) + "_left_palmar/" + row["imageName"])


for group in ['./age/old_test/']: 
    # Get the folders
    dirlist = [ item for item in os.listdir(group + "train") if os.path.isdir(os.path.join(group + "train", item)) ]

    # Shuffle the folders with a seed
    random.Random(1200).shuffle(dirlist)

    # Split in train and test set
    train, val = np.split(dirlist, [int(len(dirlist)*0.8)])

    # Move the folders from sorted to correct set folder
    for folder in val:
        shutil.move(group + "train/" + folder, group + 'val/' + folder)

            
            



