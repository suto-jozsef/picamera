import time
import cv2
from videostream import VideoStream

time.sleep(2)
cam = VideoStream(usePiCamera=True)
cam.start()

while True:
    frame = cam.read() #camera.capture_array()
    cv2.imshow("Image", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()