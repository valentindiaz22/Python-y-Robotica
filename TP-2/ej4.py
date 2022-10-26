import cv2

imagen_org = cv2.imread("imagenes/ruta.jpg")
imagen = cv2.imread("imagenes/ruta.jpg")

imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

bordes = cv2.Canny(imagen_gris, 480, 680)
bordes = cv2.dilate(bordes, None, iterations=1)
bordes = cv2.erode(bordes, None, iterations=1)

contornos, jerarquia = cv2.findContours(bordes, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagen, contornos, -1, (0, 255, 0), 2)

texto = "Alerta al conductor"
cv2.putText(imagen, texto, (70, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 4)
cv2.putText(imagen, texto, (70, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

cv2.imshow("Imagen Modificada", imagen)
cv2.imshow("Imagen Original", imagen_org)
cv2.waitKey(0)
cv2.destroyAllWindows()