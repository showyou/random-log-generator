import matplotlib.pyplot as plt
from common import load_csv
import sys


x = []
y = []
c = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
KLASS = len(c)
data = load_csv(sys.argv[1])
for i in xrange(0,KLASS):
    x = [float(dat[4]) for dat in data if int(dat[0])%KLASS == i]
    y = [float(dat[3]) for dat in data if int(dat[0])%KLASS == i]
    plt.plot(x, y, c[i])

plt.show()
