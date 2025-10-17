
# Torrent-API
A lightweight Rest API written in Django that fetches torrents data from Piratebay.

# Run locally:
1. Clone the repository:
```bash
git clone https://github.com/Charaf3334/Torrent-API.git
```
2. Navigate to the project directory:
```bash
cd Torrent-API
```
3. Create a virtual environment for Python and activate it:
```bash
python3 -m venv venv
```
- For Linux:
```bash
source venv/bin/activate
```
- For Windows:
```bash
.\venv\Scripts\Activate
```
4. Install dependencies:
```bash
pip install -r requirements.txt
```
5. Run migrations:
```bash
python3 manage.py migrate
```
6. Finally, run server:
```bash
./run.sh
```

# Usage:
To search for a specific keyword, include it as a query parameter in the API endpoint. For example:
```bash
curl -s http://localhost:8000/api/data/?key={KEYWORD} | jq
```
Example of output searching for ```interstellar```:
```json
[
    {
        "id": 1,
        "category": "Video > HD - Movies",
        "title": "Details for Interstellar (2014) (2014) 1080p BrRip x264 - YIFY",
        "link": "https://thepiratebay10.info/torrent/11756968/Interstellar_(2014)_(2014)_1080p_BrRip_x264_-_YIFY",
        "date": "03-15-2015",
        "size": "2.26 GiB",
        "seeders": "842",
        "leechers": "183",
        "uploader": "YIFY",
        "magnet": "magnet:?xt=urn:btih:89599BF4DC369A3A8ECA26411C5CCF922D78B486&dn=Interstellar+%282014%29+%282014%29+1080p+BrRip+x264+-+YIFY&tr=http%3A%2F%2Fp4p.arenabg.com%3A1337%2Fannounce&tr=udp%3A%2F%2F47.ip-51-68-199.eu%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2780%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2710%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2730%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2920%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.dler.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=udp%3A%2F%2Ftracker.pirateparty.gr%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce"
    },
    {
        "id": 2,
        "category": "Video > UHD/4k - Movies",
        "title": "Details for Interstellar.2014.PROPER.IMAX.1080p.UHD.BluRay.x265.HDR.DV.DD+5.1.Dual.YG⭐",
        "link": "https://thepiratebay10.info/torrent/71389010/Interstellar.2014.PROPER.IMAX.1080p.UHD.BluRay.x265.HDR.DV.DD_5.1.Dual_YG_",
        "date": "08-20-2023",
        "size": "4.21 GiB",
        "seeders": "293",
        "leechers": "72",
        "uploader": "yerisan710",
        "magnet": "magnet:?xt=urn:btih:13121036A0A971D7AE5601B9B95B5CC77D440B01&dn=Interstellar.2014.PROPER.IMAX.1080p.UHD.BluRay.x265.HDR.DV.DD%2B5.1.Dual.YG%E2%AD%90&tr=http%3A%2F%2Fp4p.arenabg.com%3A1337%2Fannounce&tr=udp%3A%2F%2F47.ip-51-68-199.eu%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2780%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2710%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2730%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2920%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.dler.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=udp%3A%2F%2Ftracker.pirateparty.gr%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce"
    }
    ...
]
```
# Note
This API can return up to 90 torrent results per keyword. It is intended for educational purposes only.
