import common
import random
COUNT = 100

stations = common.load_csv('stations.tsv')
class gps_generator():
    def generate(self):
        for cnt in xrange(COUNT):
            st = random.choice(stations)
            print st[0], st[1:]


g = gps_generator()
g.generate()
