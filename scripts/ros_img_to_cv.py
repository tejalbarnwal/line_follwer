#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class cv_operations_node():
    def __init__(self):
        rospy.init_node("cv_operations_node" , anonymous=True)

        rospy.Subscriber('/camera/image_raw' , Image, self.callback_image)
        self.opencv_bridge = CvBridge()

    def callback_image(self , data):
        try:
            cv_image = self.opencv_bridge.imgmsg_to_cv2(data,'bgr8')
            self.perform_operations(cv_image)
        except CvBridgeError as e:
            print(e)

    def perform_operations(self,image):
        cv2.imshow("window",image)
        if cv2.waitKey(10) == 27:
            cv2.destroyAllWindows()


if __name__ == "__main__":
    opencv_node = cv_operations_node()
    try:
        rospy.spin()
    except rospy.ROSInterruptException as e:
        print(e)
