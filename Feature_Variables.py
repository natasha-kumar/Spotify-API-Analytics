import pandas as pd 

df = pd.read_csv("Appended_data.csv")

df['season'] = 0

for i in range(df.shape[0]):
    if df.iloc[i,5] in (12,1,2):
        df.iloc[i,19] = 'Winter'
    elif df.iloc[i,5] in (3,4,5):
        df.iloc[i,19] = 'Spring'
    elif df.iloc[i,5] in (6,7,8):
        df.iloc[i,19] = 'Summer'
    else:
        df.iloc[i,19] = 'Fall'


df.to_csv('Appended_data_v2.csv')