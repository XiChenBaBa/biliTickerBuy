import base64
import struct
from time import time


def EncodeCtoken(prepare_time: int) -> str:
    current_time_ms = int(time() * 1000)
    calculatedTime = (current_time_ms - prepare_time) / 1000
    secFromPrepare = int(calculatedTime)
    if secFromPrepare <= 0:
        secFromPrepare = 1

    scrollX = 0
    scrollY = 0
    innerWidth = 1170
    innerHeight = 2532
    outerWidth = 1170
    outerHeight = 2532
    screenX = 0
    screenY = 44
    screenWidth = 1170

    data = bytearray(16)
    data[0] = 0
    data[1] = min(scrollX, 255)
    data[2] = 0
    data[3] = min(scrollY, 255)
    data[4] = min(innerWidth, 255)
    data[5] = 1
    data[6] = min(innerHeight, 255)
    data[7] = min(outerWidth, 255)
    struct.pack_into('>H', data, 8, min(secFromPrepare, 65535))
    struct.pack_into('>H', data, 10, min(int(calculatedTime), 65535))
    data[12] = min(outerHeight, 255)
    data[13] = min(screenX, 255)
    data[14] = min(screenY, 255)
    data[15] = min(screenWidth, 255)

    char_string = ''.join(chr(b) for b in data)
    uint16_array = []
    for char in char_string:
        uint16_array.append(ord(char))
    uint8_array = bytearray()
    for value in uint16_array:
        uint8_array.extend(struct.pack('<H', value))

    return base64.b64encode(uint8_array).decode('ascii')