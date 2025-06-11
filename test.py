import subprocess

streams = [
    {"name": "SHOW TURK", "url": "https://www.youtube.com/watch?v=XnvS-RZa4Qw"},
    {"name": "STAR", "url": "https://www.youtube.com/watch?v=82O6yOy_XwE&vq=1080"},
    # ... weitere Streams ...
]

def get_direct_url(youtube_url):
    try:
        # yt-dlp -g gibt die Direkt-URL aus (meist Video und Audio getrennt, wir nehmen die erste)
        result = subprocess.run(
            ["yt-dlp", "-g", youtube_url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=20
        )
        if result.returncode == 0:
            return result.stdout.strip().split('\n')[0]
        else:
            print(f"Fehler bei {youtube_url}: {result.stderr}")
            return "KEIN DIREKTLINK GEFUNDEN"
    except Exception as e:
        print(f"Exception bei {youtube_url}: {e}")
        return "KEIN DIREKTLINK GEFUNDEN"

with open("streams.txt", "w", encoding="utf-8") as f:
    for stream in streams:
        f.write(f"{stream['name']} {stream['url']}\n")
        direct_url = get_direct_url(stream["url"])
        f.write(f"{direct_url}\n")
