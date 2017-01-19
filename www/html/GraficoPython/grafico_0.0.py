# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,1, num=100)
y = x

plt.plot(x,y,'r--')

z = [t**2 for t in x]
w = [t**3 for t in x]

plt.plot(x,w,'g^')

plt.show()
