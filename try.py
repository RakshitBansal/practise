import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("cat.jpg")
img2=cv2.imread("dog.jpg")
blur=cv2.blur(img,(8,8))
blur2=cv2.blur(img2,(20,5))

plt.subplot(221),plt.imshow(img),plt.title('original')
plt.subplot(222),plt.imshow(blur),plt.title('blured')
plt.subplot(223),plt.imshow(img2),plt.title('dog')
plt.subplot(224),plt.imshow(blur2),plt.title('blured')
plt.show()
