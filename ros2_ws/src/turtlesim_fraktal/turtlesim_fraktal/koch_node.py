import rclpy
import math
import time
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtleController:
    def __init__(self, node: Node, speed: float = 1.0, unit_length: float = 0.1):
        self.node = node
        self.publisher = node.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.speed = speed
        self.unit_length = unit_length
        self.turn_speed_deg = 30.0  

    def move_forward(self, steps: int): #előre mozdítja a tekit
        twist = Twist()
        twist.linear.x = self.speed
        step_duration = self.unit_length / self.speed

        for _ in range(steps):
            self.publisher.publish(twist)
            time.sleep(step_duration)

        self.stop()

    def rotate(self, angle_degrees: float): #teki forgatás
        twist = Twist()
        twist.angular.z = math.radians(angle_degrees)
        duration = abs(angle_degrees) / self.turn_speed_deg

        self.publisher.publish(twist)
        time.sleep(duration)
        self.stop()

    def stop(self):
        self.publisher.publish(Twist())
        time.sleep(0.05)



