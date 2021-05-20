
from fake_useragent import UserAgent
from typing import List, Dict
from bs4 import BeautifulSoup
import traceback
import requests
import random
import time
import sys

class Spider_ipy(object):
    def spider_content_email(url: str) -> str:
        try:
            # 組合出要爬得 url
            iyp_id = url.rsplit('/', 1)[-1]
            fixed_content_url = 'https://www.iyp.com.tw/' + iyp_id

            # 假資料模擬瀏覽器
            headers = {'user-agent': UserAgent().random}

            # 取得網頁資料
            pageRequest = requests.get(fixed_content_url, headers = headers)
            pageRequest.encoding = pageRequest.apparent_encoding

        except:
            print('無法 request 網址: ' + fixed_content_url)
            traceback.print_exc()
            return

        try:
            soup = BeautifulSoup(pageRequest.text, 'html.parser')
        except:
            print('無法轉成 html: ' + fixed_content_url)
            print('細節: \n\t' + str(pageRequest).replace('\n', '\n\t'), file = sys.stderr)
            traceback.print_exc()
            return

        try:
            # 爬到文章 Email 區塊
            email_block = soup.find('li', class_ = 'email')

            if None == email_block:
                return
            email = email_block.select_one('div a')

        except TypeError:
            print('Parsing content url 失敗: ' + fixed_content_url)
            return

        return email.text

    def spider_list(main_category: str, sub_category: str, area_id: int = 0):
        if False == isinstance(area_id, int):
            area_id = 0

        #fixed_url: str = 'https://www.iyp.com.tw/showroom.php?cate_name_eng_lv1=agriculture&cate_name_eng_lv3=agriculture-equip&a_id=4'
        fixed_url: str = 'https://www.iyp.com.tw/showroom.php?cate_name_eng_lv1=' + main_category + '&cate_name_eng_lv3=' + sub_category + '&a_id=' + str(area_id)
        page: int = 0
        
        while True:
            try:
                # 組合出要爬得 url
                target_url = fixed_url + '&p=' + str(page)
  
                # 假資料模擬瀏覽器
                headers = {'user-agent': UserAgent().random}

                # 取得網頁資料
                pageRequest = requests.get(target_url, headers = headers)
                pageRequest.encoding = pageRequest.apparent_encoding

            except:
                print('無法 request 網址: ' + target_url)
                traceback.print_exc()
                break;

            try:
                soup = BeautifulSoup(pageRequest.text, 'html.parser')
            except:
                print('無法轉成 html: ' + target_url)
                print('細節: \n\t' + str(pageRequest).replace('\n', '\n\t'), file = sys.stderr)
                traceback.print_exc()
                break;
 
            store_data_array = []
            try:
                # 爬到文章 List 區塊
                res_block_list = soup.find(id = 'search-res')

                # VIP 店家, 優質店家,  一般店家
                store_block_list = res_block_list.find_all('ol', class_ = ['recommend', 'diamond', 'general'], recursive = False)
                if 0 == len(store_block_list):
                    break

                for list_ol in store_block_list:
                    store_list = list_ol.find_all('li', recursive = False)
                    if 0 == len(store_list):
                        break

                    for list_li in store_list:
                        item_a = list_li.select_one('h3 a')

                        # 統一網站的 url 格式
                        store_name = item_a.text
                        store_name_url = item_a['href']
                        if '//ww' == store_name_url[:4]:
                            store_name_url = 'https:' + store_name_url
                        elif 'www.' == store_name_url[:4]:
                            store_name_url = 'https://' + store_name_url
   
                        store_data_array.append({'name': store_name, 'url': store_name_url})

            except TypeError:
                print('Parsing list url 失敗: ' + target_url)
                traceback.print_exc()
                break

            if 0 == len(store_data_array):
                print('找不到任何資料: ' + target_url)
                break
            
            # 爬店家 ipy 內容頁，取回有 Email 的資訊
            for data in store_data_array:
                if 'https://www.iyp.com.tw/' in data['url']:
                    print('[FETCH] ' + data['name'], data['url'])

                    time.sleep((random.random() + 0.5) * 2)
                    store_email = Spider_ipy.spider_content_email(data['url'])
                    if None != store_email:
                        print('\033[36m[EMAIL] ' + store_email, '\033[0m')
                else:
                    print(' [SKIP] ' + data['name'], data['url'])

            page += 1
            time.sleep(5)

        print('Spider End')
        


# https://www.iyp.com.tw/087333322
# https://www.iyp.com.tw/063361134