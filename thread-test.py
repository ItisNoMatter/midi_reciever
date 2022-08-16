from os import system
import sys
from Player import Player
from Score import Note, Score
from metronome import Metronome
from midi_input import MidiIn,Message
from visualize import StdPrint
from playsound import playsound
if __name__ == "__main__":
    midiin = MidiIn()# pylanceの警告がでないぜ！！！！！！！
    port = midiin.open_port()
    metronome = Metronome(bpm=60,timesig=2 ,ppq=2)
    metronome.atatch_visualizer(StdPrint())
    score = Score()
    player = Player("bebopnet-code/resources/backing_tracks/standards/juiceS48.mp3")
    player.start()
    metronome.start() 
    with port:
        try:
            while True:
                data = port.get_message()
                if data:
                    m = Message(data)
                    if m.status == "Note:ON":
                        note = Note(metronome.get_beat_time(),m.note_num)
                        score.add_note(note)
                    print("status:{} note_num:{} velocity:{}".format(m.status,m.note_num,m.velocity))
                    
        except KeyboardInterrupt:
            print(str(score))
            sys.exit()