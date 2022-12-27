# Object-Detection
Vehicle Counting, Classification & Detection using OpenCV & Python
Today, we’re going to build an advanced vehicle detection and classification project using OpenCV. We’ll use the YOLOv3 model with OpenCV-python. Open-CV is a real-time computer vision library of Python. We can use YOLO directly with OpenCV.

What is YOLO?
YOLO stands for You Only Look Once. It is a real-time object recognition algorithm. It can classify and localize multiple objects in a single frame. YOLO is a very fast and accurate algorithm for its simpler network architecture.

How does YOLO work?
YOLO works using mainly these techniques.

1. Residual Blocks – Basically, it divides an image into NxN grids.

2. Bounding Box regression – Each grid cell is sent to the model. Then YOLO determines the probability of the cell contains a certain class and the class with the maximum probability is chosen.

3. Intersection Over Union (IOU) – IOU is a metric that evaluates intersection between the predicted bounding box and the ground truth bounding box. A Non-max suppression technique is applied to eliminate the bounding boxes that are very close by performing the IoU with the one having the highest class probability among them.

intersection over union
