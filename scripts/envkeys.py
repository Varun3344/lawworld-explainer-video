"""Read API keys from the two existing .env files (never printed)."""
import re, os
FLOW_ENV = "/Users/admin/Downloads/New short/Google Flow AI Video/.env"
BACKEND_ENV = "/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/.env"
def load(path):
    out = {}
    if not os.path.exists(path): return out
    for line in open(path, encoding="utf-8"):
        m = re.match(r'^\s*([A-Z0-9_]+)\s*=\s*(.*?)\s*$', line)
        if m:
            v = m.group(2)
            if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'": v = v[1:-1]
            out[m.group(1)] = v
    return out
_flow, _back = load(FLOW_ENV), load(BACKEND_ENV)
OPENAI_API_KEY = _flow.get("OPENAI_API_KEY") or _back.get("OPENAI_API_KEY")
ELEVENLABS_API_KEY = _back.get("ELEVENLABS_API_KEY") or _flow.get("ELEVENLABS_API_KEY")
ELEVENLABS_VOICE_ID = _back.get("ELEVENLABS_VOICE_ID") or _flow.get("ELEVENLABS_VOICE_ID")
VOICE_SETTINGS = {
    "stability": float(_back.get("ELEVENLABS_STABILITY", 0.5)),
    "similarity_boost": float(_back.get("ELEVENLABS_SIMILARITY", 0.9)),
    "style": float(_back.get("ELEVENLABS_STYLE", 0.1)),
    "use_speaker_boost": _back.get("ELEVENLABS_SPEAKER_BOOST", "true").lower() == "true",
}
