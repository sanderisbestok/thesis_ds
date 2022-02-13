import pandas as pd
import matplotlib.pyplot as plt
import os

# Loop over the test directory
for rootdir, subdirs, files in os.walk('./logs/facenet/'):
    if rootdir != './logs/facenet/':
        # Read in the annotations
        df = pd.read_csv(rootdir + "/lfw_result.txt", sep='\t', header=None)
        
        # # # gca stands for 'get current axis'
        ax = plt.gca()

        color=['yellow']

        if os.path.basename(rootdir).startswith('skin_color_dark'):
            color=['orange']
        if os.path.basename(rootdir).startswith('skin_color_very_fair'):
            color=['grey']
        if os.path.basename(rootdir).startswith('gender_male'):
            color=['cyan']
        if os.path.basename(rootdir).startswith('gender_female'):
            color=['pink']
        if os.path.basename(rootdir).startswith('age_old'):
            color=['purple']

        df.plot(kind='line',x=0,y=1, ylim=(0,1),ax=ax, legend=False, color=color)
        ax.set(xlabel='Epoch')
        ax.set(ylabel='Accuracy')
        plt.savefig('./accuracy_graphs/' + os.path.basename(rootdir) + '.png')
        plt.clf()
        # plt.show()