import cv2
import PIL.Image
import os
from playsound import playsound
cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
# img_counter = 0
# https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv
while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        # SPACE pressed
        img_name = f"person.png"
        cv2.imwrite(img_name, frame)
        print(f"{img_name} written!")
        # img_counter += 1    
        # break
        playsound('imagesaved.wav')
        os.system('python3 n.py')

cam.release()
cv2.destroyAllWindows()
