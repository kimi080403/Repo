import cv2
import matplotlib.pyplot as plt

def flip_left_right(img):
	flipped_img = cv2.flip(img,flipCode=1)
	return flipped_img