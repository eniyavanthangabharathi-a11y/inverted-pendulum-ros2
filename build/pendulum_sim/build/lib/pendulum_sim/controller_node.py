import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class ControllerNode(Node):

	def __init__(self):
		super().__init__('controller')
		self.subscription = self.create_subscription(Float64,'pendulum_angle', self.angle_callback,10)
		self.publisher_ = self.create_publisher(Float64, 'control_output',10)

		self.kp = 50.0
		self.ki = 0.0
		self.kd = 0.0

		self.prev_error = 0.0
		self.integral = 0.0
		self.dt = 0.1

		self.prev_angle = 0.0
		self.zero_crossing = 0
	def angle_callback(self,msg):
		angle = msg.data
		error = -angle

		self.integral += error * self.dt
		derivation = (error - self.prev_error)/self.dt
		output = self.kp * error + self.ki * self.integral + self.kd*derivation

		if self.prev_angle * angle< 0:
			self.zero_crossing +=1
			self.get_logger().info(f'Zero crossing #{self.zero_crossing}')
		
		command = Float64()
		command.data = output
		self.publisher_.publish(command)
		self.get_logger().info(f'Angle: {angle:.3f} Error:{error:.3f} PID output: {output:.3f} Command: {command.data}')

		self.prev_error = error
		self.prev_angle = angle

def main(args=None):
	rclpy.init(args=args)
	node = ControllerNode()
	rclpy.spin(node)

if __name__== '__main__':
	main()
