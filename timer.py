#!/usr/bin/env python3
import time, threading

class Watch:
    def __init__(self):
        self.hr = 00
        self.mint = 00
        self.sec = 00
        self.main_process()
               
    def main_process(self):
    
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.mint += 1
        elif self.mint == 60:
            self.mint = 0
            self.hr += 1
        else:
            pass
        print("\r[+]TIME: " + str(self.hr) + ":" + str(self.mint) + ":" + str(self.sec), end=" ")
        timer = threading.Timer(1,self.main_process)
        timer.start()

        
Watch()
