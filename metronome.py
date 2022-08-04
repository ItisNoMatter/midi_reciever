import time
import threading
import sys

class Metronome(threading.Thread):
    def __init__(self,bpm:int) -> None:
        super(Metronome,self).__init__()
        self.daemon = True

        self.bpm:int = bpm
        self.current_beat:int = 0
        self.currrent_bar:int = 0
        self.cnt = 0
        pass
    def run(self):
        while True:
            time.sleep(1)
            self.cnt+=1
            
    def set_timesig(self):
        pass
    def pause(self):
        pass
if __name__ == "__main__":
    m = Metronome(60)
    m.start()
    try:
        while True:
            time.sleep(0.1)
            print("\r"+ str(m.cnt),end="")
    except KeyboardInterrupt:
        sys.exit()