# generator.py
# Dhugaa Music Studio – Phase 1c
# Simple lyrics generator (text-based)

import os

# Folder where lyrics will be saved
LYRICS_DIR = "lyrics"
os.makedirs(LYRICS_DIR, exist_ok=True)

# Sample lyrics (Afaan Oromoo + English)
lyrics_sample = """
Dhugaan ifa dha
Sagaleen qalbii namaa
Sirbi keenya eenyummaa
Aadaa keenyaaf faana

Truth is light
Music is identity
Our voice is culture
Our future is unity
"""

def save_lyrics(filename, lyrics_text):
    path = os.path.join(LYRICS_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(lyrics_text)
    print(f"Lyrics saved: {path}")

if __name__ == "__main__":
    save_lyrics("sample_lyrics.txt", lyrics_sample)