# VirtualDoorman

# Flask GPIO Button Release API (Raspberry Pi)

This project provides a simple Flask-based web API that allows you to simulate a button release on your Raspberry Pi by shorting two GPIO-connected wires (e.g., green and red from an RJ9 cable).

## 🚀 Features
- Trigger a GPIO output to short two pins (simulate a button press/release).
- Lightweight Flask API with a `/release` endpoint.
- Easily accessible over your network.

---

## 🧰 Requirements

- Raspberry Pi (any model with GPIO)
- Python 3.x
- Wires connected:
  - **Green wire → GPIO17 (Pin 11)**
  - **Red wire → GND (Pin 6, 9, or any GND)**

---

## 📦 Installation

1. Clone or download this repo.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
