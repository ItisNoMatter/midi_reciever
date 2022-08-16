
import sys
from playsound import playsound
import threading

class Player(threading.Thread):
    def __init__(self,filepath:str):
        super(Player,self).__init__()
        self.daemon = True
        self.filepath = filepath
    def run(self):
        playsound(self.filepath)
if __name__ == "__main__":
    try:
        playsound.playsound("bebopnet-code/resources/backing_tracks/standards/Fly_me_to_the_moon_v2.mp3")
    except KeyboardInterrupt:
        print("a")
        sys.exit()