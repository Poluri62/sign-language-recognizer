import cv2
import numpy as np
import glob
import random
import time


# Load Yolo
weights_path = r'yolov3_training_last.weights'
cfg_path = r"yolov3_testing.cfg"
net = cv2.dnn.readNet(weights_path, cfg_path)

# Name custom object
with open('classes.txt') as cf:
    classes = cf.read().strip('\n').split('\n')

#Set up camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1456)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1456)

layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# loop through all the images
while True:
    ret,frame = cap.read()
    
    img = cv2.resize(frame, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.3:
                # Object detected
                print(class_id)
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    print(indexes)
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 1)
            cv2.putText(img, label, (x, y), font, 2, color, 2)

    big = cv2.resize(img, None, fx=2.5, fy=2.5)
    cv2.imshow("Image", big)
    if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
    else:
        time.sleep(2)

cv2.destroyAllWindows()