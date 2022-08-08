from abc import ABCMeta,abstractmethod
import os
class Visualizer(metaclass=ABCMeta):
    def __init__(self):
        pass
    @abstractmethod
    def print_beat(self,bar:int,beat:int):
        pass
    @abstractmethod
    def print_log(self,message:str):
        pass
class StdPrint(Visualizer):
    def __init__(self):
        pass
    def print_log(self, message: str):
        print(message)
        return super().print_log(message)
    def print_beat(self, bar, beat):
        os.system("cls")
        print("bar:{} beat:{}".format(bar,beat))
        return super().print_beat(bar, beat)