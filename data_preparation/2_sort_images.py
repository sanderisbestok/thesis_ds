import pandas as pd
import os
import shutil

# Read in the annotations
df = pd.read_csv("./11k_hands/HandInfo.txt")

# Sort by id column
grouped = df.groupby('id')

# Delete folder if it exists
if (os.path.isdir("./sorted")):
    shutil.rmtree("./sorted")

os.mkdir("./sorted")

# Create and sort folders based on person identifier
for name, group in grouped:
    for index, row in group.iterrows():

        # Create folders, and copy files.
        # Check if we have accessories, nailPolish or irregularities. If so don't add them.      
        if not (row["accessories"] or row["nailPolish"] or row["irregularities"]):
            if not (os.path.isdir("./sorted/" + str(name))):
                os.mkdir("./sorted/" + str(name))

            shutil.copyfile("./resized/" + row["imageName"], "./sorted/" + str(name) + "/" + row["imageName"])


