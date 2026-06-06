from logging import Logger
from typing import Any
import Utils
import dolphin_memory_engine as dme
import asyncio
import psutil

GAME_VERSION = None

SUPPORTED_GAME_IDS = {
    "SUPE01": "NTSC-U",
    "SUPP01": "PAL",
}

class DolphinException(Exception):
    pass

class DolphinClient:
    def __init__(self, logger: Logger):
        self.dme = dme
        self.logger = logger
        self.attempt = 1
        self.told_region = False

    @staticmethod
    def check_for_dolphin():
        if Utils.is_windows:
            target_processes = ["Dolphin.exe", "DolphinQt2.exe"]

        elif Utils.is_macos:
            target_processes = ["Dolphin"]

        elif Utils.is_linux:
            target_processes = ["dolphin-emu", "dolphin-emu-qt2", "dolphin-emu-wx"]

        else:
            # Unsupported operating system
            return False

        dolphin_count = 0

            # Loop through all currently running programs
        for proc in psutil.process_iter(['name']):
            try:
                # Check for a match
                if proc.info['name'] in target_processes:
                    dolphin_count = dolphin_count + 1

            # Safely ignore background processes that shift while scanning
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

        if dolphin_count > 1:
            return 2
        elif dolphin_count == 1:
            return 1
        else:
            return 0


    async def attempt_to_hook(self):
        if not self.dme.is_hooked():
            self.logger.info(f"Attempting to hook: Attempt {self.attempt}")
            self.dme.hook()

        if self.dme.is_hooked():
            self.logger.info("Hooked successfully!")
            self.attempt = 1  # Reset counter on success
        else:
            dolphin_status = self.check_for_dolphin()

            if dolphin_status == 0:
                self.logger.info("Failed to hook! Dolphin isn't running!")
            elif dolphin_status == 1:
                self.logger.info("Failed to hook! Wii Party isn't running!")
            elif dolphin_status == 2:
                self.logger.info("Failed to hook! Too many Dolphin instances are running!")

            self.attempt += 1
            await asyncio.sleep(5)

    def is_hooked_class(self):
        if self.dme.is_hooked():
            return True
        else:
            return False

    def disconnect(self):
        if self.dme.is_hooked():
            self.dme.un_hook()


    def read_byte(self, address: Any) -> Any:
        self.dme.is_hooked()
        result = self.dme.read_byte(address)
        return result

    def read_bytes(self, address: Any, bytes_to_read: int) -> Any:
        self.dme.is_hooked()
        result = self.dme.read_bytes(address, bytes_to_read)
        return result

    def read_word(self, address: Any) -> Any:
        self.dme.is_hooked()
        result = self.dme.read_word(address)
        return result

    def read_float(self, address: Any) -> Any:
        self.dme.is_hooked()
        result = self.dme.read_float(address)
        return result

    def read_string(self, address: int) -> str:
        self.dme.is_hooked()
        byte = self.dme.read_bytes(address, 5)
        # Decode and strip out the invisible null bytes
        decoded = byte.decode("utf-8", errors="ignore").rstrip('\x00')
        return decoded

    def write_string(self, address: Any, string: str) -> Any:
        self.dme.is_hooked()
        encoded = string.encode("utf-8")
        self.dme.write_byte(address, encoded)

    def write_byte(self, address: Any, data: Any):
        self.dme.is_hooked()
        self.dme.write_byte(address, data)

    def write_bytes(self, address: Any, data: Any) -> Any:
        self.dme.is_hooked()
        self.dme.write_bytes(address, data)

    def write_float(self, address: Any, data: Any):
        self.dme.is_hooked()
        self.dme.write_float(address, data)

    def write_word(self, address: Any, data: Any):
        self.dme.is_hooked()
        self.dme.write_word(address, data)

    def follow_pointers(self, address: Any, pointers: list):
        self.dme.is_hooked()
        result = self.dme.follow_pointers(address, list(pointers))
        return result
