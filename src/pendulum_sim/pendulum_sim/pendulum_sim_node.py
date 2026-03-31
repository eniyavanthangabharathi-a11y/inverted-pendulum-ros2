import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

import math
import time

class PendulumSimNode(Node):

	def __init__(self):
		super().__init__('pendulum_sim')
		self.publisher_ = self.create_publisher(Float64, 'pendulum_angle',10)
		self.timer = self.create_timer(0.1, self.publish_angle)
		self.t = 0.0

	def publish_angle(self):
		angle = math.sin(self.t)
		msg = Float64()
		msg.data = angle
		self.publisher_.publish(msg)
		self.get_logger().info(f'Angle: {angle:.3f}')
		self.t += 0.1

def main(args = None):
	rclpy.init(args=args)
	node = PendulumSimNode()
	rclpy.spin(node)

if __name__ == '__main__':
	main()

