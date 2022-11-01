#Question one:What is the result of the following code?
import pandas as pd
import numpy as np
import requests

df = pd.DataFrame(np.random.randn(5, 3), columns=['col1', 'col2', 'col3'])
df.apply(lambda x: x.max() - x.min())
print(df.apply)

#answer
#       col1      col2      col3
#0 -0.247744  0.480277 -0.562112
#1  0.576703  0.782410  0.982423
#2 -0.594293 -1.052719 -0.923104
#3 -0.198674  0.247023  0.081566
#4  0.943654 -1.187043  0.883664

#Question two:Download a csv file from 
# https://stats.govt.nz/assets/Uploads/Business-employment-data/Business-employment-data-June-2022-quarter/Download-data/business-employment-data-june-2022-quarter-csv.zip 
# and load it into a pandas dataframe. How many rows and columns are there?
# load CSV

def dowload_csv(url):
            r=requests.get(url)
            with open('data.csv','wb') as f:
                        f.write(r.content)

import os
if not os.path.exists('data.csv'):
            dowload_csv('https://stats.govt.nz/assets/Uploads/Business-employment-data/Business-employment-data-June-2022-quarter/Download-data/business-employment-data-june-2022-quarter-csv.zip')

     
df = pd.read_csv('data.csv')
print(df)

df=pd.read_csv('bands.csv')
print(df.head())



#Question three:What method can be used to get the number of non-NA values in a pandas dataframe?

#A. df.count()


#Question four:Create a dataframe with 10 rows and 3 columns,
#  where the values are random numbers between 1 and 10 (inclusive). 
# Then, replace all values greater than 5 with the value 10.






#Question five:
import json
tasks = requests.get("https://jsonplaceholder.typicode.com/albums")

df = pd.Datafame(tasks)

print(df.head())
