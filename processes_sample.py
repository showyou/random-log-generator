#! -*- coding: utf-8 -*-
import multiprocessing
import random
import time

def worker(timer):
    # カレントプロセス
    p = multiprocessing.current_process()
    counter = 100 #timer
    while counter >= 0:
        print('%s(PID %s): counter=%d' % (p.name, p.pid, counter))
        counter -= 1
        time.sleep(0.01)

processes = []
for i in range(5):
    timer = random.randrange(20)
    p = multiprocessing.Process(target=worker, args=(timer,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

