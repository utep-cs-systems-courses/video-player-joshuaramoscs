#!/usr/bin/env python3

import cv2
import numpy as np
import base64
import os
import time
import threading
import FramesQueue

global framesQ = FramesQueue()
global grayscaleFramesQ = FramesQueue()

def extractFrames():                        # Extract frames from clip and queue them
    global framesQ
    clipFileName = 'clip.mp4'
    count = 0                               # initialize frame count
    
    vidcap = cv2.VideoCapture(clipFileName) # open video clip
    success,frame = vidcap.read()           # read first frame
    print(f'READING: frame {count} {success}')
    
    while success and count < 72:           # vid is 72 frames
        print(f'Reading frame {count}')
        framesQ.insert(frame)               # insert frame into FramesQueue
        count += 1
        success,frame = vidcap.read()       # read next frame
    framesQ.insert(None)                    # insert finished indicator
    print('FINISHED: Extracting frames')

def convertToGrayScale():                   # Convert frames from queue to grayscale and queue them
    global framesQ, grayscaleFramesQ
    count = 0                               # initialize frame count
    frame = framesQ.remove()                # retrieve the first frame from queue

    while frame is not None: # convert until error or end
        print(f'CONVERTING frame {count}')
        grayscaleFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert image to grayscale
        grayscaleFramesQ.insert(grayscaleFrame) # insert grayscale frame into grayscaleFramesQ
        count += 1
        frame = framesQ.remove()            # retrieve the next frame from queue
    grayscaleFramesQ.insert(None)
    print('FINISHED Converting frames!')
    
def displayFrames():                        # Display frames from grayscale queue
    global grayscaleFramesQ
    frameDelay   = 42
    count = 0                               # initialize frame count
    frame = grayscaleFramesQ.remove()       # retrieve the first frame

    while frame is not None:                # display until error or end
        print(f'DISPLAYING: frame {count}')
        cv2.imshow('Video', frame)          # Display the frame in a window called "Video"
                                            # Wait for 42 ms and check if the user wants to quit
        if cv2.waitKey(frameDelay) and 0xFF == ord("q"):
            break
        count += 1
        frame = grayscaleFramesQ.remove()   # retreive the next frame from queue
    print('FINISHED: Displaying frames!')
    # make sure we cleanup the windows, otherwise we might end up with a mess
    cv2.destroyAllWindows()
