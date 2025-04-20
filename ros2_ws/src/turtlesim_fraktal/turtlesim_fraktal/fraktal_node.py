import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportRelative, TeleportAbsolute
from std_srvs.srv import Empty
from turtlesim.srv import Kill, Spawn
import math
import time

class FraktalNode(Node):
    def __init__(self):
        super().__init__('fraktal_node')
        
        self.teleport_rel = self.create_client(TeleportRelative, 'turtle1/teleport_relative')
        self.teleport_abs = self.create_client(TeleportAbsolute, 'turtle1/teleport_absolute')
        self.clear_client = self.create_client(Empty, '/clear')

        for client, name in [
            (self.teleport_rel, "teleport_relative"),
            (self.teleport_abs, "teleport_absolute"),
            (self.clear_client, "clear")
        ]:
            while not client.wait_for_service(timeout_sec=1.0):
                self.get_logger().info(f'Várakozás a {name} szolgáltatásra...')

        self.length = 0.8
        self.level = 2
        time.sleep(2.0)
        self.replace_turtle()
        self.clear_screen()
        time.sleep(0.5)
        self.koch_curve(self.level, self.length)
    
    def replace_turtle(self):
        #kill
        kill = self.create_client(Kill, 'kill')
        while not kill.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Várakozás a kill szolgáltatásra...')
        req_kill = Kill.Request()
        req_kill.name = 'turtle1'
        future = kill.call_async(req_kill)
        rclpy.spin_until_future_complete(self, future)

        #respawn
        spawn = self.create_client(Spawn, 'spawn')
        while not spawn.wait_for_service(timeout_sec=1.0):
         self.get_logger().info('Várakozás a spawn szolgáltatásra...')
        req_spawn = Spawn.Request()
        req_spawn.x = 12.5
        req_spawn.y = 6.0
        req_spawn.theta = float(math.radians(180.0))
        req_spawn.name = 'turtle1'
        future = spawn.call_async(req_spawn)
        rclpy.spin_until_future_complete(self, future)
        time.sleep(0.5)

    
    def clear_screen(self):
        req = Empty.Request()
        future = self.clear_client.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        time.sleep(0.2)

    def teleport(self, linear, angle_deg):
        req = TeleportRelative.Request()
        req.linear = float(linear)
        req.angular = float(math.radians(angle_deg))
        future = self.teleport_rel.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        time.sleep(0.2)

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
