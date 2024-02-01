import cv2

# Forneça o caminho completo da imagem
image_path = 'CannyFilter-OpenCV/pexels-andrea-piacquadio-3784391.jpg'

original_image = cv2.imread(image_path)

# Verifique se a leitura da imagem foi bem-sucedida
if original_image is not None:
    # Redimensione a imagem para uma largura desejada (por exemplo, 800 pixels)
    target_width = 800
    aspect_ratio = original_image.shape[1] / original_image.shape[0]
    target_height = int(target_width / aspect_ratio)
    resized_image = cv2.resize(original_image, (target_width, target_height))

    # Aplicar a filtragem gaussiana
    blurred_image = cv2.GaussianBlur(resized_image, (5, 5), 0)

    gray_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2GRAY)

    # Aplicar a detecção de bordas usando Canny
    edges_image = cv2.Canny(gray_image, 50, 150)

    cv2.imshow('Edges Image (Canny)', edges_image)
    cv2.imshow('Original Image', resized_image)
    cv2.imshow('Blurred Image', blurred_image)
    cv2.imshow('Gray Image', gray_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Erro ao ler a imagem. Verifique o caminho do arquivo.")
