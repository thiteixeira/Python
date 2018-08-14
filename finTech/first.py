#!/usr/bin/env python 

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

pd.set_option('display.expand_frame_repr', False)

style.use('ggplot')

start = dt.datetime(2017, 1, 1)
end = dt.datetime.now()

df = web.DataReader('TSLA', 'morningstar', start, end)
#print (df.head())
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)

df.to_csv('TSLA.csv')
df = pd.read_csv('TSLA.csv', parse_dates=True, index_col=0)

# Create 100-day moving average
df['100ma'] = df['Close'].rolling(window=100, min_periods=0).mean()
df['50ma'] = df['Close'].rolling(window=50, min_periods=0).mean()
#df.dropna(inplace=True)
print (df.tail())


ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1)
ax1.plot(df.index, df['Close'])
ax1.plot(df.index, df['100ma'])
ax1.plot(df.index, df['50ma'])
ax2.bar(df.index, df['Volume'])

plt.show()
#plt.savefig('first.eps', format='eps', dpi=300)
