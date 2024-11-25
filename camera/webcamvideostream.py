from threading import Thread
import time
import cv2

class WebcamVideoStream:
    def __init__(self, src=0):
        '''initialize the video camera stream and read
        the first frame from the stream'''
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.warming_time = 2
        self.stopped = False
        
    def start(self):
        '''Start the thread to read frames from the video stream'''
        Thread(target=self.update, args=()).start()
        time.sleep(self.warming_time)
        return self
    
    def update(self):
        '''Keep looping infinitely until the thread is stopped'''
        while True:  
            if self.stopped:
                self.stream.release()
                return
            else:
                (self.grabbed, self.frame) = self.stream.read()       
            
    def read(self):
        '''Return the frame most recently read'''
        return self.frame
        
    def isOpen(self):
        return self.stream.isOpen()
    
    def stop(self):
        '''Indicate that the thread should be stopped'''
        self.stopped = True