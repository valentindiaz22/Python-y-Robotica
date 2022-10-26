import cv2

imagen = cv2.imread("imagenes/cara_dado.png")
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

bordes = cv2.Canny(imagen_gris, 100, 200)
bordes = cv2.dilate(bordes, None, iterations=1)
bordes = cv2.erode(bordes, None, iterations=1)

contornos, jerarquia = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagen, contornos, -1, (0, 0, 255), 2)

texto = "Contornos encontrados: "+ str(len(contornos))
cv2.putText(imagen, texto, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)
#Modificación realizada en el tamaño del texto agregado, el texto en 0.7 se sobresalía de la imagen.

cv2.imshow("Imagen", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()


