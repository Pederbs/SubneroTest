from unetpy import *

sock = UnetSocket('129.241.10.88', 1100)
modem = sock.getGateway()

phy = modem.agentForService(Services.PHYSICAL)

sch = modem.agentsForService('org.arl.unet.Services.SCHEDULER')

#print(sch.addsleep)
print(phy << AddScheduledSleepReq()) # WORKS
#print(phy << RemoveScheduledSleepReq()) 
#print(phy << GetSleepScheduleReq())
#print(phy << addsleep)
