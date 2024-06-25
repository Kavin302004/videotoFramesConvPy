#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import os

# Function to convert a video to frames and store them
def convert_video_to_frames(video_path, output_folder):
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Initialize frame count
    frame_count = 0

    while True:
        # Read a frame from the video
        success, frame = video_capture.read()

        if not success:
            break

        # Save the frame as an image in the output folder
        frame_filename = os.path.join(output_folder, f"fram_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)

        frame_count += 1

    # Release the video capture object
    video_capture.release()

    return frame_count

# Specify the path to the video file
video_path = r"\filename.mp4" # Replace with the path to your video file

# Specify the folder where frames will be saved
output_folder = r"\FolderName"

# Convert the video to frames and get the frame count
frame_count = convert_video_to_frames(video_path, output_folder)

print(f"Video frames saved to {output_folder}. Total frames: {frame_count}")


# In[ ]:




