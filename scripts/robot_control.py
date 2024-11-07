import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class RobotControl(Node):
    def __init__(self):
        super().__init__('robot_control')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.move_robot)
        self.twist = Twist()

    def move_robot(self):
        self.twist.linear.x = 0.5   # Move forward at 0.5 m/s
        self.twist.angular.z = 0.1  # Rotate at 0.1 rad/s
        self.publisher_.publish(self.twist)

def main(args=None):
    rclpy.init(args=args)
    robot_control = RobotControl()
    rclpy.spin(robot_control)
    robot_control.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()