import cv2 
import numpy as np 

IMG = cv2.imread('Erosion Processing in Dark IMG/95103cv.png', 2)

mode = 2
kernel = ""

if mode == 1:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
else:
    kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(IMG, kernel, iterations=1)
res = np.concatenate((IMG, erosion), axis=1)

cv2.imshow('Result', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Como ficou visível no resultado, podemos constatar que o processo de erosão, decompõem alguns pixels mais claros, escurecendo a imagem.
