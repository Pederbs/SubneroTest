from lib import catlas01
import datetime
# import time
import csv

# Constants
T = 1           # Sample time
mT = 1.5        # Minimum sample time

# Create a .csv file to log data
current_datetime = datetime.datetime.now().strftime("%d_%m_%Y__%H_%M_%S")
directory = 'logs/'
file = directory + 'C_LOG_' + current_datetime + '.csv'
header = 'reading,time'

# Open the .csv file and put the header
with open(file, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow([header])

sensor = catlas01.CATLAS01()
if not sensor.init():
    # If sensor can not be detected
    print("[ERROR] Sensor could not be initialized")
    exit(1)

print('Sensor initialized successfully')

print('Reading from Conductivity sensor every %0.2f sec' % T)
# if T < mT:
#        print('Lowest sample time is %0.2f, reverting to it' % mT)

i = 0
while i <= 600:     # Sample time 1
    sensor.read()
    value = sensor._salinity
    print('%0.2f' % value)

    now = datetime.datetime.now()
    time_str = now.strftime('%H:%M:%S')

    data = str(value) + ',' + time_str

    with open(file, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=';')
                writer.writerow([data])
    i = i + 1
