import requests

def download(url):
    try:
        session = requests.get(url)
        if session.status_code == 200:
            with open("out.png","wb") as image:
                image.write(session.content)
            return True
        return False
    except:
        return False
