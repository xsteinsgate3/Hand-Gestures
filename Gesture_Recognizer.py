import mediapipe as mp
import cv2
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

model_path = '/gesture_recognizer.task'

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode

# Use OpenCV’s VideoCapture to start capturing from the webcam.
capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Cannot open camera")
    exit()

# Create a loop to read the latest frame from the camera using VideoCapture#read()
while True:
    ret, frame = capture.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Convert the frame received from OpenCV to a MediaPipe’s Image object.
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)

    # Create a gesture recognizer instance with the live stream mode:
    def print_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
        print('gesture recognition result: {}'.format(result))

    options = GestureRecognizerOptions(
        base_options=BaseOptions(model_asset_path=model_path),
        running_mode=VisionRunningMode.LIVE_STREAM,
        result_callback=print_result)
    with GestureRecognizer.create_from_options(options) as recognizer:
        # The detector is initialized. Use it here.
        recognizer.recognize_async(mp_image, frame_timestamp_ms)
