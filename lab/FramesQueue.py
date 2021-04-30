#!/usr/bin/env python3

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
