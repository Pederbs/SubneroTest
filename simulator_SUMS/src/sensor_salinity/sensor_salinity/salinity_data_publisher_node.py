from rclpy.node import Node

from sensor_interfaces.msg import Salinity
import time

class SalinityDataPublisher(Node):
    # Initializer 
    def __init__(self):
        super().__init__('SalinityDataPublisher')
        self.publisher_ = self.create_publisher(Salinity, 'salinity_data', 10)  # Creates a publisher over the topic salinity_data
        self.sample_time  = self.declare_parameter('sample_time', 2.0).value  # Gets sample time as a parameter, default = 2
        self.timer = self.create_timer(self.sample_time, self.salinity_read_and_publish)

        
        self.j = 0
        self.i = 1

    def salinity_read_and_publish(self):
        # Custom conductivity message to publish. Can be found in the brov2_interfaces.
        msg = Salinity()

        # Getting the local time 
        current_time = time.localtime()
        msg.local_time =  time.strftime("%H:%M:%S",current_time)

       
        self.j += self.i
        self.j = msg.salinity_value

        # Publishing message and logging data sent over the topic /salinity_data
        self.publisher_.publish(msg)
        self.get_logger().info('\ttime: %s  S: %0.2f µs/cm' % (msg.local_time,
                                                                msg.salinity_value))
