import rclpy 
from rclpy.node import Node
from std_msgs.msg import Float64

class MotorNode(Node):

	def __init__(self):
		super().__init__('motor')
		self.subscription = self.create_subscription(Float64,'control_output',self.command_callback,10)
	def command_callback(self, msg):
		pwm= msg.data
		self.get_logger().info(f'PWM: {pwm:.3f}')

def main(args=None):
	rclpy.init(args=args)
	node = MotorNode()
	rclpy.spin(node)

if __name__ == '__main__':
	main()



