import numpy as np
import cv2
from tensorflow.keras.models import load_model

MODEL_PATH = "model/model.keras"

def model_predict(image):
    try:
        model = load_model(MODEL_PATH)
        try:
            pred = int(model.predict(image))
            return pred
        except:
            print("Error: Prediction unsuccess")
            return None
    except:
        print("Error: Incorrect model path")
        return None


def process_image(path):
    try:
        image = cv2.imread(path)
        
        if image.shape[2] == 4:
            image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        try:
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(48, 48))
            valid_faces = []

            for i, (x, y, w, h) in enumerate(faces):
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                face_image = image[y:y+h, x:x+w]
                valid_faces.append(face_image)
                cv2.putText(image, f'Person {i+1}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            img = valid_faces[0]
        except:
            print("No face detected")
            return None
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        normalized_image = gray_image / 255.0
        resized_image = cv2.resize(normalized_image, (48, 48))
        batched_image = np.expand_dims(resized_image, axis=0)
        return batched_image
    except:
        print("Incorrect image path")
        return None