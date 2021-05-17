
import sys 
from enum import Enum
from const.color import color
from const.meta import meta

class ArgvEnum:
	def __print_color_title(text: str):
		print(color.BOLD + color.BLUE + text + color.END)

	def __print_color_description():
		print('')

	# 使用主要爬蟲功能
	def spider(main_category: str, sub_category: str, area_id: int = 0):
		print('spider', main_category, sub_category, area_id)

	# 列出主類別列表
	def list():
		print('list')

	# 列出主類別中的子類別列表
	def sublist(main_category: str):
		print('sublist', main_category)

	# 列出地區編號資訊
	def area():
		print('area')

	# 關於此程式的說明
	def about():
		print('此爬蟲提供爬取公司黃頁相關資料')
		print('網頁名稱: 中華黃頁網路電話簿')
		print('網頁網址: https://www.iyp.com.tw')

	# 關於此程式的開發資訊
	def info():
		print('Build Date     :', meta.BUILD_DATE)
		print('Build Version  :', 'v' + meta.BUILD_VERSION)
		print('Developer Name :', meta.DEVERPER_NAME)
		print('Developer Email:', meta.DEVERPER_EMAIL)

	# 未給任何參數
	def none(self):
		print(self)
		self.__print_color_title('指令說明')
		print(color.BOLD + color.BLUE + '指令說明:' + color.END)
		print(color.BOLD + color.DARKCYAN + '--' + ArgvEnum.spider.__name__ + ' [*主類別] [*子類別] [地區編號]:' + color.END, '爬取公司黃頁資料')
		print(color.BOLD + color.DARKCYAN + '--' + ArgvEnum.list.__name__ + ':' +color.END, '列出主類別列表')
		print(color.BOLD + color.DARKCYAN + '--' + ArgvEnum.sublist.__name__ + ' [*主類別]:' +color.END, '列出主類別中的子類別列表')
		print(color.BOLD + color.DARKCYAN + '--' + ArgvEnum.area.__name__ + ':' +color.END, '列出地區編號資訊')
		print(color.BOLD + color.DARKCYAN + '--' + ArgvEnum.about.__name__ + ':' +color.END, '關於此程式的說明')
		print(color.BOLD + color.DARKCYAN + '--' + ArgvEnum.info.__name__ + ':' +color.END, '關於此程式的開發資訊')

# 處理 argv 的參數
def __parse_argv():
	if 2 == len(sys.argv):
		if '--list' == sys.argv[1]:
			return ArgvEnum.list()
		elif '--area' == sys.argv[1]:
			return ArgvEnum.area()
		elif '--about' == sys.argv[1]:
			return ArgvEnum.about()
		elif '--info' == sys.argv[1]:
			return ArgvEnum.info()

	elif 3 == len(sys.argv):
		if '--sublist' == sys.argv[1]:
			return ArgvEnum.sublist(sys.argv[2])

	elif 4 <= len(sys.argv):
		if '--spider' == sys.argv[1]:
			if 5 == len(sys.argv):
				return ArgvEnum.spider(sys.argv[2], sys.argv[3], sys.argv[4])
			else:
				return ArgvEnum.spider(sys.argv[2], sys.argv[3])

	return ArgvEnum.none()

# 主程式進入口
if __name__ == '__main__':
	__parse_argv()






