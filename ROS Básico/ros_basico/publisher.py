#!/usr/bin/python3

import rospy
import random
from geometry_msgs.msg import Twist, Vector3
from std_msgs.msg import Float32

class Speaker:
    def __init__(self):
        rospy.init_node('publisher', anonymous=True)
        self.publisher = rospy.Publisher('vetores', Twist, queue_size=10)
        self.modulos = rospy.Subscriber('modulos', Vector3, self.callback)

    def publicar(self):
        
        fonte = list(range(100))
        rate = rospy.Rate(5)
        velocidades = Twist()

        while not rospy.is_shutdown():
            velocidades.linear.x = random.randrange(0, 100)
            velocidades.linear.y = random.randrange(0, 100)
            velocidades.linear.z = random.randrange(0, 100)
            velocidades.angular.x = random.randrange(0, 100)
            velocidades.angular.y = random.randrange(0, 100)
            velocidades.angular.z = random.randrange(0, 100)

            
            self.publisher.publish(velocidades)
            #rospy.loginfo(velocidades)
            rate.sleep()
    
    def callback(self, msg):
        modulo_linear = Float32()
        modulo_angular = Float32()

        modulo_linear = msg.x
        modulo_angular = msg.y

        print("O módulo do vetor velocidade linear é", modulo_linear,"e o módulo do vetor velocidade angular é", modulo_angular)


if __name__ == '__main__':
    pub = Speaker()
    pub.publicar()