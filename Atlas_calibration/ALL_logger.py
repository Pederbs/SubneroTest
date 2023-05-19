from lib import doatlas01
from lib import catlas01
import datetime
import datetime
# import time
import csv

# Constants
T = 1             # Sample time
# mT = 1.5        # Minimum sample time


# Create a .csv file to log data
current_datetime = datetime.datetime.now().strftime("%d_%m_%Y__%H_%M_%S")
directory = 'logs/'
file = directory + 'DO_LOG_' + current_datetime + '.csv'
header = 'DO,C,time'

# Open the .csv file and put the header
with open(file, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow([header])

DO_sensor = doatlas01.DOATLAS01()
C_sensor = catlas01.CATLAS01()
if not DO_sensor.init():
    # If sensor can not be detected
    print("[ERROR] DO Sensor could not be initialized")
    exit(1)

if not C_sensor.init():
    # If sensor can not be detected
    print("[ERROR] C Sensor could not be initialized")
    exit(1)

print('Sensor initialized successfully')

print('Reading from Dissolved Oxygen sensor every %0.2f sec' % T)
# if T < mT:
#        print('Lowest sample time is %0.2f, reverting to it' % mT)

i = 0
while i <= 600:     # Sample time 1 sec
    DO_sensor.read()
    DO_value = DO_sensor._oxygen

    C_sensor.read()
    C_value = C_sensor._salinity
    print('DO Sample: %i, %0.2f' % (i,DO_value))
    print('C Sample: %i, %0.2f' % (i,C_value))

    now = datetime.datetime.now()
    time_str = now.strftime('%H:%M:%S')

    data = str(DO_value) + ',' + str(C_value) + ',' + time_str

    with open(file, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=';')
                writer.writerow([data])
    i = i + 1
