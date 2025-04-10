from flask import Flask
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

# GPIO Configuration
GREEN_PIN = 17  # GPIO17 (Pin 11)

GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.output(GREEN_PIN, GPIO.LOW)  # Ensure it's disconnected initially

@app.route('/release', methods=['GET'])
def release_button():
    """Trigger the button release by shorting green & red."""
    try:
        GPIO.output(GREEN_PIN, GPIO.HIGH)  # Connect green & red
        time.sleep(0.5)  # Simulate button press duration
        GPIO.output(GREEN_PIN, GPIO.LOW)  # Disconnect
        return "Button Released!", 200
    except Exception as e:
        return str(e), 500

@app.route('/')
def home():
    return "Flask GPIO API Running! Use /release to trigger.", 200

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    except KeyboardInterrupt:
        GPIO.cleanup()
