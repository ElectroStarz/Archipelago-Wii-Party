from functools import cached_property
from .WPInterface import WPInterface
from .memory_addresses import *
from logging import Logger

class AddressLib:
    def __init__(self):
        self.interface = WPInterface(Logger("wii_party_client"))

    @cached_property
    def bgi_data(self):
        return self.interface.dolphin_client.follow_pointers(BGIAddresses.generic_data, Pointers.BGI.to_generic_data)

    address_properties = [
        "bgi_data"
    ]

    def reset_all_addresses(self, logger):
        """Forces the client to re-read memory by clearing all cached addresses."""

        cleared_count = 0

        for prop in self.address_properties:

            if prop in self.__dict__:
                delattr(self, prop)
                cleared_count += 1

        logger.info(f"Successfully cleared {cleared_count} cached addresses. They will be re-read on next access.")