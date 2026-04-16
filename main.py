import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture('Task Manager')

loop_time = time()
while True:

    try:
        screenshot = wincap.get_screenshot()
    except Exception as e:
        print("Capture failed:", e)
        break

    if screenshot is None:
        print("Screenshot returned None")
        break

    cv.imshow('Computer Vision', screenshot)

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
