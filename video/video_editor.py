# video_editor.py
# Phase 1d: Simple video editor for Dhugaa Music Studio
import os
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip, ColorClip

VIDEO_DIR = "video"
os.makedirs(VIDEO_DIR, exist_ok=True)

# -------- CONFIGURATION --------
AUDIO_FILE = "audio/export/final_my_song.mp3"  # Phase 1a+1b final MP3
OUTPUT_VIDEO = os.path.join(VIDEO_DIR, "final_video.mp4")
DURATION = 10  # seconds
BG_COLOR = (50, 50, 50)  # dark grey background

# -------- VIDEO CREATION --------
def create_simple_video(audio_file, output_file, duration=DURATION):
    # Create solid background
    bg_clip = ColorClip(size=(1280, 720), color=BG_COLOR, duration=duration)
    
    # Add text overlay
    txt_clip = TextClip("Dhugaa Music Studio", fontsize=70, color='white')
    txt_clip = txt_clip.set_pos('center').set_duration(duration)
    
    # Add audio
    audio_clip = AudioFileClip(audio_file)
    video = CompositeVideoClip([bg_clip, txt_clip])
    video = video.set_audio(audio_clip).set_duration(audio_clip.duration)
    
    # Export final video
    video.write_videofile(output_file, fps=24)
    print(f"Video exported: {output_file}")

# -------- MAIN --------
if __name__ == "__main__":
    create_simple_video(AUDIO_FILE, OUTPUT_VIDEO)
