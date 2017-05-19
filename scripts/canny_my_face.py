#!/usr/bin/env python
'''
:author: Jose Pereira
:maintainer: Jose Pereira(josenunopereira@gmail)
:description: The canny_my_face.py node simply subscribes
			  from a camera image streaming (in this case)
			  provided by the cv_camera nodelet and published
			  in the /camera/image_raw topic), converts
			  received images into opencv type images and
			  applies a canny edge filter. It publishes
			  the result as sensor_msgs/Image msgs in an
			  output topic (in this case /canny_faced).
'''

import rospy
import cv2
from functools import partial
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def raw_image_cb(data, publisher, bridge):
	'''Callback for input images topic, all processing done here'''
	try:
		# Image message to opencv type transformation
		img = bridge.imgmsg_to_cv2(data, "bgr8")
	except CvBridgeError as error:
		print error

	# Applying canny edge filter	
	face = cv2.Canny(img, 100, 250)

	try:
		# opencv type to Image message conversion and publishing
		publisher.publish(bridge.cv2_to_imgmsg(face, "mono8"))
	except CvBridgeError as error:
		print error

if __name__ == '__main__':
	try:
		rospy.init_node('canny_my_face')

		bridge = CvBridge()

		pub = rospy.Publisher('canny_faced', Image, queue_size = 10)
		sub = rospy.Subscriber('/camera/image_raw', Image, partial(raw_image_cb, publisher = pub, bridge = bridge))

		rospy.spin()

	except rospy.ROSInterruptException:
		pass