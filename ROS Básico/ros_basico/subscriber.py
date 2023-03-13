#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Twist, Vector3
import math
from std_msgs.msg import Float32

class Listener:

    def __init__(self):

        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber('vetores', Twist, self.callback)
        self.publisher = rospy.Publisher('modulos', Vector3, queue_size=10)

    def callback(self, msg):

        lx , ly, lz = msg.linear.x, msg.linear.y, msg.linear.z
        ax , ay, az = msg.angular.x, msg.angular.y, msg.angular.z

        modulo_linear = Float32()
        modulo_angular = Float32()

        modulo_linear = math.sqrt(lx*lx + ly*ly + lz*lz)
        modulo_angular = math.sqrt(ax*ax + ay*ay + az*az)
        resultados= Vector3()
        resultados.x = modulo_linear
        resultados.y = modulo_angular

       
        self.publisher.publish(resultados)
        #rospy.loginfo(resultados)
           

if __name__ == '__main__':
    sub = Listener()
    rospy.spin()