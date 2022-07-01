import time
import rtmidi

midiin = rtmidi.MidiIn()
port = midiin.open_port()
with port:
    while True:
        data = port.get_message()
        if data:
            print(data)