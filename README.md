# Virtual Mouse Control .

## Description
This project implements a virtual mouse control system using hand gestures detected via webcam. It utilizes computer vision techniques with MediaPipe for hand tracking and PyAutoGUI for mouse control. The system allows you to move the cursor and perform clicks by simply moving your index finger and thumb.




##DEMO VID:



https://github.com/user-attachments/assets/690cb216-811c-4fdd-811c-4d23805326f7


## Features
- Real-time hand tracking using MediaPipe
- Cursor movement controlled by index finger position
- Click action triggered by bringing thumb and index finger close together
- Smooth cursor movement across the screen
- Visual feedback of finger positions on the camera feed

  
 
## Requirements
- Python 3.x
- OpenCV (`cv2`)
- MediaPipe (`mediapipe`)
- PyAutoGUI (`pyautogui`)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/virtual-mouse.git
   cd virtual-mouse
   ```

2. Install the required packages:
   ```bash
   pip install opencv-python mediapipe pyautogui
   ```

## Usage
1. Run the application:
   ```bash
   python virtual_mouse.py
   ```

2. Position your hand in front of the webcam:
   - Move your index finger to control cursor position
   - Bring your thumb and index finger close together to click
   - Keep fingers apart to move without clicking

3. Press 'q' to quit the application

## Controls
- **Cursor Movement**: Move your index finger in the camera view
- **Click Action**: Bring thumb and index finger close together (distance < 30 pixels)
- **Exit**: Press 'q' key while the application window is focused

## Notes
- Works best in well-lit environments
- Requires a webcam with decent resolution
- The click action has a 1-second cooldown to prevent multiple rapid clicks
- For best results, use a plain background and avoid wearing rings or jewelry that might confuse the hand tracking

## Future Improvements
- Add right-click functionality
- Implement scrolling gestures
- Add gesture recognition for other mouse actions
- Improve performance and accuracy

