from generator import Generator
import random
import sys
import datetime

DATES_MAX = 10
COUNTS = 100
USERS = 10000
ITEMS = 10
COINS = [100, 500, 1000, 2000]
INITDATE = [2013, 6, 1]

class GameLogGenerator(Generator):
    def generate(self, dates_max=DATES_MAX, users=USERS, items=ITEMS, counts=COUNTS):
        print dates_max
        for dm in xrange(dates_max):
            for cnt in xrange(counts):
                dt = datetime.date(*INITDATE) + datetime.timedelta(dm)
                user = random.randint(0, users)
                item = random.randint(0, items)
                amount = random.choice(COINS)
                print '%s,%d,%d,%d' % (dt.isoformat(), user, item, amount)


if __name__ == '__main__':
    g = GameLogGenerator()
    if len(sys.argv) > 4:
        #g.generate(int(sys.argv[1]), int(sys.argv[2]))
        g.generate(
            int(sys.argv[1]), 
            int(sys.argv[2]),
            int(sys.argv[3]),
            int(sys.argv[4])
        )
    else:
        g.generate()
