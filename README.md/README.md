Color Detection using OpenCV
Description
This project demonstrates real-time color detection using a webcam with OpenCV. It detects a specific color (yellow by default), creates a mask in the HSV color space, and draws a bounding box around the detected object.
The project uses a helper function (get_limits) to automatically calculate HSV color limits from a given BGR color value.

Requirements
Install the required Python packages using the versions below:
pip install opencv-python==4.6.0.66 numpy==1.23.4 Pillow==9.2.0


Project Structure
project/
│── main.py        # Main color detection program
│── util.py        # Utility functions for HSV limits
│── README.md      # Project documentation


Main Program (main.py)
The main program:

Opens the webcam
Converts frames from BGR to HSV
Applies a color mask
Cleans the mask using median blur
Detects the bounding box of the color region
Draws a rectangle around the detected object

Key Features

Real-time webcam processing
HSV-based color detection
Automatic color range calculation
Bounding box visualization


Utility Program (util.py)
The get_limits function:

Converts a given BGR color to HSV
Extracts the hue value
Handles hue wrap-around cases (especially for red)
Returns lower and upper HSV limits for masking

This makes the color detection more flexible and accurate.

How to Run

Connect a webcam to your system
Make sure all required packages are installed
Run the main program:

python main.py


Controls

Press q to quit the application


Output

Displays a live webcam feed
Draws a green bounding box around the detected yellow object


Customization

Change the target color by modifying the yellow BGR value in main.py
Adjust mask cleaning by changing the medianBlur kernel size


Author
Yuvaraj D

License
This project is open-source and free to use for learning and educational purposes.
