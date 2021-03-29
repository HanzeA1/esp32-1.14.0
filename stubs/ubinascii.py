"""
Module: 'ubinascii' on esp32 1.14.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.14.0', version='v1.14 on 2021-02-02', machine='ESP32 module with ESP32')
# Stubber: 1.3.2


def a2b_base64():
    pass


def b2a_base64():
    pass


def crc32():
    pass


def hexlify(data: bytes, sep: str = '') -> bytes:
    """Convert the bytes in the data object to a hexadecimal representation. Returns a bytes object.

        If the additional argument sep is supplied it is used as a separator between hexadecimal values.
    """


def unhexlify(data) -> bytes:
    """Convert hexadecimal data to binary representation. Returns bytes string. (i.e. inverse of hexlify)
    """
