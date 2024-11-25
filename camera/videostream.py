from webcamvideostream import WebcamVideoStream

class VideoStream:
    def __init__(self, src=0, usePiCamera=False, resolution=(800,600)):
        if usePiCamera:
            from mypicamera import MyPiCamera
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
        
