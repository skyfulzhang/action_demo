import requests
import re
from set_log import logger
from send_email import send_email
from datetime import datetime

"""
热搜
"""

session = requests.session()

def get_hot_search():

    try:
        logger.info('获取热搜 - Start')
        headers = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

        }
        pattern = 'query":"(.*?)","rawUrl'
        res = session.request(method = 'GET', url = 'https://top.baidu.com/board?tab=realtime', headers = headers)
        news = []
        if len(res.text) > 500 :
            matchs = re.findall(pattern, res.text)
            for match in matchs :
                news.append(match)
        else :
            news.append("error")
        now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        email_content = '\n\n'.join(news)
        send_email(email_name = f'{now_time}热搜', email_content = email_content)
        print(news)
    except Exception as e :
        logger.error('获取热搜 - Failed')
        logger.error(f"{e}")
    finally:
        logger.info('获取热搜 - End')

        
if __name__ == '__main__':
    get_hot_search()
