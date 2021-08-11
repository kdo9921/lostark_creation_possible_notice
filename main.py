import telegram
import requests
from bs4 import BeautifulSoup

url = 'https://lostark.game.onstove.com/News/Notice/List'
response = requests.get(url)

YOUR_BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
YOUR_CHAT_ID = YOUR_CHAT_ID_HERE

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    list = soup.select_one('div.list')
    notices = list.select('a')

    for notice in notices:
        title = notice.find("span",{"class":"list__title"}).get_text()
        date = notice.find("div",{"class":"list__date"}).get_text()
        if title.find("생성 가능 수치") != -1:
            if date.find("분") == -1 and date.find("1시간") == -1 and date.find("2시간") == -1:
                continue
            else:
                bot = telegram.Bot(token=YOUR_BOT_TOKEN)
                chat_id = YOUR_CHAT_ID
                msg = date + " 캐릭터 생성 가능 수치 관련 공지가 올라온 것을 감지했습니다"
                bot.sendMessage(chat_id=chat_id, text=msg)

else : 
    print(response.status_code)