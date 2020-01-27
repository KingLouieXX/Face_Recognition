# Luis Zepeda
# AutoDrone: Face Recognition
# 01/21/20

#Base Code from Muhammad Rizwan
import cv2
import face_recognition

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    frame = cv2.resize(frame, (0,0), fx=1, fy=1)

    # Find all the faces in the video
    face_locations = face_recognition.face_locations(frame)

    number_of_faces = len(face_locations)
    print("I found {} face(s) in this video.".format(number_of_faces))

    for face_location in face_locations:
        # Print the location of each face in this image. Each face is a list of co-ordinates in (top, right, bottom, left) order.
        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom,
                                                                                                    right))
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 3)

    cv2.imshow("Frame", frame)

    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

