import cv2
import numpy as np

IMG =  cv2.imread('Dilation Processing in Dark IMG/apple.png', 0)

kernel =  cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

dilation = cv2.dilate(IMG, kernel, iterations=1)
res = np.concatenate((IMG, dilation), axis=1)

cv2.imshow('Result', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

# como podemos ver no resultado, o processo de ditação deixa a imagem mais clara, decompondo alguns pixels escuros ao redor dos pixels claros.