#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.DataFrame({'A' : np.random.randn(4),
                    'B' : np.random.randn(4),
                    'C' : np.random.randn(4),
                    'D' : np.random.randn(4)})

print('Dataframe-1:')
print(df1)

df2 = pd.DataFrame({'A' : np.random.randn(4),
                    'B' : np.random.randn(4),
                    'C' : np.random.randn(4),
                    'D' : np.random.randn(4)})
print('\nDataframe-2:')
print(df2)

print('\nConcat: ')
df = pd.concat([df1, df2])
print(df)

print('\nMean: ')
df = df.groupby(df.index).mean()
print(df)

print('\nSlice:')
print(df.ix[[0,1], 'A'])

#print('\nFilter:')
#print(df.query('color == "red"'))


df.plot()
plt.ylabel('y-label')
plt.xlabel('x-label')
plt.title('Title')
#plt.show()
plt.savefig('pandas-example.png')

print('\nMean of df:')
df = df.mean()
print(df)

print('\nIndexes: ')
print(df.index)

print('\nSlice A')
print(df['A'])
