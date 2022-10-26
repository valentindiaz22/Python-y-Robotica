import cv2
import numpy

imagen = cv2.imread("imagenes/semaforo2.jpg")
imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

redBajo1 = numpy.array([0, 100, 20], numpy.uint8)
redAlto1 = numpy.array([8, 255, 255], numpy.uint8)
redBajo2 = numpy.array([175, 100, 20], numpy.uint8)
redAlto2 = numpy.array([179, 255, 255], numpy.uint8)

maskRed1 = cv2.inRange(imagenHSV, redBajo1, redAlto1)
maskRed2 = cv2.inRange(imagenHSV, redBajo2, redAlto2)
maskRed = cv2.add(maskRed1, maskRed2)

maskRedvis = cv2.bitwise_and(imagen, imagen, mask=maskRed)

cv2.imshow("Original", imagen)
cv2.imshow("maskRed", maskRed)
cv2.imshow("maskRedvis", maskRedvis)
cv2.waitKey(0)
cv2.destroyAllWindows()
