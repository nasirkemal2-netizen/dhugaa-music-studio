# studio_phase1a1b.py
# Combined Phase 1a + Phase 1b workflow
# Record → Clean → Trim → Add simple beat → Export MP3

import os
import subprocess
import wave
import numpy as np

# -------- CONFIGURATION --------
AUDIO_DIR = "audio/record"
CLEAN_DIR = "audio/clean"
EXPORT_DIR = "audio/export"
BEATS_DIR = "beats"
DUMMY_BEAT_FILE = "beats/test_beat.wav"

# Ensure folders exist
for folder in [AUDIO_DIR, CLEAN_DIR, EXPORT_DIR, BEATS_DIR]:
    os.makedirs(folder, exist_ok=True)

# -------- PHASE 1b: Generate simple beat --------
def generate_simple_beat(filename, duration_sec=3, freq=440, sample_rate=44100):
    t = np.linspace(0, duration_sec, int(sample_rate*duration_sec))
    beat_wave = (np.sin(2*np.pi*freq*t) * 32767).astype(np.int16)
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(beat_wave.tobytes())
    print(f"Generated simple beat: {filename}")

# Generate beat if not exists
beat_path = os.path.join(BEATS_DIR, "test_beat.wav")
if not os.path.exists(beat_path):
    generate_simple_beat(beat_path)

# -------- PHASE 1a FUNCTIONS --------
def clean_audio(input_file, output_file):
    cmd = ["ffmpeg", "-i", input_file, "-af", "afftdn", output_file]
    subprocess.run(cmd)

def trim_audio(input_file, output_file, start_sec=0, end_sec=None):
    cmd = ["ffmpeg", "-i", input_file]
    if end_sec:
        cmd += ["-ss", str(start_sec), "-to", str(end_sec)]
    else:
        cmd += ["-ss", str(start_sec)]
    cmd += [output_file]
    subprocess.run(cmd)

def export_mp3(input_file, beat_file, output_file, bitrate="192k"):
    # Merge with beat and export MP3
    cmd = [
        "ffmpeg",
        "-i", input_file,
        "-i", beat_file,
        "-filter_complex", "[0:a][1:a]amix=inputs=2:duration=first:dropout_transition=2",
        "-codec:a", "libmp3lame",
        "-b:a", bitrate,
        output_file
    ]
    subprocess.run(cmd)

# -------- MAIN WORKFLOW --------
def main():
    print("Dhugaa Music Studio - Phase 1a+1b Combined Workflow")
    files = os.listdir(AUDIO_DIR)
    for file in files:
        if file.endswith(".wav") or file.endswith(".mp3"):
            input_path = os.path.join(AUDIO_DIR, file)
            clean_path = os.path.join(CLEAN_DIR, f"clean_{file}")
            export_path = os.path.join(EXPORT_DIR, f"final_{file.split('.')[0]}.mp3")

            print(f"\nProcessing: {file}")
            clean_audio(input_path, clean_path)
            trim_audio(clean_path, clean_path, start_sec=5)
            export_mp3(clean_path, beat_path, export_path)
            print(f"Exported MP3 with beat: {export_path}")

if __name__ == "__main__":
    main()
