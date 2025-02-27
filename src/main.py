from video_editor import VideoEditor

if __name__ == "__main__":
    input_video = "assets/input_video.mp4"
    output_video = "assets/output.mp4"

    editor = VideoEditor(input_video, output_video)
    editor.apply_gray_filter()