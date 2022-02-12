# perm_1 = left + right + dorsal + Palmar
# perm_2 = dorsal + Palmar (left + right apart)
# perm_3 = left + right (dorsal + Palmar apart)
# perm_4 = Alles apart

# Beste met huidskleur en beste met gender?

import pandas as pd
import os
import shutil

# Read in the annotations
df = pd.read_csv('./11k_hands/HandInfo.txt')

# Delete folder if it exists
if (os.path.isdir('./perms')):
    shutil.rmtree('./perms')

# Create and sort folders based on person identifier
for set in ['train/', 'test/', 'val/']: 
    shutil.copytree('./sets/' + set, './perms/perm_1/' + set)

    for rootdir, subdirs, _ in os.walk('./sets/' + set):
        for dir in subdirs:

            # Get the folder name, which is the id of the subject
            subject = int(dir)

            # Iterate through the files        
            files = os.listdir(os.path.join(rootdir, dir))

            for file in files:
                rowDF = df.loc[(df['id'] == subject) & (df['imageName'] == file)]
                row = rowDF.iloc[0] 

                # Split left and right
                if (row['aspectOfHand'].split(' ')[1]) == "left":
                    os.makedirs("./perms/perm_2/" + set + dir + "_left/", exist_ok = True)
                    shutil.copyfile(os.path.join(rootdir, dir, file), "./perms/perm_2/" + set + dir + "_left/" + file)

                    # Split dorsal and palmar
                    if (row['aspectOfHand'].split(' ')[0]) == "dorsal":
                        os.makedirs("./perms/perm_3/" + set + dir + "_dorsal/", exist_ok = True)
                        shutil.copyfile(os.path.join(rootdir, dir, file), "./perms/perm_3/" + set + dir + "_dorsal/" + file)

                        os.makedirs("./perms/perm_4/" + set + dir + "_left_dorsal/", exist_ok = True)
                        shutil.copyfile(os.path.join(rootdir, dir, file), "./perms/perm_4/" + set + dir + "_left_dorsal/" + file)

                    elif (row['aspectOfHand'].split(' ')[0]) == "palmar":
                        os.makedirs("./perms/perm_3/" + set + dir + "_palmar/", exist_ok = True)
                        shutil.copyfile(os.path.join(rootdir, dir, file), "./perms/perm_3/" + set + dir + "_palmar/" + file)

                        os.makedirs("./perms/perm_4/" + set + dir + "_left_palmar/", exist_ok = True)
                        shutil.copyfile(os.path.join(rootdir, dir, file), "./perms/perm_4/" + set + dir + "_left_palmar/" + file)



                elif (row['aspectOfHand'].split(' ')[1]) == "right":
                    os.makedirs("./perms/perm_2/" + set + dir + "_right/", exist_ok = True)
                    shutil.copyfile(os.path.join(rootdir, dir, file), "./perms/perm_2/" + set + dir + "_right/" + file)

                    # Split dorsal and palmar
                    if (row['aspectOfHand'].split(' ')[0]) == "dorsal":
                        os.makedirs("./perms/perm_3/" + set + dir + "_dorsal/", exist_ok = True)
                        shutil.copyfile(os.path.join(rootdir, dir, file), "./perms/perm_3/" + set + dir + "_dorsal/" + file)

                        os.makedirs("./perms/perm_4/" + set + dir + "_right_dorsal/", exist_ok = True)
                        shutil.copyfile(os.path.join(rootdir, dir, file), "./perms/perm_4/" + set + dir + "_right_dorsal/" + file)

                    elif (row['aspectOfHand'].split(' ')[0]) == "palmar":
                        os.makedirs("./perms/perm_3/" + set + dir + "_palmar/", exist_ok = True)
                        shutil.copyfile(os.path.join(rootdir, dir, file), "./perms/perm_3/" + set + dir + "_palmar/" + file)

                        os.makedirs("./perms/perm_4/" + set + dir + "_right_palmar/", exist_ok = True)
                        shutil.copyfile(os.path.join(rootdir, dir, file), "./perms/perm_4/" + set + dir + "_right_palmar/" + file)
