
# from keras.models import load_model
# from time import sleep
# from keras.preprocessing.image import img_to_array
# from keras.preprocessing import image
# import cv2
# import numpy as np

# face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# #face_classifier = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
# classifier =load_model('C:/Users/HP/Desktop/Emotion-Detection-master/Emotion-Detection-master/Emotion_Detection.h5')

# class_labels = ['Angry','Happy','Neutral','Sad','Surprise']

# cap = cv2.VideoCapture(0)

# while True:
    
#     ret, frame = cap.read()
#     labels = []
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     faces = face_classifier.detectMultiScale(gray,1.3,5)

#     for (x,y,w,h) in faces:
#         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
#         roi_gray = gray[y:y+h,x:x+w]
#         roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)


#         if np.sum([roi_gray])!=0:
#             roi = roi_gray.astype('float')/255.0
#             roi = img_to_array(roi)
#             roi = np.expand_dims(roi,axis=0)

        

#             preds = classifier.predict(roi)[0]
#             print("\nprediction = ",preds)
#             label=class_labels[preds.argmax()]
#             print("\nprediction max = ",preds.argmax())
#             print("\nlabel = ",label)
#             label_position = (x,y)
#             cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
#         else:
#             cv2.putText(frame,'No Face Found',(20,60),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
#         print("\n\n")
#     cv2.imshow('Emotion Detector',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# # press q key to exit the code

# cap.release()
# cv2.destroyAllWindows()

from flask import Flask, render_template, Response
import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array

app = Flask(__name__, template_folder='C:/Users/HP/Desktop/Emotion-Detection-master/Emotion-Detection-master/indexWeb.html')


face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
classifier = load_model('C:/Users/HP/Desktop/Emotion-Detection-master/Emotion-Detection-master/Emotion_Detection.h5')
class_labels = ['Angry','Happy','Neutral','Sad','Surprise']

def detect_emotion(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
        if np.sum([roi_gray]) != 0:
            roi = roi_gray.astype('float')/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)
            preds = classifier.predict(roi)[0]
            label = class_labels[preds.argmax()]
            cv2.putText(frame, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    return frame

def generate_frames():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        else:
            frame = detect_emotion(frame)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('indexWeb.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)

























