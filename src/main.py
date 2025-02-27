import sys
from video_editor import VideoEditor

if __name__ == "__main__":
    input_video = "assets/input_video.mp4"
    output_video = "assets/output.mp4"
    overlay_image = "assets/overlay.png"

    # Obtém o texto do argumento do Docker, limitando a 10 caracteres
    text = "DefaultTXT"  # Texto padrão
    if len(sys.argv) > 1:
        text = sys.argv[1][:10]  # Limita a 10 caracteres

    editor = VideoEditor(input_video, output_video, overlay_image, text)
    editor.apply_effects()