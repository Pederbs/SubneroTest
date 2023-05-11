class Graycode():

    # Converts a number to the number the graycode represents 
    def equivalent(self, num):
        return num ^ (num >> 1)

    # Converts a number to a binary string of bits length 
    # Only works for bits < 10
    def to_bin(self, num, bits):
        graycode = self.equivalent(num)
        bit_str = '0' + str(bits) + 'b' 
        binary_str = format(graycode, bit_str)
        return binary_str

    # Compresses a number between two given values to a number of n bits with a gain
    def compress(self, number: float, lowerlim: float, upperlim: float, bits: int, gain: int):
        if number < lowerlim:
            number = lowerlim
        elif number > upperlim:
            number = upperlim

        percent = (number - lowerlim)/(upperlim - lowerlim)

        finalNumber = round(percent*(2**bits-1)*gain)
        #if finalNumber < 0:
        #    finalNumber = 0
        return finalNumber


    # Converts graycode to int
    def to_int(self, gray_code):
        binary_code = gray_code[0]
        for i in range(1, len(gray_code)):
            if gray_code[i] == '1':
                binary_code += '1' if binary_code[i-1] == '0' else '0'
            else:
                binary_code += binary_code[i-1]
        return int(binary_code, 2)



    def unpack(self, number: str, lowerlim: float, upperlim: float, bits: int, gain: int):
        number_int = self.to_int(number)

        percent = number_int/(2**bits-1)
        value = (lowerlim + percent*(upperlim - lowerlim))/gain
        return value