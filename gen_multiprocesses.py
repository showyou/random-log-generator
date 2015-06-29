import game_log as gl
import processes_sample

if __name__ == '__main__':
    g = gl.GameLogGenerator()
    processes_sample.run( g.gen_record, [[gl.DATES_MAX, gl.USERS, gl.ITEMS],])

