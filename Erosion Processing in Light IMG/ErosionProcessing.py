import cv2 
import numpy as np 

IMG = cv2.imread('Erosion Processing in Light IMG\OpenCV_Logo.png', 1)

mode = 1
kernel = ""

if mode == 1:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
else:
    kernel = np.ones((5, 5), np.uint8)

erosion =  cv2.erode(IMG, kernel, iterations=1)
res = np.concatenate((IMG, erosion), axis= 1)

cv2.imshow('Result', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Como pode ser visto no resultado, o processo de dilatação aumenta os pixes mais escuros e detrimento 