import cv2
import time
import threading
import numpy as np
from flask import Flask, Response
from picamera2 import Picamera2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initialize the camera
picam2 = Picamera2()
video_config = picam2.create_video_configuration(main={"size": (1280, 720), "format": "RGB888"})  # RGB Format
picam2.configure(video_config)
picam2.set_controls({"Brightness": 0.5, "Contrast": 1.5, "Sharpness": 1.0})  # Adjusted quality
picam2.start()

def generate_frames():
    while True:
        try:
            frame = picam2.capture_array()  # Capture frame in RGB format
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert RGB to BGR for OpenCV
            
            _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 95])  # Better quality
            frame_bytes = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

            time.sleep(0.02)  # Reduced delay for smoother stream

        except Exception as e:
            print(f"Error capturing frame: {e}")
            break

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

import atexit

def cleanup():
    print("Stopping camera...")
    picam2.stop()

atexit.register(cleanup)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
