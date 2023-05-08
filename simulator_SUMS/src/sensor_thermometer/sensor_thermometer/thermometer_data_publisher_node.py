# This code is responsible for getting the data from the sensor and publishing it.
from rclpy.node import Node

# tsys01 needed in order to utilize the BlueRobotics TSYS01 Python Library which must be installed
#from sensor_thermometer import tsys01
from sensor_interfaces.msg import Thermometer
import time

class ThermometerDataPublisher(Node):
    # Initializer 
    def __init__(self):
        super().__init__('ThermometerDataPublisher')
        self.publisher_ = self.create_publisher(Thermometer, 'thermometer_data', 10)    # Creates a publisher over the topic thermometer_data
        self.sample_time  = self.declare_parameter('sample_time', 2.0).value  # Gets sample time as a parameter, default = 2
        self.timer = self.create_timer(self.sample_time, self.thermometer_read_and_publish)

        self.i = 1.0
        self.j = 0.0

    def thermometer_read_and_publish(self):
        # Custom thermometer message to publish. Can be found in the brov2_interfaces.
        msg = Thermometer()

        # Getting the local time 
        current_time = time.localtime()
        msg.local_time =  time.strftime("%H:%M:%S",current_time)

        
        self.j += self.i
        msg.temperature_celsius = self.j

        # Publishing message and logging data sent over the topic /thermometer_data
        self.publisher_.publish(msg)
        self.get_logger().info('\ttime: %s  T: %0.2f C' % (msg.local_time,
                                                        msg.temperature_celsius))

