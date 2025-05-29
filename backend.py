from flask import Flask
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

# GPIO Configuration
RED_PIN = 17  # GPIO17 (Pin 11)


def ensure_gpio():
    if not hasattr(ensure_gpio, "inited"):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(RED_PIN, GPIO.OUT)
        GPIO.output(RED_PIN, GPIO.LOW)
        ensure_gpio.inited = True


@app.route("/release", methods=["GET"])
def release_button():
    """Trigger the button release by shorting green & red."""
    ensure_gpio()
    try:
        # GPIO.output(RED_PIN, GPIO.HIGH)  # Connect green & red
        # time.sleep(0.5)  # Simulate button press duration
        # GPIO.output(RED_PIN, GPIO.LOW)  # Disconnect
        return "Button Released!", 200
    except Exception as e:
        return str(e), 500


@app.route("/")
def home():
    return "Flask GPIO API Running! Use /release to trigger.", 200


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
    except KeyboardInterrupt:
        GPIO.cleanup()
