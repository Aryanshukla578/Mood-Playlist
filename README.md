
# 🎵 Mood Playlist: Your Personal Music Companion

**Turn your mood into music! Upload an image, let the app read your emotions, and get a custom Spotify playlist tailored just for you.**

🔗 **[Live Demo](https://v0-image-analysis-aom8w9a07-aryanshukla578s-projects.vercel.app/)**

---

## 🌟 What's Mood Playlist?

Mood Playlist is a cutting-edge web app that fuses **AI-powered emotion detection** with the magic of Spotify. Simply upload a photo, and let the app:
1. Analyze your facial expressions using AI.
2. Match your mood with the perfect Spotify playlist.
3. Instantly transport you to a world of tailor-made melodies.

---

## 🚀 Why You'll Love It

- 🎭 **Emotion Recognition**: Powered by **DeepFace**, the app detects emotions like happiness, sadness, and more from your photo.
- 🎧 **Spotify Sync**: Curated playlists fetched straight from Spotify.
- 🖼️ **User-Friendly Interface**: Effortlessly upload images and enjoy your music.
- ⚡ **Fast Backend**: Supercharged with **FastAPI** for smooth processing.

---

## 🛠️ Built With Love (and Code)

- **Backend:** FastAPI
- **AI/ML:** DeepFace (TensorFlow & OpenCV)
- **Music API:** Spotify Web API, Spotipy
- **Environment Management:** python-dotenv
- **Frontend:** HTML, CSS, JavaScript

---

## 📂 How It's Organized

```
Mood-Playlist/
├── main.py             # Backend API logic
├── .env                # Spotify credentials
├── static/             # Static assets (CSS, JS, images)
├── templates/          # HTML templates
└── README.md           # You're reading it!
```

---

## ⚙️ Getting Started

### 1️⃣ Clone & Setup
```bash
git clone https://github.com/Aryanshukla578/Mood-Playlist.git
cd Mood-Playlist
python -m venv venv
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 2️⃣ Add Your Spotify Credentials
Create a `.env` file in the root directory:
```plaintext
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
SPOTIFY_REDIRECT_URI=http://localhost:8000/callback
```

### 3️⃣ Run the App
```bash
uvicorn main:app --reload
```
Access the app at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🎉 How to Use

1. **Upload**: Submit a clear image of your face.
2. **Analyze**: AI detects your emotional state.
3. **Play**: Enjoy a Spotify playlist that perfectly matches your mood!

---

## 🤝 Want to Contribute?

We welcome your ideas and improvements! Fork the repo, make your changes, and submit a PR. Together, we can enhance the Mood Playlist experience. ✨

---

## 📸 Sneak Peek
![App Preview](static/sample-image.png)

🎨 **Made with ❤️ by [Aryanshukla578](https://github.com/Aryanshukla578)**. Feel free to star ⭐ the repo if you like it!
```

