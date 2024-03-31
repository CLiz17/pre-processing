import os
import cv2

def resize_images_and_label(input_folder, output_folder, label):
    count = 0
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)

            resized_image = cv2.resize(image, (150, 150))

            filename_parts = os.path.splitext(filename)
            labeled_filename = f"{filename_parts[0]}_{label}{filename_parts[1]}"
            output_path = os.path.join(output_folder, labeled_filename)
            cv2.imwrite(output_path, resized_image)

            count += 1
            print(f"Image resized and labeled: {output_path}")
    return count

# real
# input_folder = 'real_output_faces'
# output_folder = 'real_resized_images'

# fake
input_folder = 'dfake_output_faces'
output_folder = 'dfake_resized_images'

# real
# label = 0

# fake
label = 1

count = resize_images_and_label(input_folder, output_folder, label)


print(f"Real Images : {count}")
# print(f"Fake Images : {count}")