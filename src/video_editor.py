import cv2

class VideoEditor:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def apply_gray_filter(self):
        """Aplica filtro preto e branco ao vídeo"""
        cap = cv2.VideoCapture(self.input_path)

        # Obtém detalhes do vídeo
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))

        # Criando um vídeo de saída
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(self.output_path, fourcc, fps, (frame_width, frame_height))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Aplicar efeito preto e branco
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)

            # Escrever o frame no vídeo de saída
            out.write(gray_frame)

        cap.release()
        out.release()
        print(f"Vídeo processado e salvo em {self.output_path}")