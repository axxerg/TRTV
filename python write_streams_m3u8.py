streams = [
    {"name": "TEST", "url": "http://example.com/stream.m3u8"}
]

def write_m3u8(streams, filename="streams.m3u8"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for stream in streams:
            f.write(f"#EXTINF:-1,{stream['name']}\n")
            f.write(f"{stream['url']}\n")

if __name__ == "__main__":
    write_m3u8(streams)
    print("streams.m3u8 wurde erstellt.")
