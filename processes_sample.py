#! -*- coding: utf-8 -*-
import multiprocessing
import random
import time

TIMESPAN = 2
COUNTS = 1000
PROCESSES = 500


def __worker(timer, func, args):
    # カレントプロセス
    p = multiprocessing.current_process()
    counter = timer #timer
    while counter >= 0:
        func(*args)
        #func(p.name, p.pid, counter)
        #print('%s(PID %s): counter=%d' % (p.name, p.pid, counter))
        counter -= 1
        time.sleep(TIMESPAN)


def func_print(name, pid, counter):
    print('%s(PID %s): counter=%d' % (name, pid, counter))


def run(func, args=[]):
    processes = []
    for i in range(PROCESSES):
        timer = random.randrange(COUNTS)
        p = multiprocessing.Process(target=__worker, args=(timer,func, args))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()



if __name__ == '__main__':
    run(func_print)
