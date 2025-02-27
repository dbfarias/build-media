import cv2
import numpy as np

class VideoEditor:
    def __init__(self, input_path, output_path, overlay_path, text):
        self.input_path = input_path
        self.output_path = output_path
        self.overlay_path = overlay_path
        self.text = text

    def apply_effects(self):
        """Aplica efeitos ao vídeo, incluindo filtro cinza, overlay piscando e texto centralizado"""

        cap = cv2.VideoCapture(self.input_path)

        # Obtém detalhes do vídeo
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))

        # Criando um vídeo de saída
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(self.output_path, fourcc, fps, (frame_width, frame_height))

        # Carrega a imagem de overlay
        overlay = cv2.imread(self.overlay_path, cv2.IMREAD_UNCHANGED)

        # Redimensionar overlay para garantir que ele caiba no vídeo (máximo 20% do tamanho do vídeo)
        max_width = int(frame_width * 0.2)
        max_height = int(frame_height * 0.2)
        overlay = cv2.resize(overlay, (max_width, max_height))

        overlay_height, overlay_width = overlay.shape[:2]

        # Separar canais de cor e transparência, caso exista um canal alpha (4º canal)
        if overlay.shape[2] == 4:
            overlay_rgb = overlay[:, :, :3]  # Pega apenas os canais BGR
            overlay_alpha = overlay[:, :, 3] / 255.0  # Normaliza a transparência (0 a 1)
        else:
            overlay_rgb = overlay
            overlay_alpha = np.ones((overlay_height, overlay_width), dtype=np.float32)  # Sem transparência

        frame_count = 0  # Contador de frames para piscar

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Aplica o efeito preto e branco
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)

            # Define posição do overlay (canto inferior direito)
            x_offset = frame_width - overlay_width - 10  # 10px de margem
            y_offset = frame_height - overlay_height - 10

            # Pisca a cada 2 segundos (fps * 2)
            if (frame_count // (fps * 2)) % 2 == 0:
                # Extrai a região onde será aplicado o overlay
                roi = gray_frame[y_offset:y_offset + overlay_height, x_offset:x_offset + overlay_width]

                # Mescla o overlay com o vídeo, considerando a transparência
                for c in range(0, 3):  # Itera pelos canais de cor (BGR)
                    roi[:, :, c] = (1 - overlay_alpha) * roi[:, :, c] + overlay_alpha * overlay_rgb[:, :, c]

                # Substitui a região original pelo overlay mesclado
                gray_frame[y_offset:y_offset + overlay_height, x_offset:x_offset + overlay_width] = roi

            # 📌 Adicionando o texto no centro do vídeo
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 1.5  # Tamanho da fonte
            font_color = (0, 255, 255)  # Amarelo (BGR)
            thickness = 3
            text_size = cv2.getTextSize(self.text, font, font_scale, thickness)[0]
            text_x = (frame_width - text_size[0]) // 2
            text_y = (frame_height + text_size[1]) // 2

            cv2.putText(gray_frame, self.text, (text_x, text_y), font, font_scale, font_color, thickness, cv2.LINE_AA)

            # Escreve o frame no vídeo de saída
            out.write(gray_frame)

            frame_count += 1  # Incrementa o contador de frames

        cap.release()
        out.release()
        print(f"Vídeo processado e salvo em {self.output_path}")