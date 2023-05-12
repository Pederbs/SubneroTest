from lib import catlas01
import datetime
import time
import csv

# Create a .csv file to log data
current_datetime = datetime.datetime.now().strftime("%d_%m_%Y__%H_%M_%S")
directory = 'logs/'
file = directory + 'C_LOG_' + current_datetime + '.csv'
header = 'reading'

# Open the .csv file and put the header
with open(file, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow([header])

data = 0.0
T = 0.5             # Sample time
mT = 0.5

sensor = catlas01.CATLAS01()
if not sensor.init():
    # If sensor can not be detected
    print("[ERROR] Sensor could not be initialized")
    exit(1)

print('Sensor initialized successfully')

print('Reading from Conductivity sensor every %0.2f sec' % T)
if T < mT:
       print('Lowest sample time is %0.2f?, reverting to it' % mT)

while True:
    sensor.read()
    data = sensor._salinity
    print(data)

    with open(file, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=';')
                writer.writerow([data])
    time.sleep(T)
