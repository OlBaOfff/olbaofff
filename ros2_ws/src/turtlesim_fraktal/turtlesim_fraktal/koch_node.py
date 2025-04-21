import rclpy
import math
import time
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtleController:
    def __init__(self, node: Node, speed: float = 2.0, unit_length: float = 0.1):
        self.node = node
        self.publisher = node.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.speed = speed
        self.unit_length = unit_length
        self.turn_speed_deg = 60.0  

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


class KochFractal:
    def __init__(self, controller: TurtleController):
        self.ctrl = controller

    def draw_curve(self, steps: int, depth: int):
        if depth == 0:
            self.ctrl.move_forward(steps)
        else:
            unit = steps // 3
            self.draw_curve(unit, depth - 1)
            self.ctrl.rotate(60)
            self.draw_curve(unit, depth - 1)
            self.ctrl.rotate(-120)
            self.draw_curve(unit, depth - 1)
            self.ctrl.rotate(60)
            self.draw_curve(unit, depth - 1)

    def draw_snowflake(self, steps: int, depth: int):
        for _ in range(3):
            self.draw_curve(steps, depth)
            self.ctrl.rotate(-120)

class KochSnowflakeNode(Node):
    def __init__(self):
        super().__init__('koch_snowflake_node')
        self.get_logger().info
        time.sleep(2)

        #inicializálás
        controller = TurtleController(self)
        fractal = KochFractal(controller)

        #rajzolás
        self.get_logger().info
        fractal.draw_snowflake(steps=27, depth=3)
        self.get_logger().info

def main():
    rclpy.init()
    node = KochSnowflakeNode()

    try:
        rclpy.spin_once(node, timeout_sec=1.0)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

