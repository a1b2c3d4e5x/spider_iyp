from typing import Dict
from ..base_category import BaseCategory

# 皮革羽毛 leather-and-feather
class LeatherAndFeather(object):
   def leather_and_feather() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '皮革羽毛'
      list['id'] = 'leather-and-feather'

      leather_and_feather = {}
      leather_and_feather['leather-fur'] = '皮革、毛皮'
      leather_and_feather['feather-products'] = '羽毛'

      list['sub'] = leather_and_feather
      return list

# 林業及林產品 forest-products
class ForestProducts(object):
   def forest_products() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '林業及林產品'
      list['id'] = 'forest-products'

      forest_products = {}
      forest_products['wood'] = '木材'
      forest_products['wooden-case-pallet'] = '木箱、棧板'
      forest_products['bamboo-rattan'] = '竹材、籐材'
      forest_products['charcoal'] = '木炭、木柴'

      list['sub'] = forest_products
      return list

# 畜牧業及產品 livestock-and-products
class LivestockAndProducts(object):
   def livestock_and_products() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '畜牧業及產品'
      list['id'] = 'livestock-and-products'

      livestock_and_products = {}
      livestock_and_products['farm-equip'] = '畜產設備'
      livestock_and_products['farms'] = '畜牧場'
      livestock_and_products['slaughterhouse'] = '屠宰場'
      livestock_and_products['feeds'] = '飼料'

      list['sub'] = livestock_and_products
      return list

# 農事服務業 agricultural-services
class AgriculturalServices(object):
   def agricultural_services() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '農事服務業'
      list['id'] = 'agricultural-services'

      agricultural_services = {}
      agricultural_services['agriculture-service'] = '農事服務'

      list['sub'] = agricultural_services
      return list

# 農業 agriculture
class Agriculture(object):
   def agriculture() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '農業'
      list['id'] = 'agriculture'

      agriculture = {}
      agriculture['orchards-farms'] = '果園、農場'
      agriculture['fertilizer'] = '肥料'
      agriculture['agriculture-equip'] = '農耕設備'
      agriculture['seeds'] = '種子'

      list['sub'] = agriculture
      return list

# 漁業及漁產品 fisheries-and-products
class FisheriesAndProducts(object):
   def fisheries_and_products() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '漁業及漁產品'
      list['id'] = 'fisheries-and-products'

      fisheries_and_products = {}
      fisheries_and_products['aquaculture'] = '水產養殖'
      fisheries_and_products['aquaculture-equipment'] = '水產養殖用品'
      fisheries_and_products['fishery'] = '漁產捕撈'

      list['sub'] = fisheries_and_products
      return list

# 礦業及礦產品 mining-and-minerals
class MiningAndMinerals(object):
   def mining_and_minerals() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '礦業及礦產品'
      list['id'] = 'mining-and-minerals'

      mining_and_minerals = {}
      mining_and_minerals['quarry'] = '石礦'
      mining_and_minerals['coal'] = '煤礦、煤炭'
      mining_and_minerals['mining'] = '採礦'
      mining_and_minerals['mineral'] = '礦物'

      list['sub'] = mining_and_minerals
      return list

# 農林漁牧 agriculture
class Agriculture(BaseCategory, LeatherAndFeather, ForestProducts, LivestockAndProducts, 
AgriculturalServices, Agriculture, FisheriesAndProducts, MiningAndMinerals):
   category_name = '農林漁牧'
   category_id = 'agriculture'