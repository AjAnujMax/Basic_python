# What is Matplotlib?
# Matplotlib is a low level graph plotting library in python that serves as a visualization utility.

#--------------------intro------------------------------

import matplotlib
print(matplotlib.__version__)

#output:- 2.0.0

#---------------------Pyplot------------------------------------
#import matplotlib.pyplot as plt
#Now the Pyplot package can be referred to as plt.
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()



