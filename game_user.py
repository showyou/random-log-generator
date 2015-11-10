from generator import Generator
import random

USERS = 100000
LASTNAMES = ['Haruto', 'Riku', 'Hinata', 'Haru', 'Hana', 'Ichika', 'Akari',
'Sara']
FIRSTNAMES = ['Sato', 'Tanaka', 'Suzuki', 'Takahashi', 'Watanabe', 'Ito']
PREFECTURES = ['Tokyo', 'Kanagawa', 'Osaka', 'Saitama', 'Fukuoka', 'Hokkaido',
'Chiba', 'Kyoto', 'Hyogo']
CARRER = ['docomo', 'softbank', 'au']

class GameLogGenerator(Generator):
    def generate(self, users=USERS):
        for us in xrange(users):
            last_name = random.choice(LASTNAMES);
            first_name = random.choice(FIRSTNAMES);
            prefecture = random.choice(PREFECTURES);
            carrer = random.choice(CARRER);
            print '%d, %s, %s, %s, %s' % (us, first_name, last_name, prefecture,
            carrer)

if __name__ == '__main__':
    g = GameLogGenerator()
    g.generate()
