import rclpy 
from rclpy.node import Node
from std_msgs.msg import String

class MotorNode(Node):

	def __init__(self):
		super().__init__('motor')
		self.subscription = self.create_subscription(String,'control_output',self.command_callback,10)
	def command_callback(self, msg):
		command = msg.data
		if command =='push_left':
			pwm = 200
		elif command =='push_right':
			pwm  = -200
		else:
			pwm  = 0
		self.get_logger().info(f'Command: {command} -> 	PWM: {pwm}')

def main(args=None):
	rclpy.init(args=args)
	node = MotorNode()
	rclpy.spin(node)

if __name__ == '__main__':
	main()



