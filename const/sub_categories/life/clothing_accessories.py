from typing import Dict
from ..base_category import BaseCategory

# 布行 textiles
class textiles(object):
   def textiles() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '布行'
      list['id'] = 'textiles'

      textiles = {}
      textiles['fabric-shop'] = '布行'

      list['sub'] = textiles
      return list

# 衣著配件 clothing-accessories
class ClothingAccessories(BaseCategory):
   category_name = '衣著配件'
   category_id = 'clothing-accessories'