from webcamvideostream import WebcamVideoStream
from mypicamera import MyPiCamera

class VideoStream:
    def __init__(self, src=0, usePiCamera=False, resolution=(800,600)):
        if usePiCamera:
            self.stream = MyPiCamera(resolution=resolution)
        else:
            self.stream = WebcamVideoStream(src=src)
            
    def start(self):
        return self.stream.start()
    
    def read(self):
        frame = self.stream.read()
        return frame
        
    def stop(self):
        self.stream.stop()
        