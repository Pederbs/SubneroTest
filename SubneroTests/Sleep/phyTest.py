from unetpy import *
import time

sock = UnetSocket('129.241.10.88', 1100)
modem = sock.getGateway()

phy = modem.agentForService(Services.PHYSICAL)

while True:
    value = phy.voltage + 0.6
    
    print('V: %0.2f' % value)
    time.sleep(1)
