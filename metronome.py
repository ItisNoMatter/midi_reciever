import time
import threading
import sys

class Metronome(threading.Thread):
    def __init__(self,bpm:int=60,timesig:int=4,ppq=4) -> None:
        super(Metronome,self).__init__()
        self.daemon = True

        #immutable(にしたい)
        self.bpm:int = bpm
        self.timesig:int = timesig
        self._ppq:int = ppq #Pulses per quarter note 
        
        #mutable
        self.current_tick:int = 1
        self.current_beat:int = 1
        self.currrent_bar:int = 1

        #debug
        self.last_call_time:float = time.time()
        self.interval:float = 0
        pass
    def run(self):
        print(self.timesig)
        while True:
            time.sleep((self.bpm/60)/self._ppq)
            self._increment_tick()

    def _increment_tick(self):
        if self.current_tick == self._ppq:
            self._increment_beat() 
            self.current_tick = 1
            return
        self.current_tick += 1

    def _increment_beat(self):
        self.interval = time.time()- self.last_call_time
        self.last_call_time = time.time()
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
            time.sleep(0.01)
            #print("\r"+ " beat:"str(m.current_beat),end="")
            print("\rbar: {} beat: {} tick: {:03}".format(m.currrent_bar,m.current_beat,m.current_tick))
            print("\rerror_time(s/beat): {} ".format(m.interval-1) +"\033[2A",end="")
            print()
    except KeyboardInterrupt:
        sys.exit()