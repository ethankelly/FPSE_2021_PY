from abc import ABC, abstractmethod


class Input(ABC):
    @abstractmethod
    def getString(self, message):
        pass
