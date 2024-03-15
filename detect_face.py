import os
import cv2
from mtcnn import MTCNN

def detect_faces(input_folder, output_folder):
    detector = MTCNN()

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)

            faces = detector.detect_faces(image)

            for i,face in enumerate(faces):
                x, y, w, h = face['box']
                face_image = image[y:y+h, x:x+w]
                output_path = os.path.join(output_folder, f"{filename.split('.')[0]}_face.jpg")
                cv2.imwrite(output_path, face_image)

            print(f"Faces detected in {filename}.")

# real
# input_folder = 'real_output_frames'
# output_folder = 'real_output_faces'

# fake
input_folder = 'dfake_output_frames'
output_folder = 'dfake_output_faces'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

detect_faces(input_folder, output_folder)