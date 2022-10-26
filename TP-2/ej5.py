import cv2

cap = cv2.VideoCapture(1)
#si no funciona, cambiar el 1 de arriba por 0 u otro número.

while True:
    ret, frame = cap.read()
    cv2.imshow("En vivo, (para salir presionar q)", frame)

    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()