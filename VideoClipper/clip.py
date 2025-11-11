import sys
import subprocess

if len(sys.argv) != 5:
    print("Incorrect number of parameters")
    sys.exit(1)

def clip_video_ffmpeg(input_path, output_path, start, end, height=480):
    """
    Trim and resize a video clip using FFmpeg.

    Args:
        input_path (str): Path to the source video file.
        output_path (str): Path to save the clipped video.
        start (float | int): Start time in seconds.
        end (float | int): End time in seconds.
        height (int): Desired output height (width auto-calculated to preserve aspect ratio).
    """

    cmd = [
        "ffmpeg", "-y",                 # Overwrite output if it exists
        "-ss", str(start),              # Start time
        "-to", str(end),                # End time
        "-i", input_path,               # Input file
        "-vf", f"scale=-2:{height}:flags=spline",  # Smooth resize (auto width)
        "-c:v", "libx264",              # H.264 codec (broad compatibility)
        "-pix_fmt", "yuv420p",          # Standard pixel format for Windows/web
        "-preset", "medium",            # Balance between speed & quality
        "-movflags", "+faststart",      # Allow instant playback
        "-an",                          # No audio
        output_path                     # Output file
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print("FFmpeg failed:")
        # print(result.stderr)
        return 1
    print(f"Video saved to {output_path}")
    return 0

def clip_gif_ffmpeg(input_path, output_path, start, end, height=480, fps=15):
    """
    Trim, resize, and convert a video clip into an optimized GIF using FFmpeg.

    Args:
        input_path (str): Path to the source video file.
        output_path (str): Path to save the clipped GIF.
        start (float | int): Start time in seconds.
        end (float | int): End time in seconds.
        height (int): Desired GIF height (width auto-calculated).
        fps (int): Frames per second for the GIF.
    """
    # Use palette for better quality
    palette_path = "palette.png"

    # Generate palette for better GIF color quality)
    cmd_palette = [
        "ffmpeg", "-y",
        "-ss", str(start),
        "-to", str(end),
        "-i", input_path,
        "-vf", f"fps={fps},scale=-2:{height}:flags=lanczos,palettegen",
        palette_path
    ]
    result = subprocess.run(cmd_palette, capture_output=True, text=True)
    if result.returncode != 0:
        print("Failed to generate palette:")
        print(result.stderr)
        return 1

    # Create GIF using palette
    cmd_gif = [
        "ffmpeg", "-y",
        "-ss", str(start),
        "-to", str(end),
        "-i", input_path,
        "-i", palette_path,
        "-filter_complex", f"fps={fps},scale=-2:{height}:flags=lanczos[x];[x][1:v]paletteuse",
        output_path
    ]
    result = subprocess.run(cmd_gif, capture_output=True, text=True)
    if result.returncode != 0:
        print("Failed to create GIF:")
        print(result.stderr)
        return 1

    print(f"GIF saved to {output_path}")
    return 0

sys.exit(clip_gif_ffmpeg(*sys.argv[1:], height=480))