"""room_check.py <clip> [ref] -> prints the wall difference vs the reference clip (q01); exit 1 when the room differs."""
import sys, subprocess, numpy as np
def sig(clip, t=4.0):
    raw = subprocess.run(["ffmpeg","-v","error","-ss",str(t),"-i",clip,"-frames:v","1","-vf","crop=iw:ih*0.28:0:0,scale=32:16","-f","rawvideo","-pix_fmt","rgb24","-"],capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.uint8).astype(np.float32).reshape(16, 32, 3)
ref = sys.argv[2] if len(sys.argv) > 2 else "/Users/admin/Downloads/New short/product-explainer/downloads/office_kn/q01.mp4"
d = float(np.abs(sig(sys.argv[1]) - sig(ref)).mean()); print(f"{d:.1f}"); sys.exit(1 if d > 18 else 0)
