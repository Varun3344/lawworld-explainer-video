"""Pass a Flow presenter clip's speech through ElevenLabs speech-to-speech into the Ravi voice.
Timing is preserved by the model, so lip-sync stays intact. Output: <clip>.ravi.mp4 (video copied, audio replaced).
Usage: python3 voice_sts.py <clip.mp4> [...]"""
import sys, os, json, subprocess, tempfile
sys.path.insert(0, os.path.dirname(__file__))
from envkeys import ELEVENLABS_API_KEY, ELEVENLABS_VOICE_ID, VOICE_SETTINGS
API = "https://api.elevenlabs.io/v1"
STS_MODEL = "eleven_multilingual_sts_v2"

def run(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)

def convert(clip):
    out = clip[:-4] + ".ravi.mp4"
    if os.path.exists(out) and os.path.getsize(out) > 10_000:
        print(f"[sts] {os.path.basename(out)} exists, skipped"); return out
    tmp = tempfile.mkdtemp()
    wav = os.path.join(tmp, "in.wav"); mp3 = os.path.join(tmp, "out.mp3")
    run(["ffmpeg", "-v", "error", "-y", "-i", clip, "-vn", "-ac", "1", "-ar", "44100", wav])
    url = f"{API}/speech-to-speech/{ELEVENLABS_VOICE_ID}?output_format=mp3_44100_128"
    r = subprocess.run(["curl", "-s", "-m", "300", "-o", mp3, "-w", "%{http_code}", "-X", "POST", url,
                        "-H", f"xi-api-key: {ELEVENLABS_API_KEY}",
                        "-F", f"audio=@{wav}", "-F", f"model_id={STS_MODEL}",
                        "-F", "remove_background_noise=false",
                        "-F", f"voice_settings={json.dumps(VOICE_SETTINGS)}"], capture_output=True, text=True)
    code = r.stdout.strip()
    if code != "200":
        body = open(mp3, "rb").read(600) if os.path.exists(mp3) else b""
        raise SystemExit(f"[sts] HTTP {code} for {clip}: {body!r}")
    # remux: keep the video stream untouched, swap in the converted voice, keep original length
    run(["ffmpeg", "-v", "error", "-y", "-i", clip, "-i", mp3, "-map", "0:v:0", "-map", "1:a:0",
         "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", out])
    d0 = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", clip]).stdout.strip())
    d1 = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", out]).stdout.strip())
    print(f"[sts] {os.path.basename(clip)} -> {os.path.basename(out)}  {d0:.2f}s -> {d1:.2f}s")
    return out

if __name__ == "__main__":
    for c in sys.argv[1:]: convert(c)
