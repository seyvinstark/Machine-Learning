#import numpy and panda for datamanipulation
7
import numpy as np
import pandas as pd
#sklear for preprocessing so we can deal with or categorical data
from sklearn.preprocessing import LabelEncoder
#file system management
import os
#to suppress warnings
import warnings
warnings.filterwarnings('ignore')

# List files available
#print(os.listdir("../input/"))
creditcards  = pd.read_csv('creditcards.csv')
print('training data shape: ',creditcards.shape)#rows and columns in this case observations and features
print(creditcards.head())
print(creditcards.columns)