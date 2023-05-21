

subscribers_updated = {
    'barometer_data' : True,
    'battery_data' : True,
    'oxygen_data' : True,
    'salinity_data' : True,
    'temperature_data' : True
}
n_sensors = 5
times_checked = 0


def send_data_modem():
        global n_sensors, times_checked, subscribers_updated
        times_checked += 1

        all_updated = True
        for topic, updated in subscribers_updated.items():
            if not updated:
                all_updated = False
                break
        if all_updated:
            print('ALL SENSORS OK')
            #string = str(barometer_data['depth']) + ', ' + str(oxygen_data['oxygen']) + ', ' +str(salinity_data['salinity']) + ', ' + str(temperature_data['temperature'])
            try:
                #sock.send('Hello from ROS', 0)
                print('MSG SENT TO MODEM')
            except:
                print('COULD NOT SEND DATA TO MODEM')
            times_checked = 0

            for topic in subscribers_updated:
                subscribers_updated[topic] = False
            return

        elif times_checked > n_sensors: # 5 sensors?
            print('SOME SENSORS NOT WORKING')
            #string = str(barometer_data['depth']) + ', ' + str(oxygen_data['oxygen']) + ', ' +str(salinity_data['salinity']) + ', ' + str(temperature_data['temperature'])
            try:
                #sock.send('Hello from ROS', 0)
                print('MSG SENT TO MODEM')
            except:
                print('COULD NOT SEND DATA TO MODEM')
            #print('DATA SENT TO MODEM: %s' % string)
            times_checked = 0
            return
            
while True:
    send_data_modem()