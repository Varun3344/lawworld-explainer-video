"""Open a finished video on a still card so frame 0 (the thumbnail most apps show) is that card.

Usage: python3 open_on_card.py <video.mp4> <card.png> <out.mp4> [hold_frames=27] [fade_frames=9]

The card holds for `hold_frames` with a 1.5 % slow push-in, then crossfades into the untouched video.
Picture and sound of the video both shift by hold_frames / fps, so lip-sync is unchanged; the card is silent.
No cover-art track is added (WhatsApp mishandles it).
"""
import os
import subprocess
import sys
import tempfile

from PIL import Image

FPS = 24
ZOOM = 0.015


def card_frames(card, n, out_dir, centre_y=0.47):
    im = Image.open(card).convert("RGB")
    w, h = im.size
    cx, cy = w / 2, h * centre_y
    for i in range(n):
        s = 1 + ZOOM * i / (n - 1)
        # inverse affine: output (x, y) samples input ((x - cx) / s + cx, (y - cy) / s + cy); sub-pixel, no jitter
        a = 1 / s
        f = im.transform((w, h), Image.AFFINE, (a, 0, cx - a * cx, 0, a, cy - a * cy), resample=Image.BICUBIC)
        f.save(f"{out_dir}/{i:03d}.png")


def main():
    video, card, out = sys.argv[1:4]
    hold = int(sys.argv[4]) if len(sys.argv) > 4 else 27
    fade = int(sys.argv[5]) if len(sys.argv) > 5 else 9
    offset, dur = hold / FPS, fade / FPS
    with tempfile.TemporaryDirectory() as tmp:
        card_frames(card, hold + fade, tmp)
        graph = (
            f"[0:v]fps={FPS},format=yuv420p,setsar=1,settb=AVTB[c];"
            f"[1:v]fps={FPS},format=yuv420p,setsar=1,settb=AVTB[v];"
            f"[c][v]xfade=transition=fade:duration={dur}:offset={offset},format=yuv420p[vo];"
            f"[1:a]adelay={round(offset * 1000)}:all=1[ao]"
        )
        cmd = [
            "ffmpeg", "-v", "error", "-y",
            "-framerate", str(FPS), "-i", f"{tmp}/%03d.png",
            "-i", video,
            "-filter_complex", graph, "-map", "[vo]", "-map", "[ao]",
            "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-profile:v", "high", "-pix_fmt", "yuv420p", "-r", str(FPS),
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
            "-movflags", "+faststart", out,
        ]
        subprocess.run(cmd, check=True)
    print(out, f"card {offset:.3f} s, crossfade {dur:.3f} s")


if __name__ == "__main__":
    main()
