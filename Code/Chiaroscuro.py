import cv2
import numpy as np
import matplotlib.pyplot as plt


# ========================================================================
# Funcion claroscuro
# ========================================================================
def chiaroscuro(img):
    # Se obtiene el tamano del arreglo (imagen)
    rows = img.shape[0] - 1
    cols = img.shape[1] - 1

    # Se calcula el nuevo color de cada pixel
    for i in range(0, rows, 1):
        for j in range(0, cols, 1):

            #Se lee cada canal (RGB)
            b = img.item(i, j, 0)
            g = img.item(i, j, 1)
            r = img.item(i, j, 2)

            # Calculo de intensidad para cada pixel,
            # dividimos entre 4 en vez de 3 para mejor contaste con las sombras.
            n = (r + g + b) / 4

            # Definimos zonas obscuras; las que esten en cierto rango (entre 0 y 100)
            if (n <= 100):

                # Creo una constante normalizada entre 0 y 1 para los pixeles mas oscuros
                alpha = n / 100

                # Multiplico el valor original del pixel (cada canal) por la constante al
                # cuadrado para que el aumento sea gradual y se vea natural

                img.itemset((i, j, 0), b * alpha * alpha)
                img.itemset((i, j, 1), g * alpha * alpha)
                img.itemset((i, j, 2), r * alpha * alpha * 1.1)

            # Similar que antes pero para los pixels claros
            elif (n > 160):

                # Similar a la constante alpha,pero esta aumentara la intensidad
                # asi que le sumo 1
                beta = (((n - 126) / 127) * ((n - 126) / 127) * 0.01) + 1

                # Multiplicamos cada canal pero los limitamos a 255
                if (b * beta <= 255):
                    img.itemset((i, j, 0), b * beta)
                else:
                    img.itemset((i, j, 0), 255)

                if (g * beta <= 255):
                    img.itemset((i, j, 1), g * beta)
                else:
                    img.itemset((i, j, 1), 255)

                if (r * beta *1.1 <= 255):
                    img.itemset((i, j, 2), (r * beta * 1.1))
                else:
                    img.itemset((i, j, 2), 255)


# ========================================================================
# Ejecucion
# ========================================================================

# Lectura y muestra la imagen original
path = "1.jpg"
imag = cv2.imread(path, cv2.IMREAD_UNCHANGED)
cv2.imshow('original', imag)
cv2.namedWindow('original')

# Se ejecuta la funcion claroscuro y se muestra el resultado
chiaroscuro(imag)
cv2.namedWindow('Claroscuro')
cv2.imshow('Claroscuro', imag)

cv2.waitKey(0)


