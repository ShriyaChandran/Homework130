import pandas as pd
import csv

df = pd.read_csv('bright_stars.csv')
df.columns

df.columns

Index(['Unnamed: 0', 'Star_name', 'Distance', 'Mass', 'Radius', 'Luminosity',
       'Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1'],
      dtype='object')
df.drop(['Unnamed: 0','Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1','Luminosity'],axis=1,inplace=True)

final_data = df.dropna()

final_data.reset_index(drop = True, inplace = True)
final_data.to_csv('final_data.csv')

final.data.info()

final_data.describe()

final_data.index()

final_data.head(5)

final_data.dtypes()