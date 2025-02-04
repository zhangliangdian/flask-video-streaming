import os, logging
import cv2
from base_camera import BaseCamera


class Camera(BaseCamera):
    video_source = 0

    def __init__(self):
        if os.environ.get('OPENCV_CAMERA_SOURCE'):
            Camera.set_video_source(int(os.environ['OPENCV_CAMERA_SOURCE']))
        super(Camera, self).__init__()

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        logging.debug("opencv frames() start")
        camera = cv2.VideoCapture(Camera.video_source)
        # camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        # camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        # camera.set(cv2.CAP_PROP_FPS, 30)
        logging.debug("VideoCapture OK")
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
