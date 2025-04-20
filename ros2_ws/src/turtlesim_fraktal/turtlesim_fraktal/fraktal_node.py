import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportRelative
import math
import time

class FraktalNode(Node):
    def __init__(self):
        super().__init__('fraktal_node')
        self.cli = self.create_client(TeleportRelative, 'turtle1/teleport_relative')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Várakozás a teleport_relative szolgáltatásra...')
        
        self.length = 1.0  # kis lépések
        self.level = 2     # fraktál szint (próbáld 1 vagy 2-vel)

        time.sleep(1.0)  # Biztos, ami biztos
        self.koch_curve(self.level, self.length)

    def teleport(self, linear, angular):
        req = TeleportRelative.Request()
        req.linear = linear
        req.angular = math.radians(angular)
        self.cli.call_async(req)
        time.sleep(0.5)  # kis szünet a mozdulat után

    def koch_curve(self, level, length):
        if level == 0:
            self.teleport(length, 0)
        else:
            self.koch_curve(level - 1, length)
            self.teleport(0, 60)
            self.koch_curve(level - 1, length)
            self.teleport(0, -120)
            self.koch_curve(level - 1, length)
            self.teleport(0, 60)
            self.koch_curve(level - 1, length)

def main(args=None):
    rclpy.init(args=args)
    node = FraktalNode()
    rclpy.spin(node)
    rclpy.shutdown()
