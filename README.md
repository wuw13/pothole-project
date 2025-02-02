
# Pothole Object Detection
This is for a summer camp and made in >1d, not of high quality work.

<br/>

### Description
Simple student project made to detect potholes in roads. (WIP. alerting system)
Ideally placed on the windshield of cars to detect potholes in the road in front and notify the driver.

<br/>

### YOLO
The model is powered by [YOLOv10](https://github.com/THU-MIG/yolov10).
Here is how YOLO works (simplified by a lot):

1. **Input Processing**
The input image is resized to a standard size (e.g., 640x640 pixels).
The image is normalized (scaled to a value between 0 and 1) and converted to a 2D array.

2. **Feature Extraction**
A CNN (Convolution Neural Network) backbone extracts features from the input image.
The backbone extracts feature maps at different scales. See 3Blue1Brown's [video](https://www.youtube.com/watch?v=KuXjwB4LzSA) for details.

3. **Neck**
A FPN (Feature Pyramid Network) combines features from different scales.
This helps in detecting objects of various sizes. This combines the extracted features into one map.

4. **Head**
The detection head processes the feature maps to predict bounding boxes, class probabilities, and segmentation masks.
It uses a decoupled head design, separating class prediction and box regression.

5. **Post-processing**
NMS (Non-Maximum Suppression) is applied to filter out overlapping detections.
The final output includes bounding boxes, class labels, confidence scores, and segmentation masks (if enabled).

<br/>

### DATASET
Using the 'Pothole 2' [Dataset](https://universe.roboflow.com/project-saocp/pothole-2-mhkce) created by PROJECT.
Dataset Published by Roboflow (Universe)

<br/>

### HOW TO RUN
1. Download the file in **Releases** (left sidebar) or **Code** (green button).
2. Extract files (ZIP) locally and open `main.py` with your python IDE.
```
pip install torch torchvision
pip install numpy==1.26.4
pip install ultralytics
```
Download `yolov10` from the [YOLOv10 GitHub](https://github.com/THU-MIG/yolov10). Extract it and put it in the home directory.

3. Change the `ACTION` constant to specify what you want to do. Action descriptions is in `main.py`.
4. Run `main.py` with your IDE.
5. Profit

<br/>

### Manual Installation
Here is a list of dependencies to install and their instructions if you were to install them manually.

1. **Ultralytics**: `pip install ultralytics`
2. **CV2**: `pip install cv2`
3. **YOLOv10**: Download YOLOv10's code from link **above**. Place it in the home directory.

Made with PyCharm Community 2024.1.4 IDE, please try reproducing with this IDE if something goes wrong.
