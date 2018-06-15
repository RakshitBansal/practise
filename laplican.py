import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("chess.jpg",0)
laplacian=cv2.Laplacian(img,cv2.CV_64F)
soblex=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobley=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
plt.subplot(2,2,1),plt.imshow(img,cmap='gray')
plt.title('original'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap='gray')
plt.title('laplacian'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3),plt.imshow(soblex,cmap='gray')
plt.title('soblex'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobley,cmap='gray')
plt.title('sobley'),plt.xticks([]),plt.yticks([])
plt.show()