# Import required libraries
import cv2
import pandas as pd
import time
from datetime import datetime

# Initialise variables
stillImage = None
motionImage = [None, None]
time = []

# Initializing the DataFrame with start and end time
df = pd.DataFrame(columns=["start", "end"])

# Capturing video
video = cv2.VideoCapture(0)

while True:
    # Start reading image from video
    check, frame = video.read()
    motion = 0

    # Convert color image to gray_scale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    if stillImage is None:
        stillImage = gray
        continue
    # Still Image and current image.
    diff_frame = cv2.absdiff(stillImage, gray)

    # change the image to white if static background and current frame is greater than 25.
    thresh_frame = cv2.threshold(diff_frame, 25, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
    # Finding contour and hierarchy from a moving object.
    contours, hierachy = cv2.findContours(thresh_frame.copy(),
                                          cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            continue
        motion = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    # Append current status of motion
    motionImage.append(motion)
    motionImage = motionImage[-2:]
    # Append Start time of motion
    if motionImage[-1] == 1 and motionImage[-2] == 0:
        time.append(datetime.now())

    # Append End time of motion
    if motionImage[-1] == 0 and motionImage[-2] == 1:
        time.append(datetime.now())
    # Displaying image in gray_scale
    cv2.imshow("Gray_Frame", gray)

    # Display black and white frame & if the intensity difference is > 25, it turns white
    cv2.imshow("Threshold Frame", thresh_frame)
    # Display colored frame
    cv2.imshow("Colored_Frame", frame)

    key = cv2.waitKey(1)
    # Press q to stop the process
    if key == ord('q'):
        if motion == 1:
            time.append(datetime.now())
        break

# Append time of motion
for i in range(0, len(time), 2):
    df = df.append({"Start": time[i], "End": time[i + 1]}, ignore_index=True)

# Creating a csv file in which time of movements will be saved
df.to_csv("FrameInMotion_time.csv")

video.release()

# close window
cv2.destroyAllWindows()
