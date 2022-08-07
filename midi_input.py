from typing import Tuple
import rtmidi

class Message:
    def __init__(self,data:Tuple) -> None:
        if data[0][0] == 144:#これmatich文で書いたほうがきれいなのは知ってるけどpythonのバージョンが<10なので無理
            self.status = "Note:ON"
        elif data[0][0] == 128:
            self.status = "Note:OFF"
        else:
            raise Exception("未実装のMIDIステータスナンバー[{}]を受け取ったぞ!".format(data[0][0]))
        self.note_num = data[0][1]
        self.velocity = data[0][2]



class _MIDI_INPUT_DEVICE:#pylanceを黙らせるための偽クラス,
    def __init__(self) -> None:
        raise Exception("""
        偽クラスのインスタンスが作られている。
        MIDI_INPUT_DEVICEクラスはpylanceを黙らせるためのものなので、インスタンス化されてはいけない。
        """)
    def open_port(self):
        return self

    def get_message(self)-> tuple:
        return ()

    def __enter__(self):
        pass
    def __exit__(self):
        pass
def MidiIn() -> _MIDI_INPUT_DEVICE:#pylanceを黙らせるための関数、型ヒントは嘘
    return rtmidi.MidiIn()


if __name__ == "__main__":
    midiin = rtmidi.MidiIn()
    port = midiin.open_port()
    print(type(midiin))
    with port:
        while True:
            data = port.get_message()
            if data:
                m = Message(data)
                print("status:{} note_num:{} velocity:{}".format(m.status,m.note_num,m.velocity))
