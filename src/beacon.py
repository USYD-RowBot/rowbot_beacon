#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from rowbot_lcm_ros_bridge.srv import RelayCommandRequest,RelayCommandResponse,RelayCommand

class BeaconServer:
    def __init__(self):
        self.colour = "red"
        rospy.loginfo("Waiting for relay service")
        rospy.wait_for_service('add_two_ints')
        rospy.loginfo("Found relay_service")

        relay_service_name = rospy.get_param('service_name','relay_command')
        self.service_client = rospy.ServiceProxy(relay_service_name, RelayCommand)
        pass
    def callback(self,msg):
        self.colour = msg.data
        pass
    def publish(self):
        red_pin = rospy.get_param('red_pin',21)
        orange_pin = rospy.get_param('orange_pin',22);
        green_pin = rospy.get_param('green_pin',23)
        buzzer_pin = rospy.get_param('buzzer_pin',24)
        red_req = RelayCommandRequest()
        orange_req = RelayCommandRequest()
        green_req = RelayCommandRequest()
        buzzer_req = RelayCommandRequest()
        red_req.relay_number = red_pin
        orange_req.relay_number = orange_pin
        green_req.relay_number = green_pin
        buzzer_req.relay_number = buzzer_pin
        if self.colour == "red":
            red_req.relay_request = True
            self.service_client
            pass
        if self.colour == "orange":
            orange_req.relay_request = True
            pass
        if self.colour =="green":
            green_req.relay_request = True
            pass
        self.service_client(red_req)
        self.service_client(orange_req)
        self.service_client(green_req)
        self.service_client(buzzer_req)
        pass



if __name__=="__main__":
    rospy.init_node('beacon_control')
    rate_num = rospy.get_param('rate',10)
    beacon_server = BeaconServer()
    rospy.Subscriber("beacon_control",String,beacon_server.callback)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        beacon_server.publish()
        rate.sleep()
