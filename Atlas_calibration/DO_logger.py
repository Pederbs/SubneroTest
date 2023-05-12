import doatlas01 
import datetime
import time
import csv

# Create a .csv file to log data
current_datetime = datetime.datetime.now().strftime("%d_%m_%Y__%H_%M_%S")
directory = 'logs/'
file = directory + 'DO_LOG_' + current_datetime + '.csv'
header = 'reading'

# Open the .csv file and put the header
with open(file, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow([header])

data = 0.0
T = 0.5             # Sample time

sensor = doatlas01.DOATLAS01()
print('Reading from Dissolved Oxugen sensor every %0.2f sec' % T)

while True:
    sensor.read()
    data = sensor._oxygen

    with open(file, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=';')
                writer.writerow([data])
    time.sleep(T)
