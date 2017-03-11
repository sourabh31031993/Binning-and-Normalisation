from sklearn import preprocessing
from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt
#from pylab import *
import pandas as pd 
import numpy as np
          
df = pd.read_csv('data2.csv',header=None)
df1 =df.ix[:,1]

#Z-scores
z_scores_np = (df1 - df1.mean()) / df1.std()
print(z_scores_np)

plt.figure(1)
plt.subplot(211)
plt.hist(df1, color='b',edgecolor='black')
plt.title("Histogram without Normalization")
#plt.grid(True)
plt.xlabel('values')
plt.tight_layout()

plt.figure(2)
plt.hist(z_scores_np, color='g',edgecolor='black')
plt.title("Histogram with Z_Score Normalization")
#plt.grid()
plt.xlabel('z_score values')
plt.tight_layout()

plt.show()
