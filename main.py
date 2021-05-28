
import sys 
from const.color import color
from const.meta import meta
from const.area_ids import area
from const.categories import categories
from core.spider_iyp import Spider_ipy
from utils.convert import csv_to_xlsx

class ArgvParser:
   def __print_color_title(self, text: str):
      print(color.BOLD + color.BLUE + text + color.END)

   def __print_color_description(self, preText: str, postText: str):
      print('  ' + color.BOLD + color.DARKCYAN + '--' + preText + ':' + color.END, postText)

   # 使用主要爬蟲功能
   def spider(self, main_category: str, sub_category: str, area_id: int = 0):
      Spider_ipy.spider_list(main_category, sub_category, area_id)

   def spider_all(self, main_category: str):
      result = categories.sub_categories(main_category)
      if None != result:
         for mid_category in result:
            for key, value in mid_category['sub'].items():
               Spider_ipy.spider_list(main_category, key)
      else:
         self.__print_color_title('Not Found.')

   # 列出主類別列表
   def categories(self):
      for part in categories.categories:
         self.__print_color_title('\n' + part['name'])
         for key, value in part['sub'].items():
            print('  ' + value + ': ' + key)

   # 列出主類別中的子類別列表
   def subcategories(self, main_category: str):
      result = categories.sub_categories(main_category)
      if None != result:
         for midCategory in result:
            self.__print_color_title('\n' + midCategory['name'])
            for key, value in midCategory['sub'].items():
               print('  ' + value + ': ' + key)
      else:
         self.__print_color_title('Not Found.')

   # 列出地區編號資訊
   def area(self):
      for key, values in area.all.items():
         self.__print_color_title('\n' + key)
         for k, v in values.items():
            print('  ' + v + ':', k)
         #print('\n')

   # 關於此程式的說明
   def about(self):
      print('此爬蟲提供爬取公司黃頁相關資料')
      print('網頁名稱: 中華黃頁網路電話簿')
      print('網頁網址: https://www.iyp.com.tw')

   # 關於此程式的開發資訊
   def info(self):
      print('Build Date     :', meta.BUILD_DATE)
      print('Build Version  :', 'v' + meta.BUILD_VERSION)
      print('Developer Name :', meta.DEVERPER_NAME)
      print('Developer Email:', meta.DEVERPER_EMAIL)

   # 把產出的 csv 轉成 excel
   def to_excel(self):
      csv_to_xlsx()

   # 未給任何參數
   def none(self):
      self.__print_color_title('指令說明')
      self.__print_color_description(self.spider.__name__ + ' [*主類別] [*子類別] [地區編號]', '爬取公司黃頁資料')
      self.__print_color_description(self.spider.__name__ + ' [*主類別]', '爬取公司黃頁主類別下所有的子類別資料')
      self.__print_color_description(self.categories.__name__, '列出主類別列表')
      self.__print_color_description(self.subcategories.__name__ + ' [*主類別]', '列出主類別中的子類別列表')
      self.__print_color_description(self.area.__name__, '列出地區編號資訊')
      self.__print_color_description(self.about.__name__, '關於此程式的說明')
      self.__print_color_description(self.info.__name__, '關於此程式的開發資訊')
      self.__print_color_description(self.to_excel.__name__, '把產出的 csv 檔轉存成 excel')

# 判斷輸入的參數指令
def __argv_is_cmd(fn_name: str) -> bool:
   if 2 <= len(sys.argv):
      return ('--' + fn_name) == sys.argv[1]
   return True

# 處理 argv 的參數
def __parse_argv():
   parser = ArgvParser()

   if 2 == len(sys.argv):
      if __argv_is_cmd(parser.categories.__name__):
         return parser.categories()
      elif __argv_is_cmd(parser.area.__name__):
         return parser.area()
      elif __argv_is_cmd(parser.about.__name__):
         return parser.about()
      elif __argv_is_cmd(parser.info.__name__):
         return parser.info()
      elif __argv_is_cmd(parser.to_excel.__name__):
         return parser.to_excel()

   elif 3 == len(sys.argv):
      if __argv_is_cmd(parser.subcategories.__name__):
         return parser.subcategories(sys.argv[2])
      elif __argv_is_cmd(parser.spider.__name__):
         return parser.spider_all(sys.argv[2])

   elif 4 <= len(sys.argv):
      if __argv_is_cmd(parser.spider.__name__):
         if 5 == len(sys.argv):
            return parser.spider(sys.argv[2], sys.argv[3], sys.argv[4])
         else:
            return parser.spider(sys.argv[2], sys.argv[3])

   return parser.none()

# 主程式進入口
if __name__ == '__main__':
   __parse_argv()


# 有 Email 的
# https://www.iyp.com.tw/035182788



