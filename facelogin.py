import face_recognition
import cv2
import numpy as np
from datetime import datetime
import time

def face_login():
    video_capture = cv2.VideoCapture(0)

    # Load face encodings and names
    fuzail_image = face_recognition.load_image_file(r"C:\Users\Administrator\OneDrive\Pictures\Camera Roll\WIN_20230814_23_05_52_Pro.jpg")
    fuzail_encoding = face_recognition.face_encodings(fuzail_image)[0]

    raza_image = face_recognition.load_image_file(r"C:\Users\Administrator\OneDrive\Pictures\Camera Roll\WIN_20230814_23_05_52_Pro.jpg")
    raza_encoding = face_recognition.face_encodings(raza_image)[0]

    known_face_encodings = [fuzail_encoding, raza_encoding]
    known_face_names = ["Fuzail", "Raza"]

    users = known_face_names.copy()

    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")

    user=input("Enter User name")
    while True:
        _, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

                if name == user:
                    time.sleep(3)
                    return True
        time.sleep(3)
        return False
        cv2.imshow("Face Login : ", frame)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    f.close()
    return False


print(face_login())