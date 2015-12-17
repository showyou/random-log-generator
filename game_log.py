from generator import Generator
import random
import sys
import datetime

DATES_MAX = 300
COUNTS = 3000
USERS = 100000
ITEMS = 100
COINS = [100, 500, 1000, 2000, 9800]
INITDATE = [2015, 7, 15]

random.seed(0)
class GameLogGenerator(Generator):
    def generate(self, dates_max=DATES_MAX, users=USERS, items=ITEMS, counts=COUNTS):
        #print dates_max
        for dm in xrange(dates_max):
            for cnt in xrange(counts):
                self.gen_record([dm, users, items,])

    def gen_record(self, args):
        dt = datetime.date(*INITDATE) + datetime.timedelta(args[0])
        user = random.randint(0, args[1])
        item = random.randint(0, args[2])
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
