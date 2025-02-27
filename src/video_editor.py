import cv2
import numpy as np
import moviepy.editor as mp
from PIL import Image
from moviepy.video.VideoClip import ImageClip

class VideoEditor:
    def __init__(self, input_video):
        self.video = mp.VideoFileClip(input_video)

    def remove_background(self, lower_bound=(35, 50, 50), upper_bound=(85, 255, 255)):
        def process_frame(frame):
            hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
            mask = cv2.inRange(hsv, np.array(lower_bound), np.array(upper_bound))
            frame[mask > 0] = [255, 255, 255]
            return frame

        self.video = self.video.fl_image(process_frame)

    def add_overlay(self, image_path, position=("center", "top")):
        image = Image.open(image_path).resize((200, 200))
        image_clip = ImageClip(np.array(image), duration=self.video.duration)
        image_clip = image_clip.set_position(position)
        self.video = mp.CompositeVideoClip([self.video, image_clip])

    def export(self, output_path="output.mp4"):
        self.video.write_videofile(output_path, codec="libx264", fps=self.video.fps)