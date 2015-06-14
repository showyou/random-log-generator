import common
import random
COUNT = 10000
MAX_USERS = 10

stations = common.load_tsv('stations.tsv')
class gps_generator():
    def generate(self):
        for cnt in xrange(COUNT):
            user = random.randint(0, MAX_USERS)
            st = random.choice(stations)
            print '%s,%s' % (user, ','.join(st))


g = gps_generator()
g.generate()
