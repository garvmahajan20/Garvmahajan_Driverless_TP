import rclpy
from rclpy.node import Node
from task5.msg import TaskOne
class Publishing(Node):

       def _init_(self):
            super()._init_('pub_lishing')
            self.publisher_=self.create_publisher(TaskOne,'/taskone',10)
            self.timer=self.create_timer(1,self.timer_callback)
       def timer_callback(self):
            av=float(input("enter angular velocity : "))
            r=float(input("enter radius : "))
            msg=TaskOne()
            msg.angvel=av
            msg.radius=r
            self.publisher_.publish(msg)
            self.get_logger().info(f'recieved angular velocity : {msg.angvel} , recieved radius : {msg.radius}')
def main(args=None):
       rclpy.init(args=args)
       pub_lishing=Publishing()
       rclpy.spin(pub_lishing)
       pub_lishing.destroy_node()
       rclpy.shutdown()

if __name__=='__main__':
    main()