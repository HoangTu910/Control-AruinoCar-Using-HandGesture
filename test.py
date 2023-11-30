import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import arduino as arduino
import time
import serial
# ser = serial.Serial("COM10", 9600, timeout = 1)
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")
offset = 20
imgSize = 300
counter = 0
folder = "images/Turn Left"
labels = ["Forward", "Stop","TRight", "TLeft", "Backward"]
while True:
    success, img = cap.read()
    hands = detector.findHands(img, draw=False)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8)*255

        try:
            imgCrop = img[y-offset:y+h+offset, x-offset:x+w+offset]
            try:
                aspect_ratio = h/w
                if aspect_ratio > 1:
                    prev_aspect = h/w
                    new_witdh = math.ceil(imgSize / prev_aspect)
                    imgResize = cv2.resize(imgCrop, (new_witdh, imgSize))
                    y_remain = math.ceil((imgWhite.shape[1] - imgResize.shape[1])/2)
                    imgWhite[0:imgResize.shape[0], y_remain:imgResize.shape[1]+y_remain] = imgResize
                    prediction, index = classifier.getPrediction(imgWhite, draw=False)
                else:
                    prev_aspect = h / w
                    new_height = math.ceil(imgSize * prev_aspect)
                    imgResize = cv2.resize(imgCrop, (imgSize, new_height))
                    x_remain = math.ceil((imgWhite.shape[0] - imgResize.shape[0]) / 2)
                    imgWhite[x_remain:imgResize.shape[0]+x_remain, 0:imgResize.shape[1]] = imgResize
                    prediction, index = classifier.getPrediction(imgWhite, draw=False)
                cv2.imshow("imgWhite", imgWhite)
                cv2.putText(img, labels[index], (x, y-20), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,255), 2)
                if index == 0:
                    arduino.forward()
                elif index == 1:
                    arduino.stop()
                elif index == 2:
                    arduino.right()
                elif index == 3:
                    arduino.left()
                elif index == 4:
                    arduino.backward()
                # if index == 0:
                #     ser.write(b'1')
                # else:
                #     ser.write(b'0')
            except:
                print("Out of imgWhite")
                arduino.stop()
        except:
            print("Out of imgCrop")
            arduino.stop()
    else:
        arduino.stop()
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)


