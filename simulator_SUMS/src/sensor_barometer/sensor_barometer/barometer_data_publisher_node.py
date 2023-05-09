from rclpy.node import Node

from sensor_interfaces.msg import Barometer
import time

class BarometerDataPublisher(Node):
    # Initializer 
    def __init__(self):
        super().__init__('BarometerDataPublisher')
        self.publisher_ = self.create_publisher(Barometer, 'barometer_data', 10)    # Creates a publisher over the topic barometer_data
        self.sample_time  = self.declare_parameter('sample_time', 2.0).value  # Gets sample time as a parameter, default = 2
        self.timer = self.create_timer(self.sample_time, self.barometer_read_and_publish)

        
        self.j = 0
        self.i = 1

    def barometer_read_and_publish(self):
        # Custom barometer message to publish. Can be found in the sensor_interfaces.
        msg = Barometer()

        # Getting the local time  
        current_time = time.localtime()
        msg.local_time =  time.strftime("%H:%M:%S",current_time)


       
        self.j += self.i
        self.j = msg.depth
        # Publishing message and logging data sent over the topic /barometer_data
        self.publisher_.publish(msg)
        self.get_logger().info('\ttime: %s  Depth: %0.2f m  P: %0.1f mbar' % (msg.local_time,
                                                                            msg.depth, 
                                                                            msg.pressure_mbar))
