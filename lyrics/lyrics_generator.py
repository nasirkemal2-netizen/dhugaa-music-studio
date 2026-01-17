# lyrics_generator.py
# Phase 1c: Lyrics generation + AI melody
import os

LYRICS_DIR = "lyrics"
os.makedirs(LYRICS_DIR, exist_ok=True)

# -------- EXAMPLE LYRICS --------
lyrics_sample = """
Yaa ooh aaaaa
Siin jaaladha, qalbii koo guutuu siif kenna
Alfee koo, si wajjin jiraachuu feena
"""

def save_lyrics(filename, lyrics_text):
    path = os.path.join(LYRICS_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(lyrics_text)
    print(f"Lyrics saved: {path}")

# -------- MAIN --------
if __name__ == "__main__":
    save_lyrics("sample_lyrics.txt", lyrics_sample)
