## Cloned from https://github.com/Brovidius/FP16_converter/blob/main/FP16_converter.py

import numpy as np

class Converter():

    def FP16_to_chars(my_number):

        # The input is converted to a float16 then turned into bytes in unicode.
        # We want to do this so we can split it up into two bytes later.
        x_bytes = (np.float16(my_number).tobytes())

        # Convert the bytes to a 16bit integer
        x_int = int.from_bytes(x_bytes, byteorder='little', signed=False)

        # convert the 16bit integer to its binary representation
        binary_x = np.binary_repr(x_int, width=16)

        # Splitting up the 16 bits into two bytes and their 8bit integer numbers based on base 2
        byte_1 = int(binary_x[:8], 2)
        byte_2 = int(binary_x[8:], 2)

        # Converting the 8bit integers into 8bit unicode equivalent character
        myasc1 = chr(byte_1)
        myasc2 = chr(byte_2)

        return myasc1, myasc2

    # RECEIVING PART
    def chars_to_FP16(received_character):
        
        # Converting the unicode characters into the unicode code integer
        myByte = ord(received_character[0])
        myByte2 = ord(received_character[1])

        # Converting the integers into 8bit binary representations, and combining them into a 16bit value as a string
        x_int = (format(myByte, '#010b')[2:] + format(myByte2, '#010b')[2:])

        # convert the 16bit value string into a 16bit integer, then into a combination of two bytes.
        byte_str = int(x_int, 2).to_bytes(2, byteorder='little')

        # create a numpy float16 from the bytes
        x = np.frombuffer(byte_str, dtype=np.float16)[0]
        
        return x

