import pyautogui
import numpy as np
import cv2
from pynput import keyboard
from multiprocessing import Manager, Process
from time import time, sleep

# Define the region of the screen to capture (left, top, width, height)
region = (1528, 419, 379, 527)

# Define the colors to look for (in BGR format for OpenCV)
colors_to_find = [
    (31, 255, 124),
    (30, 255, 125),
    (28, 255, 125),
    (30, 255, 122),
    (30, 255, 121),
    (32, 255, 124),
    (27, 251, 139),
    (27, 252, 137),
    (29, 252, 135),
    (31, 255, 125),
    (0, 216, 201),
    (0, 217, 196),
    (33, 255, 124),
    (26, 255, 125),
    (29, 255, 124)
]

# Define the color accuracy threshold (Euclidean distance threshold)
color_threshold = 80

def on_press(key, running):
    try:
        if key.char == 'k':
            running.value = False
            return False
    except AttributeError:
        pass

def find_and_click_color(color, running):
    lower_bound = np.array(color) - 10
    upper_bound = np.array(color) + 10
    
    last_click_time = time()
    
    while running.value:
        current_time = time()
        if current_time - last_click_time >= 5:
            # Perform a default click action if no target is found within 5 seconds
            pyautogui.click(1748, 969)
            last_click_time = current_time
            print("Performed default click after timeout")

        # Capture the screen
        screenshot = pyautogui.screenshot(region=region)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Check for the specific color
        mask = cv2.inRange(frame, lower_bound, upper_bound)
        coords = cv2.findNonZero(mask)

        if coords is not None:
            x, y = coords[0][0]
            print(f"Found color at ({x}, {y})")
            pyautogui.click(region[0] + x, region[1] + y)
            last_click_time = current_time
        
        # Limit the rate of screen capture
        sleep(0.05)

def run_color_finder(colors_to_find, running):
    processes = []
    for color in colors_to_find:
        p = Process(target=find_and_click_color, args=(color, running))
        p.start()
        processes.append(p)
    
    try:
        for p in processes:
            p.join()
    except KeyboardInterrupt:
        running.value = False
        for p in processes:
            p.terminate()

if __name__ == '__main__':
    # Create a manager to handle the shared value
    with Manager() as manager:
        running = manager.Value('b', True)
        
        # Start the keyboard listener
        listener = keyboard.Listener(on_press=lambda key: on_press(key, running))
        listener.start()
        
        # Run the color finder function
        run_color_finder(colors_to_find, running)
        
        listener.join()
