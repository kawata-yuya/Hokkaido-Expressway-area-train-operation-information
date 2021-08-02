import requests
import bs4

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) '\
    'AppleWebKit/537.36 (KHTML, like Gecko) '\
        'Chrome/55.0.2883.95 Safari/537.36 '
url = "https://www3.jrhokkaido.co.jp/webunkou/?a=2"
# url = "https://web.archive.org/web/20201218070004/https://www3.jrhokkaido.co.jp/webunkou/?a=2"



def status_getter():
    r = requests.get(url, headers={'User-Agent': UA})
    r.encoding = r.apparent_encoding


    soup = bs4.BeautifulSoup(r.text, features="html.parser")

    for br in soup.find_all("br"):
        br.replace_with("\n")

    data = soup.find('div', class_="mainbodyInner").text

    if data.replace('\n', '') == "※観光列車の運転見合わせに関する詳細については、こちらをご確認ください。※土休日の運休及び特急列車の曜日運休追加に関する詳細については、こちらをご確認ください。 ":
        return None
    
    else:
        text = data.replace('\n\n\n', '\n\n')[86:]
        if len(text) > 0:
            return text + url
        else:
            return 'Error'


if __name__ == '__main__':
    print(status_getter())