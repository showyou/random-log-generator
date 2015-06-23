#import numpy as np
from pandas import *
#from pylab import *
import matplotlib.pyplot as plt
from common import load_csv


x = []
y = []
c = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
KLASS = len(c)
data = load_csv("log.txt")
for i in xrange(0,KLASS):
    x = [float(dat[4]) for dat in data if int(dat[0])%KLASS == i]
    y = [float(dat[3]) for dat in data if int(dat[0])%KLASS == i]

#s = Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
#s = Series(x, y)
    plt.plot(x, y, c[i])
plt.show()
