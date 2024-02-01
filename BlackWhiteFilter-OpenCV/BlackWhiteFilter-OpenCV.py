import cv2

# Forneça o caminho completo da imagem
image_path = 'BlackWhiteFilter-OpenCV/pexels-andrea-piacquadio-3784391.jpg'

original_image = cv2.imread(image_path)

# Verifique se a leitura da imagem foi bem-sucedida
if original_image is not None:
    # Redimensione a imagem para uma largura desejada (por exemplo, 800 pixels)
    target_width = 800
    aspect_ratio = original_image.shape[1] / original_image.shape[0]
    target_height = int(target_width / aspect_ratio)
    resized_image = cv2.resize(original_image, (target_width, target_height))

    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    (thresh, black_and_white_image) = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow('Black and White Image', black_and_white_image)
    cv2.imshow('Original Image', resized_image)
    cv2.imshow('Gray Image', gray_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Erro ao ler a imagem. Verifique o caminho do arquivo.")
