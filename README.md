# Color Finder and Clicker

This project captures a specific region of the screen, searches for predefined colors within that region, and performs mouse clicks when it finds those colors. If it doesn't find any target color within 5 seconds, it performs a default click at a specified location.

## Features

- Capture a specified region of the screen.
- Detect predefined colors within the captured region.
- Perform a mouse click on the detected colors.
- Perform a default click if no target color is found within 5 seconds.
- Stop the script using the 'k' key.

## Prerequisites

- Python 3.x
- The following Python libraries: `pyautogui`, `numpy`, `opencv-python`, `pynput`

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/color-finder-clicker.git
    cd color-finder-clicker
    ```

2. Install the required libraries:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Get Coordinates for Screen Region:**

    To get the coordinates of the region you want to capture, you can use a tool like `pyautogui`. Run the following Python snippet to display your mouse position:

    ```python
    import pyautogui
    print(pyautogui.position())
    ```

    Move your mouse to the top-left corner of the desired region and note the coordinates, then move it to the bottom-right corner and note those coordinates. Use these values to define your region `(left, top, width, height)` in the script.

2. **Run the Script:**

    Execute the script with Python:

    ```sh
    python color_finder_clicker.py
    ```

3. **Stop the Script:**

    Press the 'k' key to stop the script.

## Code Explanation

The script consists of several key components:

- **Color Definition:**
  
  The `colors_to_find` list contains the colors (in BGR format) that the script will search for within the defined region of the screen.

- **Screen Capture Region:**
  
  The `region` variable defines the area of the screen to capture. Adjust the coordinates to match the region you want to monitor.

- **Color Detection and Clicking:**
  
  The `find_and_click_color` function captures the screen, converts the image to BGR format, and checks for the specified colors. If a color is found, it performs a single click at the color's location. If no color is found within 5 seconds, it performs a default click at the specified coordinates `(1748, 969)`.

- **Keyboard Listener:**
  
  The `on_press` function listens for the 'k' key to stop the script.

- **Multiprocessing:**
  
  The `run_color_finder` function runs the color detection in parallel for each color defined in `colors_to_find`.



## Contributing

Feel free to submit issues or pull requests if you have any improvements or bug fixes.

Disclaimer: This project is intended for educational purposes only. The author
is not liable for any misuse or misconduct related to the use of this software.
