import common
import random
import sys

DATES_MAX = 1
COUNT = 100000
USERS = 10000
ITEMS = 10
COINS = [100, 500, 1000, 2000]

stations = common.load_tsv('stations.tsv')
class game_log_generator():
    def generate(self):
        dates_max = DATES_MAX
        users = USERS
        count = COUNT
        items = ITEMS
        for dm in xrange(dates_max):
            for cnt in xrange(count):
                user = random.randint(0, users)
                item = random.randint(0, items)
                amount = random.choice(COINS)
                print '2015/06/29,%d,%d,%d' % (user, item, amount)

if __name__ == '__main__':
    g = game_log_generator()
    if len(sys.argv) > 2:
        #g.generate(int(sys.argv[1]), int(sys.argv[2]))
        g.generate()
    else:
        g.generate()
