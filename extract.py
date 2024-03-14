import cv2
import os

def extract_frames(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Unable to open video file")
        return

    os.makedirs(output_folder, exist_ok=True)

    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % 4 == 0:
            frame_file = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_file, frame)

        frame_count += 1

    cap.release()

    print(f"Frames extracted: {frame_count}")

video_path = "input_video.mp4"
output_folder = "output_frames"
extract_frames(video_path, output_folder)