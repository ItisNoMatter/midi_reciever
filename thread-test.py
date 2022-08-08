from os import system
import sys
from metronome import Metronome
from midi_input import MidiIn,Message
from visualize import StdPrint

if __name__ == "__main__":
    midiin = MidiIn()# pylanceの警告がでないぜ！！！！！！！
    port = midiin.open_port()
    metronome = Metronome(bpm=60)
    metronome.atatch_visualizer(StdPrint())
    metronome.start() 
    with port:
        try:
            while True:
                data = port.get_message()
                if data:
                    m = Message(data)
                    print("status:{} note_num:{} velocity:{}".format(m.status,m.note_num,m.velocity))
                    
        except KeyboardInterrupt:
            sys.exit()