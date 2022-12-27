# Object-Detection
OpenCV Vehicle Detection and Classification Project
In this project, we’ll detect and classify cars, HMV ( Heavy Motor Vehicle) , LMV (Light Motor Vehicle) on the road, and count the number of vehicles traveling through a road. And the data will be stored to analyze different vehicles that travel through the road.

We’ll create two programs to do this project. The first one will be the tracker for vehicle detection using OpenCV that keeps track of each and every detected vehicle on the road and the 2nd one will be the main detection program.

Prerequisites for Vehicle Detection and Classification Project using OpenCV:
1. Python – 3.x (We used python 3.8.8 in this project)
2. OpenCV – 4.4.0

It is strongly recommended to run DNN models on GPU.
You can install OpenCV via “pip install opencv-python opencv_contrib-python”.
3. Numpy – 1.20.3
4. YOLOv3 Pre-trained model weights and Config Files.

Download Vehicle Detection & Classification Python OpenCV Code
Please download the source code of opencv vehicle detection & classification: Vehicle Detection and Classification OpenCV Code

Tracker:
The tracker basically uses the Euclidean_distance concept to keep track of an object. It calculates the difference between two center points of an object in the current frame vs the previous frame, and if the distance is less than the threshold distance then it confirms that the object is the same object of the previous frame.


Vehicle Counter:

Steps for Vehicle Detection and Classification using OpenCV:
1. Import necessary packages and Initialize the network.
2. Read frames from a video file.
3. Pre-process the frame and run the detection.
4. Post-process the output data.
5. Track and count all vehicles on the road
6. Save the final data to a CSV file.
