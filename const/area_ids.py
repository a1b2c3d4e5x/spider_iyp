
from .constant import constant

class __ConstAreaIds(object):

   # 全部
   @constant
   def all() -> [int, str]:
      list = {}
      list['不分區'] = area.taiwan
      list['北部'] = area.north
      list['中部'] = area.central
      list['南部'] = area.south
      list['東部'] = area.east
      list['離島'] = area.outlying_islands
      return list

   # 全區
   @constant
   def taiwan() -> [int, str]:
      list = {}
      list[0] = '全區'
      return list

   # 北部
   @constant
   def north() -> [int, str]:
      list = {}
      list[1] = '宜蘭縣'
      list[3] = '基隆市'
      list[4] = '新北市'
      list[5] = '桃園市'
      list[6] = '台北市'
      list[7] = '新竹縣'
      list[8] = '苗栗縣'
      return list

   # 中部
   @constant
   def central() -> [int, str]:
      list = {}
      list[9] = '台中市'
      list[11] = '彰化縣'
      list[12] = '南投縣'
      list[13] = '雲林縣'
      return list

   # 南部 South
   @constant
   def south() -> [int, str]:
      list = {}
      list[14] = '嘉義縣'
      list[15] = '台南市'
      list[18] = '高雄市'
      list[21] = '屏東縣'
      return list

   # 東部
   @constant
   def east() -> [int, str]:
      list = {}
      list[2] = '花蓮縣'
      list[22] = '台東縣'
      return list

   # 離島 
   @constant
   def outlying_islands():
      list = {}
      list[17] = '澎湖縣'
      list[20] = '金門縣'
      return list

area = __ConstAreaIds()

