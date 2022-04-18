import cv2
import os
import numpy as np

def process_image(file_name, face_cascade):
    img = cv2.imread("input-images/" + file_name)

    faces_detected = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)
    if len(faces_detected) > 0:
        (x, y, w, h) = faces_detected[0]

        p = 10 #padding
        img_cropped = img[y-p+1:y+h+p, x-p+1:x+w+p]

        im_reshape = cv2.resize(img_cropped , (img.shape[0], img.shape[1]), interpolation=cv2.INTER_CUBIC)

        norm_img = np.zeros((im_reshape.shape[0], im_reshape.shape[1]))
        norm_img = cv2.normalize(im_reshape, norm_img, 0, 255, cv2.NORM_MINMAX)

        cv2.imwrite("output-images/" + file_name, norm_img)

face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
for filename in os.listdir("input-images"):
    process_image(filename, face_cascade)