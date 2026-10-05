import cv2
import mediapipe as mp

# MediaPipe hand setup
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7
)

# Start webcam
cap = cv2.VideoCapture(0)

while True:

    # Read frame
    success, frame = cap.read()

    if not success:
        break

    # Flip the frame
    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hand
    result = hands.process(rgb)

    gesture = "No hand"

    if result.multi_hand_landmarks:

        for hand in result.multi_hand_landmarks:

            # Get landmarks
            wrist = hand.landmark[0]

            thumb_tip = hand.landmark[4]
            index_tip = hand.landmark[8]
            middle_tip = hand.landmark[12]
            ring_tip = hand.landmark[16]
            pinky_tip = hand.landmark[20]

            index_pip = hand.landmark[6]
            middle_pip = hand.landmark[10]
            ring_pip = hand.landmark[14]
            pinky_pip = hand.landmark[18]

            # Check which fingers are up
            index_up = index_tip.y < index_pip.y
            middle_up = middle_tip.y < middle_pip.y
            ring_up = ring_tip.y < ring_pip.y
            pinky_up = pinky_tip.y < pinky_pip.y

            # Gesture recognition
            if index_up and middle_up and ring_up and pinky_up:
                gesture = "OPEN HAND"

            elif not index_up and not middle_up and not ring_up and not pinky_up:
                gesture = "CLOSED HAND"

            elif index_up and not middle_up and not ring_up and not pinky_up:
                gesture = "ONE"

            elif index_up and middle_up and not ring_up and not pinky_up:
                gesture = "TWO"

            else:
                gesture = "UNKNOWN"

            # Draw hand landmarks
            mp_draw.draw_landmarks(
                frame,
                hand,
                mp_hands.HAND_CONNECTIONS
            )

    # Display gesture
    cv2.putText(
        frame,
        gesture,
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Show frame
    cv2.imshow("Sign Gesture Translator", frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()