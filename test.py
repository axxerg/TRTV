streams = [
    {"name": "SHOW TURK", "url": "https://www.youtube.com/watch?v=XnvS-RZa4Qw"},
    {"name": "STAR", "url": "https://www.youtube.com/watch?v=82O6yOy_XwE&vq=1080"},
    {"name": "EURO D", "url": "https://www.youtube.com/watch?v=6wHAK439FDI"},
    {"name": "A2", "url": "https://www.youtube.com/watch?v=HtnytvwXi5o"},
    {"name": "a HABER", "url": "https://www.youtube.com/watch?v=nmY9i63t6qo"},
    {"name": "a SPOR", "url": "https://www.youtube.com/watch?v=7uBpwcn2ZZ0&vq=1080"},
    {"name": "beIN SPORTS HABER", "url": "https://www.youtube.com/watch?v=VCl1wO81VdM"},
    {"name": "HT SPOR", "url": "https://www.youtube.com/watch?v=RdpqsTbi_KU"},
    {"name": "KRAL POP", "url": "https://www.youtube.com/watch?v=GuFTuKoXepw"},
    {"name": "CNBC-E", "url": "https://www.youtube.com/watch?v=XihyuKSyUD0"},
    {"name": "CNN TÜRK", "url": "https://www.youtube.com/watch?v=VXMR3YQ7W3s"},
    {"name": "NTV", "url": "https://www.youtube.com/watch?v=qnpfhjMhMKY"},
    {"name": "HABER GLOBAL", "url": "https://www.youtube.com/watch?v=6BX-NUzBSp8"},
    {"name": "HABER TURK", "url": "https://www.youtube.com/watch?v=RNVNlJSUFoE&vq=1080"},
    {"name": "tv100", "url": "https://www.youtube.com/watch?v=6g_DvD8e2T0"},
    {"name": "24", "url": "https://www.youtube.com/watch?v=jDEuHBhjfmg"},
    {"name": "TVNET", "url": "https://www.youtube.com/watch?v=KdhO7SV9tF8"},
    {"name": "HALK TV", "url": "https://www.youtube.com/watch?v=ZSWPj9szKb8"},
    {"name": "TELE 1", "url": "https://www.youtube.com/watch?v=fNqmmqNNGp8"},
    {"name": "SÖZCÜ TV", "url": "https://www.youtube.com/watch?v=ztmY_cCtUl0"}
]

def write_m3u8(streams, filename="streams.m3u8"):
    print("Anzahl Streams:", len(streams))  # Debug-Ausgabe
    with open(filename, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for stream in streams:
            f.write(f"#EXTINF:-1,{stream['name']}\n")
            f.write(f"{stream['url']}\n")

if __name__ == "__main__":
    write_m3u8(streams)
    print("streams.m3u8 wurde erstellt.")
