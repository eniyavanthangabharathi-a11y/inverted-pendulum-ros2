import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class ControllerNode(Node):

	def __init__(self):
		super().__init__('controller')
		self.subscription = self.create_subscription(
					Float64,'pendulum_angle',
					self.angle_callback,
					10)
	def angle_callback(self, msg):
		angle = msg.data
		if angle >0.1:
			self.get_logger().info(f'Angle: {angle:.3f} - Leaning RIGHT, push left')
		
		elif angle <0.1:
			self.get_logger().info(f'Angle: {angle:.3f} - Leaning LEFT, push right')
		
		else:
			self.get_logger().info(f'Angle: {angle:.3f} - BALANCED')

def main(args =None):
	rclpy.init(args=args)
	node = ControllerNode()
	rclpy.spin(node)
if __name__ == '__main__':
	main()
