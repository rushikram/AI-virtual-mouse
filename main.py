import cv2
import mediapipe as mp
import pyautogui
import math
import time


cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()


prev_click_time = 0

while True:
    success, frame = cap.read()
    if not success:
        break

    # Flip and convert color
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_height, frame_width, _ = frame.shape


    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)


            landmarks = hand_landmarks.landmark
            index_finger_tip = landmarks[8]
            thumb_tip = landmarks[4]


            index_x = int(index_finger_tip.x * frame_width)
            index_y = int(index_finger_tip.y * frame_height)
            thumb_x = int(thumb_tip.x * frame_width)
            thumb_y = int(thumb_tip.y * frame_height)


            cv2.circle(frame, (index_x, index_y), 10, (0, 255, 0), -1)
            cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 0, 255), -1)


            screen_x = screen_width / frame_width * index_x
            screen_y = screen_height / frame_height * index_y


            pyautogui.moveTo(screen_x, screen_y)


            distance = math.hypot(index_x - thumb_x, index_y - thumb_y)
            if distance < 30:
                current_time = time.time()
                if current_time - prev_click_time > 1:
                    pyautogui.click()
                    prev_click_time = current_time


    cv2.imshow("Virtual Mouse", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
