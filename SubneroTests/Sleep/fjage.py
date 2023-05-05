from unetpy import *
'''
ShellExecReq = MessageClass('org.arl.fjage.shell.ShellExecReq')
msg = ShellExecReq()

gw = Gateway('129.241.10.69', 1100)

msg = Message()
msg.
'''


sock = UnetSocket('129.241.10.88', 1100)
modem = sock.getGateway()

modem.
gw = sock.gateway
gw.subscribe(phy)