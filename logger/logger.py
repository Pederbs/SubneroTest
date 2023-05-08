from unetpy import UnetSocket
import csv
import datetime

sock = UnetSocket('192.168.42.86', 1100)

current_datetime = datetime.datetime.now().strftime("%d_%m_%Y__%H_%M_%S")
file = "SUMS_logger_" + current_datetime + '.csv'

header = 'Modem_ID,Time,Depth,Voltage,Oxygen,Salinity,Temerature'

with open(file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow([header])

while True:
    print('Listening...')
    rx = sock.receive()
    print(datetime.datetime.now().strftime("%H:%M:%S"), 'from node', rx.from_, ':', bytearray(rx.data).decode())
    #print('from node', rx.from_, ':', bytearray(rx.data))
    streng = str(rx.from_) + ','
    streng += bytearray(rx.data).decode()

    # Convert byte array to list of strings
    #str_list = [str(byte) for byte in rx]

    with open(file, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow([streng])

# Virker ikke bare for å se fin ut
sock.close()