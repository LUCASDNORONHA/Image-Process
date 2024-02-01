import cv2

image = cv2.imread('GrayFilter-OpenCV/pexels-andrea-piacquadio-3784391.jpg')

# Verifique se a leitura da imagem foi bem-sucedida
if image is not None:
    # Redimensione a imagem para uma largura desejada (por exemplo, 800 pixels)
    target_width = 800
    aspect_ratio = image.shape[1] / image.shape[0]
    target_height = int(target_width / aspect_ratio)
    resized_image = cv2.resize(image, (target_width, target_height))

    gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Original Image', resized_image)
    cv2.imshow('Gray Image', gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Erro ao ler a imagem. Verifique o caminho do arquivo.")
