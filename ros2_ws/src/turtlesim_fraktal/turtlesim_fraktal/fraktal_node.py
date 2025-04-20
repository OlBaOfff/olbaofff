import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import time

class FraktalNode(Node):
    def __init__(self):
        super().__init__('fraktal_node')
        self.publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        time.sleep(1)  # wait for publisher to connect
        self.koch_curve(level=2, length=2.0)

    def move_forward(self, distance):
        twist = Twist()
        twist.linear.x = distance
        twist.angular.z = 0.0
        self.publisher.publish(twist)
        time.sleep(1.0)  # időt adunk a mozgásra
        self.stop()

    def turn_left(self, angle_deg):
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = math.radians(angle_deg)
        self.publisher.publish(twist)
        time.sleep(1.0)  # időt adunk a fordulásra
        self.stop()

    def stop(self):
        twist = Twist()
        self.publisher.publish(twist)

    def koch_curve(self, level, length):
        if level == 0:
            self.move_forward(length)
        else:
            self.koch_curve(level - 1, length)
            self.turn_left(60)
            self.koch_curve(level - 1, length)
            self.turn_left(-120)
            self.koch_curve(level - 1, length)
            self.turn_left(60)
            self.koch_curve(level - 1, length)

def main(args=None):
    rclpy.init(args=args)
    node = FraktalNode()
    rclpy.spin(node)
    rclpy.shutdown()
