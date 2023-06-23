import cv2

face_cascade = cv2.CascadeClassifier('D:\Python\Image and Video Processing\haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.2, minNeighbors = 5)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("Recog",frame)
    key = cv2.waitKey(1)
    if (key == ord('w')):
        break

video.release()
cv2.destroyAllWindows