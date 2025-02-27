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
git clone https://github.com/YOUR_GITHUB_USERNAME/video-editor.git
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
assets/output.mp4

