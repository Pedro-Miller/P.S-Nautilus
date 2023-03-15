#!/usr/bin/env python3

import math
import rospy
import tf2_ros
import geometry_msgs.msg

#cria a classe com seus atributos, um broadcaster e um TransformStamped
class Celestial:
    def __init__(self, name, parent, radius, speed):
        self.name = name
        self.parent = parent
        self.radius = radius
        self.speed = speed
        self.br = tf2_ros.TransformBroadcaster()
        self.t = geometry_msgs.msg.TransformStamped()

#define a função do movimento dos corpos em órbita e a hierarquia entre frames
    def movement(self):
        self.t.header.stamp = time
        self.t.header.frame_id = self.parent
        self.t.child_frame_id = self.name
        self.t.transform.translation.x = self.radius * math.cos(self.speed *time_elapsed)
        self.t.transform.translation.y = self.radius * math.sin(self.speed *time_elapsed)
        self.t.transform.translation.z = 0
        self.t.transform.rotation.x = 0
        self.t.transform.rotation.y = 0
        self.t.transform.rotation.z = 0
        self.t.transform.rotation.w = 1
        self.br.sendTransform(self.t)

if __name__ == '__main__':

    rospy.init_node('solar')
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        time = rospy.Time.now()
        time_elapsed = rospy.Time.now().to_sec()

        #lista com os corpos para facilitar adição de objetos
        celestial_bodies = [
        
        #mercury
        Celestial(rospy.get_param("/mercury/name"), rospy.get_param("/mercury/parent"), rospy.get_param("/mercury/radius"), rospy.get_param("/mercury/speed")),

        #venus
        Celestial(rospy.get_param("/venus/name"), rospy.get_param("/venus/parent"), rospy.get_param("/venus/radius"), rospy.get_param("/venus/speed")),
    
        #earth
        Celestial(rospy.get_param("/earth/name"), rospy.get_param("/earth/parent"), rospy.get_param("/earth/radius"), rospy.get_param("/earth/speed")),

        #moon
         Celestial(rospy.get_param("/moon/name"), rospy.get_param("/moon/parent"), rospy.get_param("/moon/radius"), rospy.get_param("/moon/speed")),

        #mars
         Celestial(rospy.get_param("/mars/name"), rospy.get_param("/mars/parent"), rospy.get_param("/mars/radius"), rospy.get_param("/mars/speed")),

         #phobos
         Celestial(rospy.get_param("/phobos/name"), rospy.get_param("/phobos/parent"), rospy.get_param("/phobos/radius"), rospy.get_param("/phobos/speed")),

         #deimos
         Celestial(rospy.get_param("/deimos/name"), rospy.get_param("/deimos/parent"), rospy.get_param("/deimos/radius"), rospy.get_param("/deimos/speed"))

         ]
        
        #chama o método de movimento para todos os objetos da classe
        for cel in celestial_bodies:
            cel.movement()

        rate.sleep()

   
