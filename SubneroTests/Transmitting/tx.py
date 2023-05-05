from unetpy import UnetSocket

s = UnetSocket('129.241.10.88', 1100) # for actual modem API port is 1100
#s = UnetSocket('localhost', 1101)  #simulation API port
s.send('Hello Underwater!', 0)
s.close()
