#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

# Plot y versus its index values
plt.plot(y, 'r-')        # 'r' = red, '-' = solid line
plt.xlim(0, 10)          # forces x-axis to range exactly from 0 to 10
plt.show()