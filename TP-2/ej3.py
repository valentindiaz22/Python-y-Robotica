import cv2
import numpy

imagen = cv2.imread("imagenes/cubo.jpg")

imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

blueBajo = numpy.array([90, 50, 70], numpy.uint8)
blueAlto = numpy.array([128, 255, 255], numpy.uint8)
# usé otros valores para detectar el azul ya que el dado por el ejercicio apenas marcaba los contornos, éste funciona
# correctamente

maskBlue = cv2.inRange(imagenHSV, blueBajo, blueAlto)

maskBluevis = cv2.bitwise_and(imagen, imagen, mask=maskBlue)

cv2.imshow("Original", imagen)
cv2.imshow("maskBlue", maskBlue)
cv2.imshow("maskBluevis", maskBluevis)
cv2.waitKey(0)
cv2.destroyAllWindows()