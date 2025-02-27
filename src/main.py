from video_editor import VideoEditor

if __name__ == "__main__":
    editor = VideoEditor("assets/input_video.mp4")
    editor.remove_background()
    editor.add_overlay("assets/overlay.png")
    editor.export("assets/output.mp4")