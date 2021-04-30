#!/usr/bin/env python3

import cv2
import numpy as np
import base64
import os
import threading

class FramesQueue:
    def __init__(self):
        self.buff = list()
        self.full = semaphore(0)    # starts at 0 since buff is empty
        self.empty = semaphonre(10) # starts at 10 since we only want to hold 10 frames

    def insert(self, frame):     # insert into end of the "queue", will block if buff has 10 frames
        self.empty.acquire()     # decrement empty semaphore since we are filling buff
        self.buff.append(frame)  # append frame to the end of the buffer
        self.full.release()      # increment full since we just took a spot

    def remove(self):            # remove from the front of the "queue", will block while empty
        self.full.acquire()      # decrement full semaphore since we are removing from buff
        frame = self.buff.pop(0) # remove frame from the front of buff
        self.empty.release()     # increment empty since we just opened a spot
        return frame

    def extractFrames():
        # outputDir    = 'frames'
        clipFileName = 'clip.mp4'
        count = 0                               # initialize frame count
        vidcap = cv2.VideoCapture(clipFileName) # open video clip

        # if not os.path.exists(outputDir):       # create the output directory if it doesn't exits
        #     print(f"Output directory {outputDir} didn't exist, creating")
        #     os.makedirs(outputDir)

        success,image = vidcap.read()           # read first frame
        
        print(f'Reading frame {count} {success}')
        while success and count < 72:           # vid is 72 frames
            self.insert(image)                  # insert image into "queue" aka buff
            
            # write the current frame out as a jpeg image
            # cv2.imwrite(f"{outputDir}/frame_{count:04d}.bmp", image)
            success,image = vidcap.read()       # read next frame
            print(f'Reading frame {count}')
            count += 1
        self.insert(None)
        print('Frame extraction complete!')

    def convertToGrayScale():
        # outputDir    = 'frames'
        count = 0 # initialize frame count

        # get the next frame file name
        # inFileName = f'{outputDir}/frame_{count:04d}.bmp'
        image = self.remove()
        
        # load the next file
        inputFrame = cv2.imread(inFileName, cv2.IMREAD_COLOR)

        while inputFrame is not None and count < 72:
            print(f'Converting frame {count}')

            # convert the image to grayscale
            grayscaleFrame = cv2.cvtColor(inputFrame, cv2.COLOR_BGR2GRAY)

            # generate output file name
            outFileName = f'{outputDir}/grayscale_{count:04d}.bmp'

            # write output file
            cv2.imwrite(outFileName, grayscaleFrame)

            count += 1

            # generate input file name for the next frame
            inFileName = f'{outputDir}/frame_{count:04d}.bmp'

            # load the next frame
            inputFrame = cv2.imread(inFileName, cv2.IMREAD_COLOR)

    def displayFrames():
        #some
