#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 20001)
y1 = np.exp((np.log(0.5) / 5730) * x)
y2 = np.exp((np.log(0.5) / 1600) * x)

# Plot decay of C-14 and Ra-226
plt.plot(x, y1, 'r--', label='C-14')
plt.plot(x, y2, 'g-', label='Ra-226')
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title('Exponential Decay of Radioactive Elements')
plt.xlim(0, 20000)
plt.ylim(0, 1)
plt.legend(loc='upper right')
plt.show()