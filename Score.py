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