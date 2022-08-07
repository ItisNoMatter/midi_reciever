from nis import match
import time
from typing import Tuple
import rtmidi
midiin = rtmidi.MidiIn()
port = midiin.open_port()
with port:
    while True:
        data = port.get_message()
        if data:
            print(data)
            print(type(rtmidi._rtmidi))

class Message:
    def __init__(self,data:Tuple) -> None:
        if data[0][0] == 144:#これmatich文で書いたほうがきれいなのは知ってるけどpythonのバージョンが<10なので無理
            self.status = "Note:ON"
        elif data[0][0] == 128:
            self.status = "Note:OFF"
        else:
            raise Exception("未実装のMIDIステータスナンバー[{}]を受け取ったぞ!".format(data[0][0]))