# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ktl0KsCvUovMoYpHGwskitMuKAJ5OBBX
"""

from google.colab import files
import pandas as pd

uploaded = files.upload()

data_maol = pd.read_csv('/content/titanic.csv.csv')
print(data_maol)

data1 = data_maol.loc[:,['Age','Pclass','Survived']]
print(data1)

data2 = data_maol[['Age', 'Pclass', 'Survived']]
data2.plot(title='Persebaran Data', x='Age', y='Pclass', kind='scatter', c='Survived', colormap='Paired')

data3 = data_maol[['Name', 'Sex', 'Age', 'Pclass', 'Fare']]
penumpang=data3.groupby('Pclass')['Name'].nunique()
print('Jumlah Penumpang:\n', penumpang)

data4 = data_maol[['Name', 'Sex', 'Age', 'Pclass', 'Fare']]
notsurvivedpassanger=data4['Pclass'].loc[data_maol['Survived']==0]
print('Penumpang yang tidak survived:\n', notsurvivedpassanger.value_counts())
survivedpassanger=data4['Pclass'].loc[data_maol['Survived']==1]
print('\nPenumpang yang survived:\n', survivedpassanger.value_counts())

data3 = data_maol [['Name', 'Sex', 'Age', 'Pclass', 'Fare']]
penumpang = data3.groupby('Sex')['Name'].nunique()
print('Jumlah penumpang:\n', penumpang)

data4 = data_maol[['Name', 'Sex', 'Age', 'Pclass', 'Fare']]
notsurvivedpassanger=data4['Sex'].loc[data_maol['Survived']==0]
print('Penumpang yang tidak survived:\n', notsurvivedpassanger.value_counts())

survivedpassanger=data4['Sex'].loc[data_maol['Survived']==1]
print('penumpang yang survived:\n', survivedpassanger.value_counts())