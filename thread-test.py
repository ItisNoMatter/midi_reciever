from os import system
import sys
from Score import Note, Score
from metronome import Metronome
from midi_input import MidiIn,Message
from visualize import StdPrint

if __name__ == "__main__":
    midiin = MidiIn()# pylanceの警告がでないぜ！！！！！！！
    port = midiin.open_port()
    metronome = Metronome(bpm=60)
    metronome.atatch_visualizer(StdPrint())
    score = Score()
    metronome.start() 
    with port:
        try:
            while True:
                data = port.get_message()
                if data:
                    m = Message(data)
                    note = Note(metronome.get_beat_time(),m.note_num)
                    score.add_note(note)
                    print("status:{} note_num:{} velocity:{}".format(m.status,m.note_num,m.velocity))
                    
        except KeyboardInterrupt:
            print(str(score))
            sys.exit()