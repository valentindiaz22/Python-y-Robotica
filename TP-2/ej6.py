import cv2

video = cv2.VideoCapture("imagenes/video.mp4")

while True:

    ret, frame = video.read()

    fps = "Fps: ", int(video.get(cv2.CAP_PROP_FPS))
    ancho = "Ancho: ", int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    largo = "Largo: ", int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    tiempo = "Tiempo en milisegundos: ", int(video.get(cv2.CAP_PROP_POS_MSEC ))

    cv2.putText(frame, str(fps), (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 6)
    cv2.putText(frame, str(fps), (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 4)

    cv2.putText(frame, str(ancho), (0, 65), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 6)
    cv2.putText(frame, str(ancho), (0, 65), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 4)

    cv2.putText(frame, str(largo), (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 6)
    cv2.putText(frame, str(largo), (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 4)

    cv2.putText(frame, str(tiempo), (0, 135), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 6)
    cv2.putText(frame, str(tiempo), (0, 135), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 4)

    cv2.imshow("Video propiedades basicas, (para salir presionar q)", frame)

    if cv2.waitKey(1) == ord("q"):
        break

video.release()
cv2.destroyAllWindows()