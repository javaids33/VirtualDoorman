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
        # Force LOW state first to ensure clean start
        GPIO.output(RED_PIN, GPIO.LOW)
        time.sleep(0.1)

        # Trigger the pin
        GPIO.output(RED_PIN, GPIO.HIGH)
        time.sleep(0.5)  # Simulate button press duration

        # Explicitly set back to LOW
        GPIO.output(RED_PIN, GPIO.LOW)

        # Verify pin state
        current_state = GPIO.input(RED_PIN)
        return f"Button Released! Pin state: {current_state}", 200
    except Exception as e:
        return str(e), 500


@app.route("/status", methods=["GET"])
def check_status():
    """Check the current state of the GPIO pin."""
    ensure_gpio()
    try:
        state = GPIO.input(RED_PIN)
        return f"Current GPIO state: {'HIGH' if state else 'LOW'}", 200
    except Exception as e:
        return str(e), 500


@app.route("/reset", methods=["GET"])
def reset_pin():
    """Force the GPIO pin to LOW state."""
    ensure_gpio()
    try:
        GPIO.output(RED_PIN, GPIO.LOW)
        return "Pin reset to LOW", 200
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
