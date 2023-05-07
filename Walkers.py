import cv2

body_classifier = cv2.CascadeClassifier("haarcascade_fullbody.xml")

cap = cv2.VideoCapture('walking.avi')

while True:
    
    ret, frame = cap.read()

    cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    bodies = body_cassifier.detectMultiScale(gray, 1.2,3)
    
    for (x,y,w,h) in bodies:
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    if cv2.waitKey(1) == 32:
        break

cap.release()
cv2.destroyAllWindows()
