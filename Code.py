import serial
import time

# ---------------------------
# CONFIGURATION
# ---------------------------

USE_ARDUINO = False   # ✅ Set True if Arduino is connected
ARDUINO_PORT = "COM3"
BAUD_RATE = 9600

# Connect to Arduino if enabled
if USE_ARDUINO:
    arduino = serial.Serial(port=ARDUINO_PORT, baudrate=BAUD_RATE, timeout=1)
    time.sleep(2)  # wait for Arduino reset


# ---------------------------
# ML PLACEHOLDERS (replace with real models later)
# ---------------------------

def get_car_density(frame):
    """
    Placeholder ML model.
    Input: webcam frame
    Output: "low" or "high"
    """
    return "low"   # default dummy


def detect_ambulance(audio, road_id):
    """
    Placeholder ML model.
    Input: audio recording
    Output: True (ambulance detected) / False
    """
    return False   # default dummy


def get_webcam_frame(road_id):
    """Simulated webcam frame for each road."""
    return None


def get_microphone_audio(road_id):
    """Simulated mic audio for each road."""
    return None


# ---------------------------
# Arduino communication
# ---------------------------

def send_command(road, color):
    """Send command to Arduino or just print if simulating."""
    cmd = f"{road} {color}\n"
    if USE_ARDUINO:
        arduino.write(cmd.encode())
    print(f"Sent: Road {road+1} -> {color}")


def traffic_cycle(road, car_density="low", ambulance=False):
    """Run one traffic cycle for a given road."""

    # Ambulance priority: immediate 30s green
    if ambulance:
        send_command(road, "GREEN")
        time.sleep(30)

        send_command(road, "YELLOW")
        time.sleep(10)

        send_command(road, "RED")
        time.sleep(1)
        return

    # Normal cycle
    green_time = 60 if car_density == "high" else 30

    send_command(road, "GREEN")
    time.sleep(green_time)

    send_command(road, "YELLOW")
    time.sleep(10)

    send_command(road, "RED")
    time.sleep(1)


# ---------------------------
# Main loop
# ---------------------------

if __name__ == "__main__":
    while True:
        # Step 1: check ambulance
        ambulance_roads = []
        for road in range(3):
            audio = get_microphone_audio(road)
            if detect_ambulance(audio, road):
                ambulance_roads.append(road)

        if ambulance_roads:
            # 🚑 Give priority to first detected ambulance road
            priority_road = ambulance_roads[0]
            print(f"🚨 Ambulance detected on Road {priority_road+1}!")
            traffic_cycle(priority_road, car_density="low", ambulance=True)
            continue  # Restart loop after ambulance handling

        # Step 2: normal traffic cycle
        for road in range(3):
            frame = get_webcam_frame(road)
            car_density = get_car_density(frame)
            traffic_cycle(road, car_density)
