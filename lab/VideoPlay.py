#! /usr/bin/env python3

from threading import *
from ProcessVideo import *

threadNum = 0

class Extractor(Thread):
    def __init__(self):
        global threadNum
        Thread.__init__(self, name="Thread-%d" % threadNum)
        threadNum += 1
    def run(self):
        print("Working in Thread-%d" % threadNum)
        extractFrames()

class GrayscaleConverter(Thread):
    def __init__(self):
        global threadNum
        Thread.__init__(self, name="Thread-%d" % threadNum)
        threadNum += 1
    def run(self):
        print("Working in Thread-%d" % threadNum)
        convertToGrayscale()

class Display(Thread):
    def __init__(self):
        global threadNum
        Thread.__init__(self, name="Thread-%d" % threadNum)
        threadNum += 1
    def run(self):
        print("Working in Thread-%d" % threadNum)
        displayFrames()

if __name__ == "__main__":
    Extractor().start()
    GrayscaleConverter().start
    Display().start()
