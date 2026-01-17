# studio_phase1a.py
# Simple audio workflow for Dhugaa Music Studio
# Record (external), clean, trim, export MP3

import os
import subprocess

# -------- CONFIGURATION --------
AUDIO_DIR = "audio/record"
CLEAN_DIR = "audio/clean"
EXPORT_DIR = "audio/export"

# Ensure folders exist
for folder in [AUDIO_DIR, CLEAN_DIR, EXPORT_DIR]:
    os.makedirs(folder, exist_ok=True)

# -------- FUNCTIONS --------
def clean_audio(input_file, output_file):
    """
    Basic noise reduction using FFmpeg's afftdn filter
    """
    cmd = [
        "ffmpeg",
        "-i", input_file,
        "-af", "afftdn",
        output_file
    ]
    subprocess.run(cmd)

def trim_audio(input_file, output_file, start_sec=0, end_sec=None):
    """
    Trim audio from start_sec to end_sec
    """
    cmd = ["ffmpeg", "-i", input_file]
    if end_sec:
        cmd += ["-ss", str(start_sec), "-to", str(end_sec)]
    else:
        cmd += ["-ss", str(start_sec)]
    cmd += [output_file]
    subprocess.run(cmd)

def export_mp3(input_file, output_file, bitrate="192k"):
    """
    Export cleaned audio to MP3
    """
    cmd = [
        "ffmpeg",
        "-i", input_file,
        "-codec:a", "libmp3lame",
        "-b:a", bitrate,
        output_file
    ]
    subprocess.run(cmd)

# -------- MAIN WORKFLOW --------
def main():
    print("Dhugaa Music Studio - Phase 1a Workflow")
    files = os.listdir(AUDIO_DIR)
    for file in files:
        if file.endswith(".wav") or file.endswith(".mp3"):
            input_path = os.path.join(AUDIO_DIR, file)
            clean_path = os.path.join(CLEAN_DIR, f"clean_{file}")
            export_path = os.path.join(EXPORT_DIR, f"final_{file.split('.')[0]}.mp3")

            print(f"\nProcessing: {file}")
            clean_audio(input_path, clean_path)
            # Example trim: first 5 seconds removed
            trim_audio(clean_path, clean_path, start_sec=5)
            export_mp3(clean_path, export_path)
            print(f"Exported MP3: {export_path}")

if __name__ == "__main__":
    main()
