import cv2
import time
import threading
from flask import Flask, Response
from picamera2 import Picamera2
from flask_cors import CORS  # CORS import kiya gaya

app = Flask(__name__)

# Enable CORS for the Flask app
CORS(app)  # Flask app mein CORS enable kiya gaya

# Initialize the camera
picam2 = Picamera2()
video_config = picam2.create_video_configuration(main={"size": (640, 480)})
picam2.configure(video_config)
picam2.start()

def generate_frames():
    while True:
        try:
            frame = picam2.capture_array()  # Live frame capture
            _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 85])  # Optimize quality
            frame_bytes = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

            time.sleep(0.03)  # Small delay to reduce CPU load (30 FPS limit)
        
        except Exception as e:
            print(f"Error capturing frame: {e}")
            break

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Graceful shutdown
import atexit

def cleanup():
    print("Stopping camera...")
    picam2.stop()

atexit.register(cleanup)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)



