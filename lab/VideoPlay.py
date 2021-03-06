#! /usr/bin/env python3

from threading import *
from ProcessVideo import *

threadNum = 0

class ExtractConverDisplay(Thread):
    def __init__(self, stage):
        global threadNum
        Thread.__init__(self, name="Thread-%d" % threadNum)
        threadNum += 1
        self.stage = stage
    def run(self):
        print("CREATED: Thread-%d" % threadNum)
        if(self.stage == 0):        # Extract
            extractFrames()
        elif(self.stage == 1):      # Convert
            convertToGrayscale()
        elif(self.stage == 2):      # Display
            displayFrames()

if __name__ == "__main__":
    ExtractConverDisplay(0).start() # Extract
    ExtractConverDisplay(1).start() # Convert
    ExtractConverDisplay(2).start() # Display
