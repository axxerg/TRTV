import subprocess

streams = [
    {"name": "SHOW TURK", "url": "https://www.youtube.com/watch?v=XnvS-RZa4Qw"},
    {"name": "STAR", "url": "https://www.youtube.com/watch?v=82O6yOy_XwE&vq=1080"},
    # ... Rest wie gehabt ...
]

def get_direct_url(youtube_url):
    try:
        # yt-dlp -g gibt Direktstream-URL zurück
        result = subprocess.run(
            ["yt-dlp", "-g", youtube_url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=20
        )
        # Im Erfolgsfall: Video-URL (und evtl. Audio-URL) in den Zeilen
        return result.stdout.strip().split('\n')[0]
    except Exception as e:
        print(f"Fehler: {e}")
        return "KEIN DIREKTLINK GEFUNDEN"

def write_streams(streams, filename="streams.m3u8"):
    with open(filename, "w", encoding="utf-8") as f:
        for stream in streams:
            f.write(f"{stream['name']} {stream['url']}\n")
            direct_url = get_direct_url(stream["url"])
            f.write(f"{direct_url}\n")

if __name__ == "__main__":
    write_streams(streams)
    print("streams.m3u8 wurde erstellt.")
