import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()
        print(f"Cursor Position: x={x}, y={y}", end="\r") 
        time.sleep(0.1)  # update every 0.1 seconds
except KeyboardInterrupt:
    print("\nTracking stopped.")
