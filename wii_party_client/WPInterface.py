from enum import Enum

from .dolphin_connection import DolphinClient, DolphinException


class ConnectionState(Enum):
    DISCONNECTED = 0
    CONNECTED = 1


class WPInterface:
    dolphin_client: DolphinClient

    def __init__(self, logger):
        self.logger = logger
        self.dolphin_client = DolphinClient(logger)

    def get_connection_state(self) -> ConnectionState:
        try:
            if not self.dolphin_client.is_hooked_class():
                return ConnectionState.DISCONNECTED

            return ConnectionState.CONNECTED

        except (DolphinException, RuntimeError):
            return ConnectionState.DISCONNECTED
