# simple_beats.py
# Phase 1b: Basic beat & melody generation
# Generates simple sine wave beats and saves as WAV

import os
import wave
import numpy as np

# -------- CONFIGURATION --------
BEATS_DIR = "beats"
os.makedirs(BEATS_DIR, exist_ok=True)

def generate_simple_beat(filename, duration_sec=3, bpm=120, sample_rate=44100):
    """
    Generate a simple sine-wave beat for testing
    """
    t = np.linspace(0, duration_sec, int(sample_rate*duration_sec))
    freq = 440  # A4 tone
    beat_wave = (np.sin(2*np.pi*freq*t) * 32767).astype(np.int16)
    
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(beat_wave.tobytes())

# -------- MAIN --------
if __name__ == "__main__":
    output_file = os.path.join(BEATS_DIR, "test_beat.wav")
    generate_simple_beat(output_file)
    print(f"Simple beat generated: {output_file}")
