import pickle
import os
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

networks = ['age_old', 'gender_male', 'gender_female', 'skin_color_dark', 'skin_color_very_fair']

fprs = {}
tprs = {}

for network in networks:
    with open('./results/' + network + '_fpr.pickle', "rb") as fp:   #Pickling
        fprs[network] = pickle.load(fp)
    with open('./results/' +  network +  '_tpr.pickle', "rb") as fp:   #Pickling
        tprs[network] = pickle.load(fp)        

ax = plt.gca()

fpr = fprs['skin_color_dark']
tpr = tprs['skin_color_dark']
roc_auc = metrics.auc(fpr, tpr)
fnr = 1 - tpr
eer = fpr[np.nanargmin(np.absolute((fnr - fpr)))]
plt.plot(fpr,tpr,label="Experiment skinColour_1, AUC=" + str(round(roc_auc,4)) + ', EER=' + str(round(eer,4)),color='orange')

fpr = fprs['skin_color_very_fair']
tpr = tprs['skin_color_very_fair']
roc_auc = metrics.auc(fpr, tpr)
fnr = 1 - tpr
eer = fpr[np.nanargmin(np.absolute((fnr - fpr)))]
plt.plot(fpr,tpr,label="Experiment skinColour_2, AUC=" + str(round(roc_auc,4)) + ', EER=' + str(round(eer,4)),color='grey')

fpr = fprs['gender_female']
tpr = tprs['gender_female']
roc_auc = metrics.auc(fpr, tpr)
fnr = 1 - tpr
eer = fpr[np.nanargmin(np.absolute((fnr - fpr)))]
plt.plot(fpr,tpr,label="Experiment Gender_1, AUC=" + str(round(roc_auc,4)) + ', EER=' + str(round(eer,4)),color='pink')

fpr = fprs['gender_male']
tpr = tprs['gender_male']
roc_auc = metrics.auc(fpr, tpr)
fnr = 1 - tpr
eer = fpr[np.nanargmin(np.absolute((fnr - fpr)))]
plt.plot(fpr,tpr,label="Experiment Gender_2, AUC=" + str(round(roc_auc,4)) + ', EER=' + str(round(eer,4)),color='cyan')

fpr = fprs['age_old']
tpr = tprs['age_old']
roc_auc = metrics.auc(fpr, tpr)
fnr = 1 - tpr
eer = fpr[np.nanargmin(np.absolute((fnr - fpr)))]
plt.plot(fpr,tpr,label="Experiment Age_1, AUC=" + str(round(roc_auc,4)) + ', EER=' + str(round(eer,4)),color='purple')

ax.set(xlabel='False Positive Rate', ylabel='True Positive Rate')
ax.legend()

plt.savefig('./results/' + network + '.png')
plt.clf()


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