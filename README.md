# Video to Frames Converter

This repository contains a script to convert a video into individual frames and save them as images using OpenCV. The frames are saved in a specified output folder.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Function Description](#function-description)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Installation


1. Install the required dependencies:
    ```sh
    pip install opencv-python
    ```

2. Ensure you have OpenCV and OS library installed:
    ```sh
    pip install opencv-python-headless
    ```
# Function Description

convert_video_to_frames(video_path, output_folder): This function converts the given video into frames and saves them in the specified output folder.
video_path: Path to the input video file.
output_folder: Path to the folder where frames will be saved.
Returns the total number of frames extracted from the video.

# Example
To use the function, simply specify the path to your video file and the output folder where you want to save the frames. The script will read the video, convert it into frames, and save each frame as an image in the specified folder.

