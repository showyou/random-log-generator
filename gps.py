from generator import Generator
import common
import random
import sys

COUNTS = 100000
USERS = 1000
RESOLUTION = 0.0005

stations = common.load_tsv('stations.tsv')
class gps_generator(Generator):
    def generate(self, count=COUNTS, users=USERS):

        for cnt in xrange(count):
            user = random.randint(0, users)
            st = random.choice(stations)
            st[2] = float(st[2])
            st[2] += random.gauss(0, RESOLUTION)
            st[3] = float(st[3])
            st[3] += random.gauss(0, RESOLUTION)
            print '%s,%s,%s,%f,%f' % (user, st[0], st[1], st[2], st[3])


if __name__ == '__main__':
    g = gps_generator()
    if len(sys.argv) > 2:
        g.generate(int(sys.argv[1]), int(sys.argv[2]) )
    else:
        g.generate()
