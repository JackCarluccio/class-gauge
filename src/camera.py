import numpy as np
import pyrealsense2 as rs

class Camera:
    def __init__(self):
        self._callbacks = []
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)


    def register_callback(self, callback):
        self._callbacks.append(callback)


    def _notify_callbacks(self, frame):
        for callback in self._callbacks:
            callback(frame)


    def start(self):
        self.pipeline.start(self.config)
        try:
            while True:
                frames = self.pipeline.wait_for_frames()
                color_frame = frames.get_color_frame()
                if not color_frame:
                    continue
                
                frame_data = np.asanyarray(color_frame.get_data())
                self._notify_callbacks(frame_data)
        except KeyboardInterrupt:
            print("Camera stream interrupted by user.")
        finally:
            self.pipeline.stop()


# Example usage:
if __name__ == "__main__":
    def process_frame(frame):
        print("Received a new frame with shape:", frame.shape)
    
    camera = Camera()
    camera.register_callback(process_frame)
    camera.start()