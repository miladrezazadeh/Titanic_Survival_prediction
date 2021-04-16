## Import required libraries
import numpy as np
import pandas as pd
import pickle
import re
import os
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

## Import the data
train_data = '/Users/milad/OneDrive - Dalhousie University/Titanic_Github/Titanic_Survival_prediction/train.csv'
test_data = '/Users/milad/OneDrive - Dalhousie University/Titanic_Github/Titanic_Survival_prediction/test.csv'
df_train = pd.read_csv(train_data)
df_test = pd.read_csv(test_data)
