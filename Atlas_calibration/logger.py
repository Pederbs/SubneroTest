import catlas01
import doatlas01 
import datetime
import time
import csv

# Create a .csv file to log data
current_datetime = datetime.datetime.now().strftime("%d_%m_%Y__%H_%M_%S")
directory = 'logs/'
file = directory + 'LOG_' + current_datetime + '.csv'
header = 'reading'

# Open the .csv file and put the header
with open(file, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow([header])

# Ask user for what sensor they are using
choise = input('Choose what sensor to use (doatlas/catlas)')
ok = True           # Answer is as expected
salinity = None     # It is the salinity sensor
data = 0.0
T = 0.5             # Sample time

while ok:
    if choise == 'doatlas':
        sensor = doatlas01.DOATLAS01()
        ok = True
        salinity = False

    elif choise == 'catlas':
        sensor = catlas01.CATLAS01()
        ok = True
        salinity = True

    else:
        print('Please choose a valid sensor')
        ok = False


while True:
    sensor.read()
    if salinity:
        data = sensor._salinity
    else:
        data = sensor._oxygen

    with open(file, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=';')
                writer.writerow([data])
    time.sleep(T)
    