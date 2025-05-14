# 🎵 Mood Playlist App

**Detect your mood from an image and receive a personalized Spotify playlist recommendation.**

🔗 **Live Demo**: [https://v0-image-analysis-aom8w9a07-aryanshukla578s-projects.vercel.app/](https://v0-image-analysis-aom8w9a07-aryanshukla578s-projects.vercel.app/)

---

## 📸 Overview

Mood Playlist App is a web application that analyzes facial expressions from uploaded images to determine the user's mood. Based on the detected emotion, it suggests a curated Spotify playlist to match the mood.

---

## 🚀 Features

- **Facial Emotion Detection** with DeepFace
- **Spotify Integration** to fetch matching playlists
- **Simple Upload Interface** for users
- **FastAPI Backend** for quick processing

---

## 🛠️ Tech Stack

- **Backend:** FastAPI
- **ML:** DeepFace (built on TensorFlow & OpenCV)
- **Spotify:** Web API & Spotipy
- **Env Config:** python-dotenv

---

## 📂 Project Structure

mood-playlist-app/
├── main.py
├── .env
├── static/
├── templates/
└── README.md

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/mood-playlist-app.git
cd mood-playlist-app
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt

Add your .env file
Create a .env file in the root directory:
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
SPOTIFY_REDIRECT_URI=http://localhost:8000/callback
Run the app
bash
Copy
Edit
uvicorn main:app --reload
Go to: http://127.0.0.1:8000

📌 How to Use
Upload a clear face image.

The app analyzes your emotion.

It fetches a Spotify playlist that matches your mood.

Click and enjoy your playlist!

🤝 Contributing
Feel free to fork and contribute. PRs are welcome!

