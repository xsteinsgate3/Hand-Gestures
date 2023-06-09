'''
    -- Government Technical Institute -- 

    CLASS: ODCS2
    LECTURER: Sir Samaroo Randolph
    DATE: 26/04/2023
    
    DEVELOPERS:
        Roclay Rodrigues and Christopher McKay
'''

import cv2
import mediapipe as mp
import time
import random

def count_fingers(lst):
    cnt = 0

    thresh = (lst.landmark[0].y*100 - lst.landmark[9].y*100)/2

    if (lst.landmark[5].y*100 - lst.landmark[8].y*100) > thresh:
        cnt += 1

    if (lst.landmark[9].y*100 - lst.landmark[12].y*100) > thresh:
        cnt += 1

    if (lst.landmark[13].y*100 - lst.landmark[16].y*100) > thresh:
        cnt += 1

    if (lst.landmark[17].y*100 - lst.landmark[20].y*100) > thresh:
        cnt += 1

    if (lst.landmark[5].x*100 - lst.landmark[4].x*100) > 6:
        cnt += 1

    return cnt

cap = cv2.VideoCapture(0)

drawing = mp.solutions.drawing_utils
hands = mp.solutions.hands
hand_obj = hands.Hands(max_num_hands=1)

# selects random of three
options = ["paper", "scissors", "rock"]
bot = random.choice(options)

player = None
winner = None

start_init = False

prev = -1

while True:
    end_time = time.time()
    _, frm = cap.read()
    frm = cv2.flip(frm, 1)

    res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

    if res.multi_hand_landmarks:

        hand_keyPoints = res.multi_hand_landmarks[0]

        cnt = count_fingers(hand_keyPoints)

        if not (prev == cnt):
            if not (start_init):
                start_time = time.time()
                start_init = True

            elif (end_time-start_time) > 1:
                if (cnt == 2):
                    player = "scissors"

                elif (cnt == 5):
                    player = "paper"

                elif (cnt == 0):
                    player = "rock"

                else:
                    player = None

                prev = cnt
                start_init = False

        drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)

    cv2.putText(frm, f"Player: {player}      Bot: {bot}",(0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA, False)

    cv2.putText(frm, f"Winner: {winner}",(0, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA, False)

    cv2.imshow("window", frm)

    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        cap.release()
        break

    if player:
        if player == "paper" and bot == "rock":
            winner = "Player"
            
        elif player == "rock" and bot == "scissors":
            winner = "Player"

        elif player == "scissors" and bot == "paper":
            winner = "Player"

        else:
            winner = "Bot"

    else:
        winner = "Undetermined"