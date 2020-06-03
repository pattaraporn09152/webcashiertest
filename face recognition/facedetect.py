import numpy as np
import cv2
import time
import pickle
import dlib
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
model = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
FACE_DESC, FACE_NAME = pickle.load(open('trainset.pk', 'rb'))
cap = cv2.VideoCapture(0)


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_detector.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)

    for(x,y,w,h)in face:
        img = frame[y-10:y+h+10, x-10:x+w+10] [:,:,::-1]
        dets = detector(img,1)
        for k ,d in enumerate (dets) :
            shape = sp(img,d)
            face_desc0 = model.compute_face_descriptor(img, shape, 2)
            d = []
            for face_desc in FACE_DESC:
                d.append(np.linalg.norm(np.array(face_desc) - np.array(face_desc0)))
            d = np.array(d)
            idx = np.argmin(d)
            if d[idx] < 0.5 :
                name = FACE_NAME[idx]
                print(name)
                cv2.putText(frame, name, (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,255,255), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) 

    

    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.waitKey(1) 
     