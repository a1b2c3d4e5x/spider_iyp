
import sys 
from enum import Enum
from const.color import color
from const.meta import meta

class ArgvParser:
	def __print_color_title(self, text: str):
		print(color.BOLD + color.BLUE + text + color.END)

	def __print_color_description(self, preText: str, postText: str):
		print(color.BOLD + color.DARKCYAN + '--' + preText + ':' + color.END, postText)

	# 使用主要爬蟲功能
	def spider(self, main_category: str, sub_category: str, area_id: int = 0):
		print('spider', main_category, sub_category, area_id)

	# 列出主類別列表
	def list(self):
		print('list')

	# 列出主類別中的子類別列表
	def sublist(self, main_category: str):
		print('sublist', main_category)

	# 列出地區編號資訊
	def area(self):
		print('area')

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

	# 未給任何參數
	def none(self):
		self.__print_color_title('指令說明')

		self.__print_color_description(self.spider.__name__ + ' [*主類別] [*子類別] [地區編號]', '爬取公司黃頁資料')
		self.__print_color_description(self.list.__name__, '列出主類別列表')
		self.__print_color_description(self.sublist.__name__ + ' [*主類別]', '列出主類別中的子類別列表')
		self.__print_color_description(self.area.__name__, '列出地區編號資訊')
		self.__print_color_description(self.about.__name__, '關於此程式的說明')
		self.__print_color_description(self.info.__name__, '關於此程式的開發資訊')

# 判斷輸入的參數指令
def __argv_is_cmd(fn_name: str) -> bool:
	if 2 <= len(sys.argv):
		return ('--' + fn_name) == sys.argv[1]
	return True

# 處理 argv 的參數
def __parse_argv():
	parser = ArgvParser()

	if 2 == len(sys.argv):
		if __argv_is_cmd(parser.list.__name__):
			return parser.list()
		elif __argv_is_cmd(parser.area.__name__):
			return parser.area()
		elif __argv_is_cmd(parser.about.__name__):
			return parser.about()
		elif __argv_is_cmd(parser.info.__name__):
			return parser.info()

	elif 3 == len(sys.argv):
		if __argv_is_cmd(parser.sublist.__name__):
			return parser.sublist(sys.argv[2])

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






