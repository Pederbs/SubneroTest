import numpy as np

class Converter():

    def bytes_list_to_FP16(user_input):

        if isinstance(user_input, list):
            if isinstance(user_input[0], str):
                user_input = [eval(i) for i in user_input]  

        if isinstance(user_input, str):
            converted_list = user_input.strip('][').split(', ')
            converted_list = [eval(i) for i in converted_list]
            user_input = converted_list

        new_val = [Converter.bytes_to_FP16(a, b) for a, b in zip(user_input[::2], user_input[1::2])]
        return new_val
    
    def FP16_list_to_bytes(user_input):

        if isinstance(user_input, list):
            if isinstance(user_input[0], str):
                user_input = [eval(i) for i in user_input]  

        if isinstance(user_input, str):
            converted_list = user_input.strip('][').split(', ')
            converted_list = [eval(i) for i in converted_list]
            user_input = converted_list

        new_val = [Converter.FP16_to_bytes(a) for a in user_input]
        flattened_list = [num for tup in new_val for num in tup]
        return flattened_list

      
    
    def FP16_to_bytes(user_input):

        # The input is converted to a float16 then turned into bytes in unicode.
        # We want to do this so we can split it up into two bytes later.
        x_bytes = (np.float16(user_input).tobytes())
                        
        # Convert the bytes to a 16bit integer
        x_int = int.from_bytes(x_bytes, byteorder='little', signed=False)

        # convert the 16bit integer to its binary representation
        binary_x = np.binary_repr(x_int, width=16)

        # Splitting up the 16 bits into two bytes and their 8bit integer numbers based on base 2
        byte_1 = int(binary_x[:8], 2)
        byte_2 = int(binary_x[8:], 2)

        # Converting the 8bit integers into 8bit unicode equivalent character
        # myasc1 = chr(byte_1)
        # myasc2 = chr(byte_2)

        return (byte_1, byte_2)

    # RECEIVING PART
    def bytes_to_FP16(received_character_1, received_character_2):
        
        # Converting the unicode characters into the unicode code integer
        # myByte = ord(received_character_1)
        # myByte2 = ord(received_character_2)
        
        byte_1 = received_character_1
        byte_2 = received_character_2

        # Converting the integers into 8bit binary representations, and combining them into a 16bit value as a string
        x_int = (format(byte_1, '#010b')[2:] + format(byte_2, '#010b')[2:])


        # convert the 16bit value string into a 16bit integer, then into a combination of two bytes.
        byte_str = int(x_int, 2).to_bytes(2, byteorder='little')

        # create a numpy float16 from the bytes
        x = np.frombuffer(byte_str, dtype=np.float16)[0]
        
        return x
