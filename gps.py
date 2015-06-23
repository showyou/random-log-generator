import common
import random
COUNT = 100
MAX_USERS = 5
RESOLUTION = 0.0005

stations = common.load_tsv('stations.tsv')
class gps_generator():
    def generate(self):
        for cnt in xrange(COUNT):
            user = random.randint(0, MAX_USERS)
            st = random.choice(stations)
            st[2] = float(st[2])
            st[3] = float(st[3])
            st[2] += random.gauss(0, RESOLUTION)
            st[3] += random.gauss(0, RESOLUTION)
            print '%s,%s,%s,%f,%f' % (user, st[0], st[1], st[2], st[3])


g = gps_generator()
g.generate()
