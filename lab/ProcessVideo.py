#!/usr/bin/env python3

import cv2
import numpy as np
import base64
import os
import threading
import FramesQueue

def extractFrames():
    clipFileName = 'clip.mp4'
    count = 0                               # initialize frame count
    
    vidcap = cv2.VideoCapture(clipFileName) # open video clip
    success,image = vidcap.read()           # read first frame
    print(f'Reading frame {count} {success}')
    
    while success and count < 72:           # vid is 72 frames
        FramesQueue.insert(image)           # insert image into FramesQueue
        success,image = vidcap.read()       # read next frame
        print(f'Reading frame {count}')
        count += 1
    self.insert(None)                       # insert finished indicator
    print('Frame extraction complete!')

