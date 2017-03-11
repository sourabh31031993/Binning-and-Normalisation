#import seaborn as sns
from sklearn import preprocessing
import matplotlib.pyplot as plt
from pylab import *
import pandas as pd
import numpy as np
         
df = pd.read_csv('data2.csv',header=None)
df1 =df.ix[:,1]


plt.hist(df1, bins='auto')

plt.title("Histogram with 'auto' binning")
plt.xlabel("Binned Data")
plt.ylabel("Frequency")
plt.show()

 
