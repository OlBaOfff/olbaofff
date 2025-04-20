import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import time

class FraktalNode(Node):
    def __init__(self):
        super().__init__('fraktal_node')
        self.publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        time.sleep(1.0)  # várunk a kapcsolatra

        self.speed = 0.5  # kis sebesség
        self.turn_speed = 1.0  # kis fordulási sebesség
        self.move_time = 1.0   # kis lépés
        self.turn_time = math.pi / 3 / self.turn_speed  # kb. 60 fok
        self.koch_curve(2)  # fraktál szint: 2

    def move_forward(self):
        twist = Twist()
        twist.linear.x = self.speed
        twist.angular.z = 0.0
        self.publisher.publish(twist)
        time.sleep(self.move_time)
        self.stop()

    def turn(self, angle_deg):
        angle_rad = math.radians(angle_deg)
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = self.turn_speed if angle_rad > 0 else -self.turn_speed
        self.publisher.publish(twist)
        time.sleep(abs(angle_rad / self.turn_speed))
        self.stop()

    def stop(self):
        twist = Twist()
        self.publisher.publish(twist)
        time.sleep(0.2)  # kis szünet a mozdulat után

    def koch_curve(self, level):
        if level == 0:
            self.move_forward()
        else:
            self.koch_curve(level - 1)
            self.turn(60)
            self.koch_curve(level - 1)
            self.turn(-120)
            self.koch_curve(level - 1)
            self.turn(60)
            self.koch_curve(level - 1)

def main(args=None):
    rclpy.init(args=args)
    node = FraktalNode()
    rclpy.spin(node)
    rclpy.shutdown()
