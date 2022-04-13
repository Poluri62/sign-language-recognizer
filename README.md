# sign-language-recognizer
A YOLOv3 object detection model custom trained to learn to recognize alphabets from the American Sign Language.
The model has achieved a mAP (mean average precision) of 60.6.

## Run the model
Pre-requisites:
1. Python version 3+
2. OpenCV
3. numpy
4. glob

Download the weights file "yolov3_training_last.weights" from https://drive.google.com/drive/folders/11f_uEHOzS-md4pEICAaOf1AuxVJ54Os2

After cloning the repo, run yolo_detection_from_camera.py to try out the detector in real time.
Run test_yolo_detector_on_images.py to try out the detector on images. You will need to set up a "test" folder with the images you want to test

## Training Yolo
The steps followed during training the model are in the notebook: Yolov3-training-notebook.ipynb