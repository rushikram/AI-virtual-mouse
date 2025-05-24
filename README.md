
🖱️ Virtual Mouse Using Hand Tracking
This project implements a virtual mouse using OpenCV, MediaPipe, and PyAutoGUI. It enables mouse control through hand gestures captured via a webcam.

📹 Demo
Move your index finger to control the mouse cursor.


https://github.com/user-attachments/assets/13c22803-a6d5-4733-8295-b5ca1ff7d115


Touch your thumb and index finger together to perform a click.



🔧 Features
Hand tracking using MediaPipe

Cursor control based on index finger position

Click event triggered by pinching (thumb + index finger)

Real-time performance with webcam input

🧰 Dependencies
Install the required libraries with pip:

bash
Copy
Edit
pip install opencv-python mediapipe pyautogui
🚀 How to Run
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/yourusername/virtual-mouse-handtracking.git
cd virtual-mouse-handtracking
Run the Script:

bash
Copy
Edit
python virtual_mouse.py
A window will open showing the webcam feed. Move your hand to control the mouse.

🖐️ Controls
Gesture	Action
Move index finger	Move cursor
Pinch (index + thumb close)	Mouse click
Press q	Exit program

🛠️ How It Works
MediaPipe Hands detects 21 landmarks per hand.

The index fingertip (landmark 8) is used to move the mouse cursor.

The distance between the index finger and thumb (landmark 4) is measured.

If the distance is less than a threshold (e.g., 30px), a click is triggered.

⚠️ Notes
Works best in well-lit environments.

Only tracks one hand (set with max_num_hands=1).

Cursor movement may vary slightly depending on your screen resolution.
