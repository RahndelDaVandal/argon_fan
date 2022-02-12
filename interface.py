# interface.py
from controller import Controller

class Interface:
    controller: Controller

    def setInterface(self, interface = None) -> None:
        if interface is not None:
            self.interface = interface
        else:
            self.interface = Default()

    def run(self) -> None:
        pass

