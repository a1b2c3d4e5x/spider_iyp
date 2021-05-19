from typing import Dict
from ..base_category import BaseCategory

# 報紙 newspaper
class Newspaper(object):
   def newspaper() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '報紙'
      list['id'] = 'newspaper'

      newspaper = {}
      newspaper['distribution-service'] = '派報服務'
      newspaper['publishers'] = '報社'

      list['sub'] = newspaper
      return list

# 電視 television
class Television(object):
   def television() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '電視'
      list['id'] = 'television'

      television = {}
      television['TV-station'] = '電視台'
      television['recording-equip'] = '電視攝影器材'
      television['program-production-service'] = '電視節目製作'

      list['sub'] = television
      return list

# 廣播 broadcast
class Broadcast(object):
   def broadcast() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '廣播'
      list['id'] = 'broadcast'

      broadcast = {}
      broadcast['radio-stations'] = '廣播電台'
      broadcast['production-service'] = '廣播節目製作'

      list['sub'] = broadcast
      return list

# 傳播業 communication-industry
class CommunicationIndustry(object):
   def communication_industry() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '傳播業'
      list['id'] = 'communication-industry'

      communication_industry = {}
      communication_industry['communication'] = '傳播公司'

      list['sub'] = communication_industry
      return list

# 圖書出版 publication
class Publication(object):
   def publication() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '圖書出版'
      list['id'] = 'publication'

      publication = {}
      publication['book-stores'] = '書店'
      publication['book-rentals'] = '租書店'
      publication['secondhand-books'] = '二手書'
      publication['publication'] = '出版社'

      list['sub'] = publication
      return list

# 教育器材 education-supplies
class EducationSupplies(object):
   def education_supplies() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '教育器材'
      list['id'] = 'education-supplies'

      education_supplies = {}
      education_supplies['teaching-aids'] = '教具'

      list['sub'] = education_supplies
      return list

# 新聞文化 news-and-culture
class NewsAndCulture(BaseCategory, Newspaper, Television, Broadcast, CommunicationIndustry, Publication, 
EducationSupplies):
   category_name = '新聞文化'
   category_id = 'news-and-culture'