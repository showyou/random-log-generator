import numpy as np
from pandas import *
from pylab import *
import matplotlib.pyplot as plt
from common import load_csv

x = []
y = []
data = load_csv("log.txt")
x = [dat[3] for dat in data]
y = [dat[2] for dat in data]


s = Series(x, y)
s.plot()

plt.show()
