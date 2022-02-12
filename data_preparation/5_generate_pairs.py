# Van elke map maximaal 20 random afbeeldingen pakken
import os
import random
import itertools
import shutil

# Delete folder if it exists
# if (os.path.isdir('./pairs')):
    # shutil.rmtree('./pairs')

# Create folder
# os.mkdir('./pairs')

for set in ['test', 'val']: 

    filesPerDir = {}

    # Loop over the test directory
    for rootdir, subdirs, files in os.walk('./age/old_test/' + set):

        # Place the files per directory in a dict
        if os.path.basename(rootdir):
            filesPerDir[os.path.basename(rootdir)] = files 

    allFiles = []

    # Create an array of tuples with the combinations of directory and name
    for dir in filesPerDir:
        for file in filesPerDir[dir]:
            allFiles.append((dir, file))

    equalPairs = []
    unequalPairs = []

    # Make all the pairs
    for pair in itertools.combinations(allFiles,2):
        
        # Pair of equal person
        if pair[0][0] == pair[1][0]:
            equalPairs.append(pair)
        else:
            unequalPairs.append(pair)
        
    # Shuffle the arrays    
    random.Random(1200).shuffle(equalPairs)
    random.Random(1200).shuffle(unequalPairs)

    # Create the file
    with open('./pairs/age_old_test_' + set + '.txt', 'w+') as f:

        for pair in equalPairs[:6000]:
            f.write(pair[0][0] + ' ' + pair[0][1] + ' ' + pair[1][1] + '\n')

        for pair in unequalPairs[:6000]:
            f.write(pair[0][0] + ' ' + pair[0][1] + ' ' + pair[1][0] + ' ' + pair[1][1] + '\n')


    