# Hand based verification using deep learning

## Repository description
This repository is made for the Thesis of Sander Hansen for the Master Information Studies with the Data Science Track. 

The code found in this repository is the code used for this thesis. Next to the code you will find some instructions on how to use certain scripts.

## Data preparation
- [This](data_preparation/eda.py) can be used to replicate the exploratory data analysis
- The 11K hands dataset can be found [here](https://sites.google.com/view/11khands).
- Place the dataset in ROOT/dataset/11k_hands/
- Execute script [1](data_preparation/1_resize_images.py) to resize the images
- Execute script [2](data_preparation/2_sort_images.py) to place the images in a folder per identity and remove accessories, nailPolish and irregularities
- Execute script [3](data_preparation/3_create_sets.py) create the train, validation and test sets
- Execute script [4](data_preparation/4_create_permutations.py) create the left, right, dorsal and palmar permutations
- Execute script [5](data_preparation/5_generate_pairs.py) use this script to create the test pairs, adjust script and use folder for a permuation in line 19 and 49
- Execute script [6](data_preparation/6_generate_color_groups.py) use this script to create the demographic colour training and test sets
- Execute script [7](data_preparation/7_generate_gender_groups.py) use this script to create the demographic gender training and test sets
- Execute script [8](data_preparation/_generate_age_groups.py) use this script to create the demographic gender training and test sets
- Execute script [4](data_preparation/5_generate_pairs.py) use this script to create the test pairs, adjust script and use folder for a permuation in line 19 and 49

## Facenet
These instructions are made to work with the LISA cluster.
- Use the FaceNet version which can be found [here](facenet) 
- Install dependencies from [requirements.txt](facenet/requirements.txt)
- Set the pythonpath ``export PYTHONPATH=[...]/facenet/src``

## Experiments
All commands to start the jobs for training and testing can be found in the [Job Scripts](job_scripts) folder
