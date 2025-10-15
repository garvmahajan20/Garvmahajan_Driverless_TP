import rclpy
from rclpy.node import Node
from task5.msg import TaskOne
class Subscribing(Node):
        def _init_(self):
            super()._init_('sub_scribing')
            self.subscription=self.create_subscription(
                 TaskOne,
                 '/taskone',
                  self.listener_callback,
                  10)
            self.subscription
        def listener_callback(self,msg):
            longitudnal_velocity=msg.angvel*msg.radius
            self.get_logger().info(f'longitudnal velocity : {longitudnal_velocity}')
def main(args=None):
      rclpy.init(args=args)
      sub_scribing=Subscribing()
      rclpy.spin(sub_scribing)
      sub_scribing.destroy_node()
      rclpy.shutdown()

if __name__=='__main__':
      main()