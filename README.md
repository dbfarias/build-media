# Video Editor with OpenCV (Dockerized) 🎬

This project is a **video processing application** using **OpenCV** inside a **Docker container**.  
It applies a **grayscale filter** and overlays an image (`overlay.png`) that **blinks every 2 seconds** in the bottom right corner of the video.

## 🚀 Features
- ✅ Converts video to grayscale.  
- ✅ Adds an overlay image (`overlay.png`) in the **bottom-right corner**.  
- ✅ The overlay **blinks every 2 seconds**.  
- ✅ Fully **Dockerized** – No need to install dependencies manually!  

---

## 📌 Requirements
- **Docker** installed on your system.  
- A **video file** (`input_video.mp4`) placed inside the `assets/` folder.  
- An **overlay image** (`overlay.png`) inside the `assets/` folder.  

---

## 📌 Project Structure
video-editor/
│── src/
│   ├── main.py           # Runs the video processing
│   ├── video_editor.py   # Video editing logic (OpenCV)
│── assets/
│   ├── input_video.mp4   # Input video file (required)
│   ├── overlay.png       # Image to overlay (required)
│── requirements.txt      # Python dependencies
│── Dockerfile            # Docker setup
│── README.md             # Documentation

---

## 📌 How to Use

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/dbfarias/video-editor.git
cd video-editor
```
2️⃣ Build the Docker Image
```bash
docker build -t video-editor .
```
3️⃣ Run the Container
```bash
docker run --rm -v "$(pwd)/assets:/app/assets" video-editor
```
After execution, the processed video will be saved as:
```bash
assets/output.mp4
```

## 📌 Dependencies

The project uses the following Python libraries:
```bash
opencv-python
numpy
pillow
ffmpeg-python
```

## 📌 How It Works
	1.	Opens the input video (input_video.mp4).
	2.	Converts each frame to grayscale.
	3.	Loads the overlay image (overlay.png) and resizes it to fit in the bottom-right corner.
	4.	Makes the overlay blink every 2 seconds.
	5.	Saves the processed video as output.mp4.

## 📌 Notes
	•	The overlay.png image must be smaller than the video resolution.
	•	If overlay.png has transparency, it will be smoothly blended with the video.

📌 Troubleshooting

❓ “Could not broadcast input array” error?

This happens if overlay.png has an alpha channel (RGBA) but the video is only RGB.
This is automatically handled in the latest version of video_editor.py.

❓ Docker volume error (invalid reference format)?

Try adding quotes around $(pwd) when running the container:
```bash
docker run --rm -v "$(pwd)/assets:/app/assets" video-editor
```
