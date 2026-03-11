"""
Smart Industrial Maintenance System

This script simulates a basic Smart Industrial Maintenance System.
It includes functionalities for:
- Simulating sensor data from industrial machinery.
- Storing sensor data.
- Implementing a simple predictive maintenance model based on vibration data.
- Generating alerts for potential failures.
- Displaying basic maintenance logs.

Note: This is a simplified simulation and does not represent a production-ready system.
It lacks features like real-time data ingestion, complex AI models, robust error handling,
database integration, and a user interface.

Libraries Used:
- random: For simulating sensor data.
- time: For simulating timestamps and delays.
- datetime: For handling date and time objects.
"""

import random
import time
from datetime import datetime
MACHINERY_ID = "Machine-001"
SENSOR_READING_FREQUENCY_SEC = 5
VIBRATION_THRESHOLD = 8.0  
ALERT_COOLDOWN_SEC = 60 * 5  

sensor_data = []
maintenance_logs = []
last_alert_time = None

def simulate_sensor_data(machine_id):
    """Simulates sensor readings for a given machine."""
    timestamp = datetime.now()
    temperature = random.uniform(30, 70)  # Celsius
    vibration = random.uniform(1, 10)      # Arbitrary unit
    pressure = random.uniform(100, 150)    # PSI
    return {"machine_id": machine_id, "timestamp": timestamp,
            "temperature": temperature, "vibration": vibration, "pressure": pressure}

def store_sensor_data(data):
    """Stores the simulated sensor data."""
    sensor_data.append(data)
    print(f"[{data['timestamp']}] - Data logged: Temperature={data['temperature']:.2f}°C, Vibration={data['vibration']:.2f}, Pressure={data['pressure']:.2f} PSI")

# --- Predictive Maintenance Model (Simple Vibration Analysis) ---
def analyze_vibration(data):
    """Analyzes vibration data to predict potential issues."""
    if data["vibration"] > VIBRATION_THRESHOLD:
        return True
    return False

# --- Alerting System ---
def generate_alert(data):
    """Generates an alert if a potential issue is detected."""
    global last_alert_time
    current_time = datetime.now()
    if last_alert_time is None or (current_time - last_alert_time).total_seconds() > ALERT_COOLDOWN_SEC:
        alert_message = f"[{data['timestamp']}] - POTENTIAL ISSUE: High vibration detected on {data['machine_id']} (Vibration = {data['vibration']:.2f})"
        print(f"\n{'!'*30} ALERT! {'!'*30}\n{alert_message}\n{'!'*67}\n")
        maintenance_logs.append({"timestamp": data['timestamp'], "machine_id": data['machine_id'], "event": "High Vibration Alert"})
        last_alert_time = current_time

# --- Maintenance Logging ---
def display_maintenance_logs():
    """Displays the recorded maintenance logs."""
    if maintenance_logs:
        print("\n--- Maintenance Logs ---")
        for log in maintenance_logs:
            print(f"[{log['timestamp']}] - {log['machine_id']}: {log['event']}")
        print("------------------------\n")
    else:
        print("\n--- No Maintenance Logs Yet ---\n")

# --- Main Simulation Loop ---
if __name__ == "__main__":
    print("Starting Smart Industrial Maintenance System Simulation...")
    try:
        while True:
            sensor_reading = simulate_sensor_data(MACHINERY_ID)
            store_sensor_data(sensor_reading)

            if analyze_vibration(sensor_reading):
                generate_alert(sensor_reading)

            time.sleep(SENSOR_READING_FREQUENCY_SEC)

    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")
        display_maintenance_logs()
    except Exception as e:
        print(f"An error occurred: {e}")
        display_maintenance_logs()

