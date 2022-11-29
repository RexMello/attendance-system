import os
import face_recognition as fr
import cv2


image = cv2.imread('new\90.PNG')

coords  = fr.face_locations(image)
print(coords)