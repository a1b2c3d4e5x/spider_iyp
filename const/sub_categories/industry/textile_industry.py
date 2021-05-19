from typing import Dict
from ..base_category import BaseCategory

# 人造纖維製品 man-made-fiber
class ManMadeFiber(object):
   def man_made_fiber() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '人造纖維製品'
      list['id'] = 'man-made-fiber'

      man_made_fiber = {}
      man_made_fiber['man-made-fiber'] = '人造纖維'

      list['sub'] = man_made_fiber
      return list

# 棉毛紗線 cotton-and-yarn
class CottonAndYarn(object):
   def cotton_and_yarn() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '棉毛紗線'
      list['id'] = 'cotton-and-yarn'

      cotton_and_yarn = {}
      cotton_and_yarn['cotton-yarns'] = '棉紗'
      cotton_and_yarn['wool-yarns'] = '羊毛'
      cotton_and_yarn['yarns'] = '紗'

      list['sub'] = cotton_and_yarn
      return list

# 布 cloth
class Cloth(object):
   def cloth() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '布'
      list['id'] = 'cloth'

      cloth = {}
      cloth['non-woven'] = '不織布'
      cloth['denim'] = '牛仔布'
      cloth['nylon'] = '尼龍布'
      cloth['wool'] = '毛布'
      cloth['woven'] = '平織布'
      cloth['sofa-curtain-fabric'] = '窗簾布、沙發布'
      cloth['cotton'] = '棉布'
      cloth['jacquard'] = '提花布'
      cloth['tricot'] = '針織布'
      cloth['grey-cloth'] = '胚布'
      cloth['canvas'] = '帆布'
      cloth['fabric'] = '布'

      list['sub'] = cloth
      return list

# 印染 dying
class Dying(object):
   def dying() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '印染'
      list['id'] = 'dying'

      dying = {}
      dying['printing'] = '印花'
      dying['dying'] = '染整'
      dying['flocking'] = '靜電植毛'

      list['sub'] = dying
      return list

# 織品 fabric-products
class FabricProducts(object):
   def fabric_products() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '織品'
      list['id'] = 'fabric-products'

      fabric_products = {}
      fabric_products['nylon'] = '尼龍'
      fabric_products['Tarpaulin'] = '帆布篷'
      fabric_products['cotton'] = '棉織品'
      fabric_products['elastic'] = '彈性'
      fabric_products['woven-labels'] = '織標'
      fabric_products['ropes'] = '織繩'
      fabric_products['nylon-velcro'] = '尼龍黏扣帶'

      list['sub'] = fabric_products
      return list

# 紡織工業 textile-industry
class TextileIndustry(BaseCategory, ManMadeFiber, CottonAndYarn, Cloth, Dying, FabricProducts):
   category_name = '紡織工業'
   category_id = 'textile-industry'