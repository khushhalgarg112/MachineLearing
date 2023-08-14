import cv2

cap = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml")

while True:

    ret,frame = cap.read()

    if ret:
        faces = classifier.detectMultiScale(frame)

        for face in faces:
            x,y,w,h = face
            frame = cv2.rectangle(frame,(x,y), (x+w,y+h), (0,255,0),8)
        cv2.imshow("MY Windows",frame )

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()



#  Adding image 

# import cv2
# import numpy as np

# cap = cv2.VideoCapture(0)
# classifier = cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml")
# overlay = cv2.imread("thug.png")

# while True:
#     ret, frame = cap.read()

#     if ret:
#         faces = classifier.detectMultiScale(frame)

#         for face in faces:
#             x, y, w, h = face
#             overlay_resized = cv2.resize(overlay, (w, h))
#             frame[y:y+h, x:x+w] = cv2.addWeighted(frame[y:y+h, x:x+w], 1, overlay_resized, 0.5, 0)

#         cv2.imshow("MY Windows", frame)

#     key = cv2.waitKey(1)

#     if key == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()