# create_dummy_audio.py
# Creates a dummy WAV audio file for testing Dhugaa Music Studio
import os
import wave
import numpy as np

# -------- CONFIGURATION --------
AUDIO_DIR = "audio/record"
os.makedirs(AUDIO_DIR, exist_ok=True)
DUMMY_FILE = "my_song.wav"

# -------- CREATE DUMMY AUDIO --------
def create_dummy_wav(filename, duration_sec=3, sample_rate=44100):
    t = np.linspace(0, duration_sec, int(sample_rate*duration_sec))
    data = (np.sin(2*np.pi*440*t) * 32767).astype(np.int16)  # simple sine wave tone
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(data.tobytes())
    print(f"Dummy audio created: {filename}")

# -------- MAIN --------
if __name__ == "__main__":
    dummy_path = os.path.join(AUDIO_DIR, DUMMY_FILE)
    create_dummy_wav(dummy_path)
