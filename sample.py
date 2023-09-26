import cv2
import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt

change_background_mp = mp.solutions.selfie_segmentation

change_bg_segment = change_background_mp.SelfieSegmentation()
sample_img = cv2.imread('me.jpg')

plt.figure(figsize = [10, 10])

plt.title("Sample Image");plt.axis('off');plt.imshow(sample_img[:,:,::-1]);plt.show()
