import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("cat.jpg")
blur=cv2.blur(img,(8,8))

plt.subplot(211),plt.imshow(img),plt.title('original')
plt.subplot(212),plt.imshow(blur),plt.title('blured')
plt.show()