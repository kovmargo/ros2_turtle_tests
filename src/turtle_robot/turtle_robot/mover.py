import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class Mover(Node):
    def __init__(self):
        super().__init__('mover')
        self.get_logger().info('Mover started')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.send_command)
        self.subscription = self.create_subscription(Pose, '/turtle1/pose', self.on_pose, 10)

    def send_command(self):
        msg = Twist()
        msg.linear.x = 0.5
        msg.angular.z = 1.0
        self.publisher.publish(msg)

    def on_pose(self, msg):
        self.get_logger().info(f'x={msg.x:.2f}, y={msg.y:.2f}, theta={msg.theta:.2f}', throttle_duration_sec=1.0)


def main():
    rclpy.init()
    node = Mover()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
