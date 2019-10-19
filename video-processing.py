import cv2
import numpy as np

#Create a videocapture object and read input from file
#Camera input pass 0, not video
#This simple python code is to open an mp4 format video frames by frames.
#Can be utilized for any other type of video / frame processing.

cap = cv2.VideoCapture('video-test.mp4') 
fgbg = cv2.createBackgroundSubtractorMOG2()

#Check file opening status
if (cap.isOpened()==False):
    print("Error opening video stream or file")
else:
    print("Successfully opening the media file")

    # Count frames
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print('Total frame counted :', length)

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()

  frameS = cv2.resize(frame, (640,480))

  #Image processing here
  fgmask = fgbg.apply(frameS)
  gray = cv2.cvtColor(frameS, cv2.COLOR_BGR2GRAY)

  # Capture frame-by-frame [R,G,B] matrix
  # success, image = cap.read()
  # print(image)

  if ret == True:
    # Display the resulting frame in color
    cv2.imshow('Frame',frameS)

    # Display the resulting frame in Background Substractor MOG2
    cv2.imshow('frameS',fgmask)

    # Display the resulting frame in grayscale
    # cv2.imshow('frameS',gray)

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
  # Break the loop
  else:
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
