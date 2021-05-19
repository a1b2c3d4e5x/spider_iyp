
from fake_useragent import UserAgent
from typing import List, Dict
from bs4 import BeautifulSoup
import traceback
import requests
import time
import sys

class Spider_ipy(object):
    # 回傳公司名稱與網址陣列
    def spider_list(main_category: str, sub_category: str, area_id: int = 0):
        if False == isinstance(area_id, int):
            area_id = 0

        # https://www.iyp.com.tw/showroom.php?cate_name_eng_lv1=agriculture&cate_name_eng_lv3=agriculture-equip&a_id=7
        fixed_url: str = 'https://www.iyp.com.tw/showroom.php?cate_name_eng_lv1=' + main_category + '&cate_name_eng_lv3=' + sub_category + '&a_id=' + str(area_id)
        page: int = 0
        
        while True:
            try:
                # 組合出要爬得 url
                target_url = fixed_url + '&p=' + page
  
                # 假資料模擬瀏覽器
                headers = {'user-agent': UserAgent().random}

                # 取得網頁資料
                pageRequest = requests.get(target_url, headers = headers)
                pageRequest.encoding = pageRequest.apparent_encoding

            except:
                print('無法 request 網址: ' + target_url)
                print('Stack trace: ')
                traceback.print_exc()
                break;

            try:
                soup = BeautifulSoup(pageRequest.text, 'html.parser')
            except:
                print('無法轉成 html: ' + target_url)
                print('細節: \n\t' + str(pageRequest).replace('\n', '\n\t'), file = sys.stderr)
                traceback.print_exc()
                break;
 
            try:
                # 爬到文章 List 區塊
                list_block = soup.find(id = 'search-res')

                # VIP 店家, 優質店家,  一般店家
                for list_ol in list_block.find_all('ol', class_ = ['recommend', 'diamond', 'general'], recursive = False):
                    for list_li in list_ol.find_all('li', recursive = False):
                        item_a = list_li.select_one('h3 a')

                        # 統一網站的 url 格式
                        store_name = item_a.text
                        store_name_url = item_a['href']
                        if '//ww' == store_name_url[:4]:
                            store_name_url = 'https:' + store_name_url
                        elif 'www.' == store_name_url[:4]:
                            store_name_url = 'https://' + store_name_url
   
                        print(store_name, store_name_url, '\n===========================')

            except TypeError:
                print('Parsing url 失敗: ' + target_url)
                break

            if url:
                url=("https://abcde.com"+url)
                print(url)  
                b.append(url)

            time.sleep(5)

            #==================================

        
    
        


# https://www.iyp.com.tw/087333322
# https://www.iyp.com.tw/063361134