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

        if os.path.basename(rootdir).startswith('perm_1'):
            color=['red']
        if os.path.basename(rootdir).startswith('perm_2'):
            color=['green']
        if os.path.basename(rootdir).startswith('perm_3'):
            color=['blue']
        if os.path.basename(rootdir).startswith('perm_4'):
            color=['black']

        df.plot(kind='line',x=0,y=1, ylim=(0,1),ax=ax, legend=False, color=color)
        ax.set(xlabel='Epoch')
        ax.set(ylabel='Accuracy')
        plt.savefig('./accuracy_graphs/' + os.path.basename(rootdir) + '.png')
        plt.clf()
        # plt.show()