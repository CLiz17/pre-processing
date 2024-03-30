import cv2
import os

def extract_frames_from_folder(video_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(video_folder):
        video_path = os.path.join(video_folder, filename)
        if os.path.isfile(video_path):
            extract_frames(video_path, output_folder, filename)

def extract_frames(video_path, output_folder, filename):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Unable to open video file {video_path}")
        return

    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % 4 == 0:
            frame_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_file, frame)

        frame_count += 1

    cap.release()

    print(f"Frames extracted from {video_path}: {frame_count}")
    
# real
video_folder = "real_input_videos"
output_folder = "real_output_frames"

extract_frames_from_folder(video_folder, output_folder)

# fake
# video_folder = "deepfake_videos"
# output_folder = "dfake_output_frames"
# extract_frames_from_folder(video_folder, output_folder)