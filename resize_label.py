import os
import cv2

def resize_images_and_label(input_folder, output_folder, label):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)

            resized_image = cv2.resize(image, (150, 150))

            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, resized_image)

            print(f"Image resized and labeled: {output_path}")

input_folder = 'output_faces'
output_folder = 'resized_images'

label = 0

resize_images_and_label(input_folder, output_folder, label)