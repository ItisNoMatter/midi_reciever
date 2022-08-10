from dataclasses import dataclass
from typing import List

from metronome import BeatTime


@dataclass(frozen=True)
class Note:
    beat:BeatTime
    note_num:int
@dataclass
class Score:
    def __init__(self) -> None:
        self.notes:List[Note] = []
    def __str__(self):
        s = ["note:{:4} time:{}".format(n.note_num,n.beat.time,) for n in self.notes]
        return '\n'.join(s)
    def add_note(self,note:Note):#この機能だけだと属性に直接アクセスしたほうが良いが、あとでいろいろ機能追加しそうなのでこうしている
        self.notes.append(note)