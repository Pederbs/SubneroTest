from rclpy.node import Node

from sensor_interfaces.msg import Oxygen
import time

class OxygenDataPublisher(Node):
    # Initializer 
    def __init__(self):
        super().__init__('OxygenDataPublisher')
        self.publisher_ = self.create_publisher(Oxygen, 'oxygen_data', 10)  # Creates a publisher over the topic oxygen_data
        self.sample_time  = self.declare_parameter('sample_time', 2.0).value  # Gets sample time as a parameter, default = 2
        self.timer = self.create_timer(self.sample_time, self.oxygen_read_and_publish)

        self.j = 0
        self.i = 1

    def oxygen_read_and_publish(self):
        # Custom dissolved oxygen message to publish. Can be found in the brov2_interfaces.
        msg = Oxygen()
        
        # Getting the local time 
        current_time = time.localtime()
        msg.local_time =  time.strftime("%H:%M:%S",current_time)

        
        self.j += self.i
        self.j = msg.oxygen_concentration

        # Publishing message and logging data sent over the topic /oxygen_data
        self.publisher_.publish(msg)
        self.get_logger().info('\t\ttime: %s  O: %0.2f mg/L' % (msg.local_time,
                                                            msg.oxygen_concentration))
