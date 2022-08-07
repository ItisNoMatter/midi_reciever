import sys
from metronome import Metronome
from midi_input import MidiIn,Message

if __name__ == "__main__":
    midiin = MidiIn()# pylanceの警告がでないぜ！！！！！！！
    port = midiin.open_port()
    with port:
        try:
            while True:
                data = port.get_message()
                if data:
                    m = Message(data)
                    print("status:{} note_num:{} velocity:{}".format(m.status,m.note_num,m.velocity))
        except KeyboardInterrupt:
            sys.exit()