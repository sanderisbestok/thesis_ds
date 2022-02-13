import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

# Read in the annotations
df = pd.read_csv("./11k_hands/HandInfo.txt")

# Show first row
print(df.head(1))

# How many rows
print(df.shape)

# How many subjects
print("Amount of subjects: " + str(len(df.groupby('id'))))

# # How many with:
print("Accessoires: " + str(len((df.loc[(df['accessories'] == 1)].groupby('id')))))
print("nailPolish: "+ str(len((df.loc[(df['nailPolish'] == 1)].groupby('id')))))
print("irregularities: " + str(len((df.loc[(df['irregularities'] == 1)].groupby('id')))))

# # How many images without
noIrr = df.loc[(df['accessories'] == 0) & (df['nailPolish'] == 0) & (df['irregularities'] == 0)]
print("images without the above: " + str(len(noIrr)))
print("subjects without the above: " + str(len(noIrr.groupby('id'))))

# How many images with:
dorsalleft = df.loc[(df['aspectOfHand'] == 'dorsal left') & (df['accessories'] == 0) & (df['nailPolish'] == 0) & (df['irregularities'] == 0)]
dorsalright = df.loc[(df['aspectOfHand'] == 'dorsal right') & (df['accessories'] == 0) & (df['nailPolish'] == 0) & (df['irregularities'] == 0)]
palmarleft = df.loc[(df['aspectOfHand'] == 'palmar left') & (df['accessories'] == 0) & (df['nailPolish'] == 0) & (df['irregularities'] == 0)]
palmarright = df.loc[(df['aspectOfHand'] == 'palmar right') & (df['accessories'] == 0) & (df['nailPolish'] == 0) & (df['irregularities'] == 0)]
print("dorsal left: " + str(len(dorsalleft)))
print("dorsal right: " + str(len(dorsalright)))
print("palmar left: " + str(len(palmarleft)))
print("palmar right: " + str(len(palmarright)))

# How many images with:
print("Very fair: " + str(len(df.loc[(df['skinColor'] == 'very fair') & (df['accessories'] == 0) & (df['nailPolish'] == 0) & (df['irregularities'] == 0)])))
print("Fair: " + str(len(df.loc[(df['skinColor'] == 'fair') & (df['accessories'] == 0) & (df['nailPolish'] == 0) & (df['irregularities'] == 0)])))
print("Medium: " + str(len(df.loc[(df['skinColor'] == 'medium') & (df['accessories'] == 0) & (df['nailPolish'] == 0) & (df['irregularities'] == 0)])))
print("Dark: " + str(len(df.loc[(df['skinColor'] == 'dark') & (df['accessories'] == 0) & (df['nailPolish'] == 0) & (df['irregularities'] == 0)])))

print("subj Very fair: " + str(len((df.loc[(df['skinColor'] == 'very fair') & (df['accessories'] == 0) & (df['nailPolish'] == 0) & (df['irregularities'] == 0)]).groupby('id'))))
print("subj Fair: " + str(len((df.loc[(df['skinColor'] == 'fair') & (df['accessories'] == 0) & (df['nailPolish'] == 0) & (df['irregularities'] == 0)]).groupby('id'))))
print("subj Medium: " + str(len((df.loc[(df['skinColor'] == 'medium') & (df['accessories'] == 0) & (df['nailPolish'] == 0) & (df['irregularities'] == 0)]).groupby('id'))))
print("subj Dark: " + str(len((df.loc[(df['skinColor'] == 'dark') & (df['accessories'] == 0) & (df['nailPolish'] == 0) & (df['irregularities'] == 0)]).groupby('id'))))

# Gender
print("Male: " + str(len((df.loc[(df['gender'] == 'male') & (df['accessories'] == 0) & (df['nailPolish'] == 0) & (df['irregularities'] == 0)]))))
print("Female: " + str(len((df.loc[(df['gender'] == 'female') & (df['accessories'] == 0) & (df['nailPolish'] == 0) & (df['irregularities'] == 0)]))))
print("Not male and not Female: " + str(len((df.loc[(df['gender'] != 'female') & (df['gender'] != 'male') & (df['accessories'] == 0) & (df['nailPolish'] == 0) & (df['irregularities'] == 0)]))))

print("subj Male: " + str(len((df.loc[(df['gender'] == 'male') & (df['accessories'] == 0) & (df['nailPolish'] == 0) & (df['irregularities'] == 0)]).groupby('id'))))
print("subj Female: " + str(len((df.loc[(df['gender'] == 'female') & (df['accessories'] == 0) & (df['nailPolish'] == 0) & (df['irregularities'] == 0)]).groupby('id'))))

print("subj >60: " + str(len((df.loc[(df['age'] >= 60) & (df['accessories'] == 0) & (df['nailPolish'] == 0) & (df['irregularities'] == 0)]))))
print("subj >70: " + str(len((df.loc[(df['age'] > 70) & (df['accessories'] == 0) & (df['nailPolish'] == 0) & (df['irregularities'] == 0)]))))


bins = np.linspace(10,80,8)
# print(bins)

labels = ['10-20','20-30','30-40','40-50','50-60','60-70','70-80']

df['ageGroup'] = pd.cut(df['age'],bins=bins,labels=labels)
noIrr = df.loc[(df['accessories'] == 0) & (df['nailPolish'] == 0) & (df['irregularities'] == 0)]

print(df.loc[(df['age'] >= 60) & (df['accessories'] == 0) & (df['nailPolish'] == 0) & (df['irregularities'] == 0)].head(10000))

# ax = sb.countplot(data = noIrr, x = 'ageGroup')
# ax.set(xlabel='Age', ylabel='Number of images')
# plt.show()