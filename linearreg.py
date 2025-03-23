import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("advertising.csv")
df

x = df.drop(columns=['sales'])
y=df['sales']
print(x)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

print(x_train)
print(x_test)
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(x_train, y_train)
y_pred = reg.predict(x_test)
y_pred
import pickle 
filename="classifier.pkl"
with open (filename,'wb') as file :
  pickle.dump(reg,file)
  
import pickle 
filename="classifier.pkl"
with open (filename,'rb') as file :
  loaded_model=pickle.load(file)
  
predictions = loaded_model.predict(x_test)
print(f"Predictions: {predictions}")