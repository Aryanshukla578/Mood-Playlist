# main.py

from fastapi import FastAPI, UploadFile, File, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import cv2
import numpy as np
from deepface import DeepFace
import uvicorn

# Load environment variables
load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI", "https://v0-image-analysis-aom8w9a07-aryanshukla578s-projects.vercel.app/callback")

if not SPOTIFY_CLIENT_ID or not SPOTIFY_CLIENT_SECRET:
    raise EnvironmentError("Missing Spotify credentials. Check your .env file.")

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

MOOD_PLAYLISTS = {
    "happy": "Happy Songs",
    "sad": "Sad Songs",
    "angry": "Workout Music",
    "surprise": "Surprising Soundtracks",
    "fear": "Relaxing Calm Music",
    "neutral": "LoFi Chill Beats"
}

spotify = Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="playlist-read-private"
))

def search_spotify_playlists(query, max_results=1):
    results = spotify.search(q=query, type="playlist", limit=max_results)
    return [
        {"name": item["name"], "url": item["external_urls"]["spotify"]}
        for item in results["playlists"]["items"]
    ]

@app.get("/")
def index():
    return HTMLResponse("""
        <h2>Mood Detection with Playlist</h2>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <button type="submit">Upload Face Image</button>
        </form>
    """)

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    try:
        analysis = DeepFace.analyze(img_path=img, actions=['emotion'], enforce_detection=False)
        emotion = analysis[0]['dominant_emotion']
        mood_label = emotion.lower()
        playlist_query = MOOD_PLAYLISTS.get(mood_label, "Chill Vibes")
        playlists = search_spotify_playlists(playlist_query)

        html = f"<h3>Detected Mood: {emotion}</h3>"
        for playlist in playlists:
            html += f'<p><a href="{playlist["url"]}" target="_blank">{playlist["name"]}</a></p>'
        return HTMLResponse(html)

    except Exception as e:
        return HTMLResponse(f"<p>Error detecting emotion: {str(e)}</p>")

@app.get("/callback")
async def spotify_callback(request: Request):
    code = request.query_params.get("code")
    return HTMLResponse(f"<p>Received Spotify code: {code}</p>")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
