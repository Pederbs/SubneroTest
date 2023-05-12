# How to calibrate the Atlas Scientific sensors with the Ubuntu server RPi

## UART

I am doing this on a brand new RPi so i first ran 
```
sudo apt-get update
``` 
and then 
```
sudo apt-get upgrade
``` 
Theese commands updates all apt packages?? and it will take some time...

When connecting the EZO board to power through the isolated carrier board it is lighting Green this means that it is in UART mode and to switch it to i2c mode i have to first communicate in UART(I think). Therfore it might just be easy to calibrate in UART.

the tutorial tells me to use command `sudo nano /boot/cmdline.txt` but it did not work... Tried 
```
sudo nano /boot/firmware/cmdline.txt
```
I seem to be in the same file.

The file contains:

```
console=serial0,115200 dwc_otg.lpm_enable=0 console=tty1 root=LABEL=writable rootfstype=ext4 rootwait fixrtc quiet splash
```
The tutorial tells me that `console=serial0,115200` can cause conflict with the serial port so i should **DELETE** it.
Now it should look like this:

```
dwc_otg.lpm_enable=0 console=tty1 root=LABEL=writable rootfstype=ext4 rootwait fixrtc quiet splash
```
press **CTRL+X** then **Y** and hit enter to save.

Tried to install pyserial but found out that pip was not installed, installed it with:

```
sudo apt install python3-pip
```
Then i installed PySerial:
```
sudo pip install pyserial
```
The requirement is already satisfied...
Running:
```
cd ~/Raspberry-Pi-sample-code
sudo pyhton3 uart.py
```

got to open the file but it does not seem to work:/
Tried to enable a specific uart (uart5), used this command 
```
sudo nano /boot/firmware/config.txt
```
To add theese lines to the file ans save and exit
```
# Enable the serial pins
enable_uart=1
dtoverlay=uart5
```
and restarted the Pi with 
```
sudo reboot
```
went in to the `/Raspberry-Pi-sample-code/uart.py` and changed the call in line 70 in `if __name__ == "__main__" `
```
usbport = ‘/dev/ttyAMA0’
    |
    V
usbport = ‘/dev/ttyAMA1’
```
After this the script `/Raspberry-Pi-sample-code/uart.py` can be run without problems.

Now type in "C,1". This enables the sensor to take a reading every second.
Type in "Poll,1" to display these readings. 
When the readings stabalize, type in "Cal".
Open the zero dissolved oxygen pouch and dip the sensor in the solution.
Wait until the sensor readings stabalize and type in "Cal,0"

### Change communication from I2C to UART
short SDA and PGND 
refer to page 62 of DO_EZO_Datasheet

or run command `I2C,97` in the urat.py program

## I2C
Attempted i2c calibration after UART calibration was successful due to having a script that is easier to work with in i2c

ran the commands:
```
# sudo apt-get install python3-smbus
sudo apt-get install python-smbus
sudo apt-get install i2c-tools
```
opened `uart.py` and ran `I2C,97` for (DO) and had to rewire the connection

this seemed to work better




## fra tidligere gruppe 
HOW TO CHECK FOR I2C 101

Når du har terminal oppe skriv: `sudo i2cdetect -y 1`

Fra det skal du få opp en tabell, dersom det er en sensor tilkoblet skal den dukke opp som et tall. Dersom ingen tall dukker kan du se om I2C konfigurasjonen på Raspberryen er skrudd av.

Dette sjekker du ved å skrive: sudo raspi-config
Du kommer da til en meny der du navigerer først til "Interfacing options" --> "I2C" og trykk enable. Deretter naviger ut av meny og "sudo reboot"



# Kjapp Test

prøvde å koke litt vann og blande det ut med kalt vann så det ble litt mer enn lunket og hadde en skål med kalt vann, prøvde å dyppe proben ned i begge uten noe spesielt hell
Vil si at testen var inconclusive