from typing import Dict
from ..base_category import BaseCategory

# 百貨賣場 department-store
class DepartmentStore(object):
   def department_store() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '百貨賣場'
      list['id'] = 'department-store'

      department_store = {}
      department_store['warehouse-stores'] = '量販店'
      department_store['mail-order-TV-shopping'] = '電視購物'
      department_store['supermarkets'] = '超商、購物中心'
      department_store['department-stores-boutiques'] = '精品百貨'

      list['sub'] = department_store
      return list

# 俗賣省錢 money-save-products
class MoneySaveProducts(object):
   def money_save_products() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '俗賣省錢'
      list['id'] = 'money-save-products'

      money_save_products = {}
      money_save_products['secondhand-goods'] = '二手商品'
      money_save_products['discount-stores'] = '一元商品'

      list['sub'] = money_save_products
      return list

# 個性化商品 personalized-product
class PersonalizedProduct(object):
   def personalized_product() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '個性化商品'
      list['id'] = 'personalized-product'

      personalized_product = {}
      personalized_product['sex-toys'] = '情趣用品'
      personalized_product['personalized-stores'] = '個性化商店'

      list['sub'] = personalized_product
      return list

# 化粧品 cosmetics
class Cosmetics(object):
   def cosmetics() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '化粧品'
      list['id'] = 'cosmetics'

      cosmetics = {}
      cosmetics['cosmetics'] = '化粧品'
      cosmetics['cosmetic-manufacturers'] = '化粧品製造'

      list['sub'] = cosmetics
      return list

# 沐浴用品 bath-supplies
class BathSupplies(object):
   def bath_supplies() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '沐浴用品'
      list['id'] = 'bath-supplies'

      bath_supplies = {}
      bath_supplies['bath-supplies'] = '沐浴用品'

      list['sub'] = bath_supplies
      return list

# 珠寶 jewerlly
class Jewerlly(object):
   def jewerlly() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '珠寶'
      list['id'] = 'jewerlly'

      jewerlly = {}
      jewerlly['jade'] = '玉飾'
      jewerlly['jewelry'] = '銀樓、珠寶'

      list['sub'] = jewerlly
      return list

# 貴重金屬 precious-metals
class PreciousMetals(object):
   def precious_metals() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '貴重金屬'
      list['id'] = 'precious-metals'

      precious_metals = {}
      precious_metals['precious-metals'] = '貴金屬'

      list['sub'] = precious_metals
      return list

# 飾品 accessories
class Accessories(object):
   def accessories() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '飾品'
      list['id'] = 'accessories'

      accessories = {}
      accessories['mobile-phone-straps'] = '手機吊飾'
      accessories['accessories'] = '飾品'
      accessories['accessory-manufacturers'] = '飾品製造'

      list['sub'] = accessories
      return list

# 禮品 gift
class Gift(object):
   def gift() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '禮品'
      list['id'] = 'gift'

      gift = {}
      gift['gift-manufacturers'] = '禮贈品製造'
      gift['gifts'] = '禮贈品'

      list['sub'] = gift
      return list

# 藝品 arts
class Arts(object):
   def arts() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '藝品'
      list['id'] = 'arts'

      arts = {}
      arts['craft-manufacturers'] = '藝品製造'
      arts['crafts'] = '藝品'

      list['sub'] = arts
      return list

# 工藝材料 craft-materials
class CraftMaterials(object):
   def craft_materials() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '工藝材料'
      list['id'] = 'craft-materials'

      craft_materials = {}
      craft_materials['craft-materials'] = '工藝材料'

      list['sub'] = craft_materials
      return list

# 人造植物 artificial-plants
class ArtificialPlants(object):
   def artificial_plants() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '人造植物'
      list['id'] = 'artificial-plants'

      artificial_plants = {}
      artificial_plants['artificial-flowers'] = '人造花'

      list['sub'] = artificial_plants
      return list

# 節慶用品 ceremony-supplies
class CeremonySupplies(object):
   def ceremony_supplies() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '節慶用品'
      list['id'] = 'ceremony-supplies'

      ceremony_supplies = {}
      ceremony_supplies['Christmas-decorations'] = '聖誕飾品'
      ceremony_supplies['fireworks'] = '炮竹、煙火'
      ceremony_supplies['Christmas-decoration-manufacturers'] = '聖誕飾品製造'

      list['sub'] = ceremony_supplies
      return list

# 玩具 toys
class Toys(object):
   def toys() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '玩具'
      list['id'] = 'toys'

      toys = {}
      toys['toys'] = '玩具'
      toys['toy-manufacturers'] = '玩具製造'

      list['sub'] = toys
      return list

# 餐具茶具 tableware
class Tableware(object):
   def tableware() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '餐具茶具'
      list['id'] = 'tableware'

      tableware = {}
      tableware['tablewares'] = '餐具茶具'
      tableware['tablewares-manufacturers'] = '餐具製造'

      list['sub'] = tableware
      return list

# 鎖匙配製 lock
class Lock(object):
   def lock() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '鎖匙配製'
      list['id'] = 'lock'

      lock = {}
      lock['locks'] = '開鎖'

      list['sub'] = lock
      return list

# 家庭雜貨 grocery
class Grocery(object):
   def grocery() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '家庭雜貨'
      list['id'] = 'grocery'

      grocery = {}
      grocery['cleaning-product-manfuacturers'] = '清潔用品'
      grocery['household-goods-manufacturers'] = '家庭雜貨製造'
      grocery['household-goods'] = '家庭雜貨'

      list['sub'] = grocery
      return list

# 防身器材 defensive-device
class DefensiveDevice(object):
   def defensive_device() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '防身器材'
      list['id'] = 'defensive-device'

      defensive_device = {}
      defensive_device['self-defensive-equip'] = '防身器材'

      list['sub'] = defensive_device
      return list

# 軍需用品 munitions
class Munitions(object):
   def munitions() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '軍需用品'
      list['id'] = 'munitions'

      munitions = {}
      munitions['military-supplies'] = '軍用品'

      list['sub'] = munitions
      return list

# 百貨購物 shopping
class Shopping(BaseCategory, DepartmentStore, MoneySaveProducts, PersonalizedProduct, Cosmetics, 
BathSupplies, Jewerlly, PreciousMetals, Accessories, Gift, Arts, CraftMaterials, ArtificialPlants,
CeremonySupplies, Toys, Tableware, Lock, Grocery, DefensiveDevice, Munitions):
   category_name = '百貨購物'
   category_id = 'shopping'