import pickle
import os
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

perms = ['perm_1_', 'perm_2_', 'perm_3_', 'perm_4_']
networks = ['classifier_nopretrain', 'classifier_pretrain', 'triplet_nopretrain', 'triplet_pretrain']

fprs = defaultdict(dict)
tprs = defaultdict(dict)


for perm in perms:
    for network in networks:
        with open('./results/' + perm + network + '_fpr.pickle', "rb") as fp:   #Pickling
            fprs[perm][network] = pickle.load(fp)
        with open('./results/' +  perm + network +  '_tpr.pickle', "rb") as fp:   #Pickling
            tprs[perm][network] = pickle.load(fp)        
i = 1

for network in networks:
    ax = plt.gca()

    fpr = fprs['perm_1_'][network]
    tpr = tprs['perm_1_'][network]
    roc_auc = metrics.auc(fpr, tpr)
    fnr = 1 - tpr
    eer = fpr[np.nanargmin(np.absolute((fnr - fpr)))]
    print(str(round(eer,4)))
    plt.plot(fpr,tpr,label="Experiment 1_"+str(i)+", AUC=" + str(round(roc_auc,4)) + ', EER=' + str(round(eer,4)),color='red')

    fpr = fprs['perm_2_'][network]
    tpr = tprs['perm_2_'][network]
    roc_auc = metrics.auc(fpr, tpr)
    fnr = 1 - tpr
    eer = fpr[np.nanargmin(np.absolute((fnr - fpr)))]
    plt.plot(fpr,tpr,label="Experiment 2_"+str(i)+", AUC=" + str(round(roc_auc,4)) + ', EER=' + str(round(eer,4)),color='green')

    fpr = fprs['perm_3_'][network]
    tpr = tprs['perm_3_'][network]
    roc_auc = metrics.auc(fpr, tpr)
    fnr = 1 - tpr
    eer = fpr[np.nanargmin(np.absolute((fnr - fpr)))]
    plt.plot(fpr,tpr,label="Experiment 3_"+str(i)+", AUC=" + str(round(roc_auc,4)) + ', EER=' + str(round(eer,4)),color='blue')

    fpr = fprs['perm_4_'][network]
    tpr = tprs['perm_4_'][network]
    roc_auc = metrics.auc(fpr, tpr)
    fnr = 1 - tpr
    eer = fpr[np.nanargmin(np.absolute((fnr - fpr)))]
    plt.plot(fpr,tpr,label="Experiment 4_"+str(i)+", AUC=" + str(round(roc_auc,4)) + ', EER=' + str(round(eer,4)),color='black')


    ax.set(xlabel='False Positive Rate', ylabel='True Positive Rate')
    ax.legend()

    plt.savefig('./results/' + network + '.png')
    plt.clf()

    i += 1




# print('Equal Error Rate (EER): %1.3f' % eer)

# # Loop over the test directory
# for rootdir, subdirs, files in os.walk('./results/'):

#     for file in sorted(files):
#         # global fpr
#         # global tpr
#         # fpr = 0
#         # tpr = 0

#         if file.endswith('fpr.pickle'):
#             print(file)
#             with open('./results/' +  file, "rb") as fp:   #Pickling
#                 fpr = pickle.load(fp)
#             with open('./results/' +  file[:len(file) - 10] + 'tpr.pickle', "rb") as fp:   #Pickling
#                 tpr = pickle.load(fp)


#             roc_auc = metrics.auc(fpr, tpr)
#             display = metrics.RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc)
#             display.plot(color='darkorange')
#             plt.savefig('./results/' + file[:len(file)-11] + '.png')

#             fnr = 1 - tpr
#             eer = fpr[np.nanargmin(np.absolute((fnr - fpr)))]

#             print('Equal Error Rate (EER): %1.3f' % eer)