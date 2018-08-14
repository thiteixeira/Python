#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# Read from CSV
data = np.loadtxt('./sample.csv', delimiter='\t', skiprows=1)

x1 = data[0:1,0]
x2 = data[1:,0]

# Multiplot
fig, axs = plt.subplots(nrows=2, ncols=2, sharex=True)

# Plot 1
ax = axs[0,0]
ax.yaxis.grid()
y1 = data[0:1,2] # 50 nodes
y2 = data[1:,2] # 90 nodes
line1, = ax.bar(x1, y1, color='b', alpha=0.3)
line2, = ax.bar(x2, y2, color='r', alpha=0.3)
ax.set_title('Plot-1')

# Plot 2
ax = axs[0,1]
y1 = data[0:1,5] # 50 nodes
y2 = data[1:,5] # 90 nodes
line1, = ax.bar(x1, y1, lw=2, alpha=0.5, label='Label-1')
line2, = ax.bar(x2, y2, lw=2, alpha=0.5, label='Label-2')
ax.set_title('Plot-2')

# Plot 3
ax = axs[1,0]
y1 = data[0:1,8] # 50 nodes
y2 = data[1:,8] # 90 nodes
line1, = ax.bar(x1, y1, lw=2, alpha=0.7,  label='Label-1')
line2, = ax.bar(x2, y2, lw=2, alpha=0.7, label='Label-2')
ax.set_title('Plot-3')

# Plot 4
ax = axs[1,1]
y1 = data[0:1,11] # 50 nodes
y2 = data[1:,11] # 90 nodes
line1, = ax.bar(x1, y1, lw=2, label='Label-1')
line2, = ax.bar(x2, y2, lw=2, label='Label-2')
ax.set_title('Plot-4')

ax.yaxis.grid()
fig.tight_layout()

plt.show()

