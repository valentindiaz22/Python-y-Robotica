import cv2

imagen = cv2.imread("imagenes/vehiculo.jpg")
imagen_recorte = imagen[137:160, 107:177]

cv2.imwrite("patente.png", imagen_recorte)

cv2.imshow("Imagen Original", imagen)
cv2.imshow("Imagen Recortada", imagen_recorte)
cv2.waitKey(0)
cv2.destroyAllWindows()

