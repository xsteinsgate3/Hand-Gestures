import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import imageio.v2 as imageio
import numpy as np

# Checking that packages were imported successfully.
if mp and python and vision:
    print("Packages Imported Successfully.")

# Load the input image from an image file.
mp_image = mp.Image.create_from_file('hand.jpg')

# Create a gesture recognizer instance with the image mode:
model_path = '/gesture_recognizer.task'
BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.IMAGE)

# Load the image
img = imageio.imread('hand.jpg')

# Convert the image to a numpy array
img_np = np.array(img)

# Load the input image from a numpy array.
mp_image = mp.Image(format=mp.ImageFormat.SRGB, data=img_np)

# Where output will be.


input("End of Program.")