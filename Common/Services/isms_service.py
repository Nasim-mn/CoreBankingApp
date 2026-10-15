from abc import ABC, abstractmethod


class ISmsService(ABC):
    @abstractmethod
    def send(self, phone: str, content: str) -> bool:
        """Send an SMS. Returns True if the message was accepted, False otherwise."""
        pass