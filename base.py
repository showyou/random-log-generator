# -*- encoding: utf-8 -*-
import random

class Base():
    def generate(self, context, config):
        # must override
        exit(1)

class Apache(Base):
    RECORDS = 10
    AGENT_LIST = [ \
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A405 Safari/7534.48.3',
    'Mozilla/5.0 (iPad; CPU OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A405 Safari/7534.48.3',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)'
    ];
    def __init__(self):
        self.HOSTS = self.RECORDS*4
        self.PAGES = self.RECORDS/4

    def generate(self):
        for i in xrange(0, self.RECORDS):
            print random.choice(self.AGENT_LIST)
     

a = Apache()
a.generate()
