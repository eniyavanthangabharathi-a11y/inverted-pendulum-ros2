import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64, String

class ControllerNode(Node):

    def __init__(self):
        super().__init__('controller')
        self.subscription = self.create_subscription(
            Float64,
            'pendulum_angle',
            self.angle_callback,
            10)
        self.publisher_ = self.create_publisher(String, 'control_output', 10)
        self.prev_angle = 0.0
        self.zero_crossings = 0

    def angle_callback(self, msg):
        angle = msg.data
        command = String()

        if self.prev_angle * angle < 0:
            self.zero_crossings += 1
            self.get_logger().info(f'Zero crossing #{self.zero_crossings}')

        if angle > 0.1:
            command.data ='push_left'
            self.get_logger().info(f'Angle: {angle:.3f} — push_left')
        elif angle < -0.1:
            command.data = 'push_right'
            self.get_logger().info(f'Angle: {angle:.3f} — push_right')
        else:
            command.data = 'hold'
            self.get_logger().info(f'Angle: {angle:.3f} — BALANCED, hold')

        self.publisher_.publish(command)
        self.prev_angle = angle

def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
