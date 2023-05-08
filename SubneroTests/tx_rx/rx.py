from unetpy import UnetSocket

#s = UnetSocket('129.241.10.88', 1100) # for actual modem API port is 1100
s = UnetSocket('localhost', 1102)  #simulation API port
rx = s.receive()
print('from node', rx.from_, ':', bytearray(rx.data).decode())
s.close()
