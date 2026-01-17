# studio_phase1a_test.py
# Test workflow for Dhugaa Music Studio
# Creates a dummy audio file, runs Phase 1a script, exports MP3

import os
import wave
import numpy as np
import subprocess

# -------- CONFIGURATION --------
AUDIO_DIR = "audio/record"
CLEAN_DIR = "audio/clean"
EXPORT_DIR = "audio/export"
DUMMY_FILE = "my_dummy_song.wav"

# Ensure folders exist
for folder in [AUDIO_DIR, CLEAN_DIR, EXPORT_DIR]:
    os.makedirs(folder, exist_ok=True)

# -------- CREATE DUMMY AUDIO --------
def create_dummy_wav(filename, duration_sec=3, sample_rate=44100):
    t = np.linspace(0, duration_sec, int(sample_rate*duration_sec))
    data = (np.sin(2*np.pi*440*t) * 32767).astype(np.int16)  # simple sine wave
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(data.tobytes())

dummy_path = os.path.join(AUDIO_DIR, DUMMY_FILE)
create_dummy_wav(dummy_path)
print(f"Dummy audio created: {dummy_path}")

# -------- RUN Phase1a SCRIPT --------
print("Running studio_phase1a.py workflow...")
subprocess.run(["python3", "scripts/studio_phase1a.py"])
print("Test workflow complete!")
