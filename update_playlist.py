import urllib.request

SOURCE_URL = "https://tinyurl.com/ByteFixRepairs2026"

# NHK World Channel Entry
NHK_ENTRY = """
#EXTINF:-1 tvg-id="NHKWorldJapan.jp@HD",NHK World-Japan HD (1080p) [Geo-blocked]
https://nhk.lls.pbs.org/index.m3u8
"""

try:
    # Fetch original playlist
    req = urllib.request.Request(SOURCE_URL, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
    
    # Append NHK World at the end
    merged_content = content.strip() + "\n" + NHK_ENTRY.strip()
    
    # Save combined playlist
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write(merged_content)
    print("Playlist updated successfully!")

except Exception as e:
    print(f"Error fetching playlist: {e}")
