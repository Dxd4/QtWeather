import requests
from bs4 import BeautifulSoup


def get_weather(city):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
        session = requests.get(f"https://google.com/search?q=погода+{city}",headers=headers)
        if not(session.status_code == 200):
            return ["Can't reach the server","","","",""]
        
        soup = BeautifulSoup(session.text,"html.parser")
        spans = soup.find_all("span")
        imgs = soup.find_all("img")

        for x in range(len(spans)):
            if spans[x].get_text().find("°C")>-1:
                geoposition, temperature, time, weather = spans[x-4].get_text(), spans[x].get_text(), spans[x+3].get_text(), spans[x+5].get_text()
                break
            
        for x in imgs:
            if x["src"].find("gstatic")>-1:
                img_url = x["src"]
                break
        return (geoposition, temperature, time, weather, img_url)
    
    except:
        return ["Request error","","","",""]
