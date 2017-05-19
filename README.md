# canny_edge_my_face

The purpose of this package is to use an
embeded camera (such as a laptop camera)
to display a filtered (using canny filter)
version of the image being sensed.

And to canny edge my, your and anyone's
face.

The package consists of a single node
in python that uses opencv to apply
a canny edge filter to an input image
and produce an ouput image.

To run this node use the canny_my_face.launch
file. This files uses the cv_camera
nodelet and stream images to a /camera/image_raw
topic. Our python node subscribes
to this node and publishes filtered
images in the /canny_faced topic.

An example is shown in image.png

Use:

1. compile using catkin_make usual approach
2. run the cv_camera nodelet and canny python file with

roslaunch canny_edge_my_face canny_my_face.launch

3. run rqt image viewer to see the ouput

rqt_image_view /canny_faced