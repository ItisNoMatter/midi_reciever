import time
import threading
import sys

class Metronome(threading.Thread):
    def __init__(self,bpm:int=60,timesig:int=4) -> None:
        super(Metronome,self).__init__()
        self.daemon = True

        self.bpm:int = bpm
        self.timesig:int = timesig
        self.current_beat:int = 1
        self.currrent_bar:int = 1
        self.cnt = 0
        pass
    def run(self):
        print(self.timesig)
        while True:
            time.sleep(self.bpm/60)
            self.cnt += 1
            self._increment_beat()
    def _increment_beat(self):
        if self.current_beat == self.timesig:
            self.currrent_bar += 1
            self.current_beat = 1
            return
        self.current_beat += 1

    def set_timesig(self):
        pass
    def pause(self):
        pass
if __name__ == "__main__":
    m = Metronome(bpm=60,timesig=4)
    m.start()
    try:
        while True:
            time.sleep(0.1)
            #print("\r"+ " beat:"str(m.current_beat),end="")
            print("\rbar: {} beat: {}".format(m.current_beat,m.currrent_bar),end="")
    except KeyboardInterrupt:
        sys.exit()