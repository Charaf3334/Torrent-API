from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup

def getTorrentData(request):
    
    def parseKeyword(keyword):
        formatted = keyword.replace(" ", "%20")
        return formatted

    keyword = request.GET.get('key', '').strip()    
    if not keyword:
        return JsonResponse([], safe=False)
    formatted_keyword = parseKeyword(keyword)
    results = []
    id_counter = 1

    for page in range(1, 4):
        URL = f'https://thepiratebay10.info/search/{formatted_keyword}/{page}/99/0'
        response = requests.get(URL)

        if response.status_code != 200:
            return JsonResponse({"error": f"Failed to fetch URL: {response.status_code}"}, status=500)
        soup = BeautifulSoup(response.text, 'html.parser')
        rows = soup.find_all('tr')
        
        for row in rows:
            cols = row.find_all('td')
            if len(cols) < 8:
                continue

            category = cols[0].find('a').text if cols[0].find('a') else ""
            title = cols[1].find('a')['title'] if cols[1].find('a') else ""
            link = cols[1].find('a')['href'] if cols[1].find('a') else ""
            date = cols[2].get_text(strip=True)
            size = cols[4].get_text(strip=True)
            seeders = cols[5].get_text(strip=True)
            leechers = cols[6].get_text(strip=True)
            uploader = cols[7].get_text(strip=True)
            magnet = cols[3].find('a')['href'] if cols[3].find('a') else ""

            results.append({
                "id": id_counter,
                "category": category.replace("\u00a0", " ").strip(),
                "title": title.replace("\u00a0", " ").strip(),
                "link": link.replace("\u00a0", " ").strip(),
                "date": date.replace("\u00a0", " ").strip().replace(" ", "-"),
                "size": size.replace("\u00a0", " ").strip(),
                "seeders": seeders.replace("\u00a0", " ").strip(),
                "leechers": leechers.replace("\u00a0", " ").strip(),
                "uploader": uploader.replace("\u00a0", " ").strip(),
                "magnet": magnet.replace("\u00a0", " ").strip(),
            })
            id_counter += 1

    return JsonResponse(results, safe=False)