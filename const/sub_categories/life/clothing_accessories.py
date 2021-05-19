from typing import Dict
from ..base_category import BaseCategory

# 布行 textiles
class Textiles(object):
   def textiles() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '布行'
      list['id'] = 'textiles'

      textiles = {}
      textiles['fabric-shop'] = '布行'

      list['sub'] = textiles
      return list

# 流行品牌 fashion-popular
class FashionPopular(object):
   def fashion_popular() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '流行品牌'
      list['id'] = 'fashion-popular'

      fashion_popular = {}
      fashion_popular['fashion-garment'] = '流行服飾'

      list['sub'] = fashion_popular
      return list

# 成衣 garment
class Garment(object):
   def garment() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '成衣'
      list['id'] = 'garment'

      garment = {}
      garment['apparel-equip-and-supplies'] = '成衣製造設備'
      garment['t-shirts'] = 'Ｔ恤'
      garment['feather-clothing'] = '羽毛衣'
      garment['shirts'] = '襯衫'
      garment['uniforms'] = '制服'
      garment['fashion'] = '時裝百貨'
      garment['garment'] = '成衣'
      garment['large-size-clothes'] = '大尺碼衣服'
      garment['garment-production'] = '成衣加工'
      garment['leather-fur'] = '皮衣、皮草'

      list['sub'] = garment
      return list

# 二手衣 second-hand-clothing
class SecondHandClothing(object):
   def second_hand_clothing() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '二手衣'
      list['id'] = 'second-hand-clothing'

      second_hand_clothing = {}
      second_hand_clothing['secondhand-clothes'] = '二手衣'

      list['sub'] = second_hand_clothing
      return list

# 內衣睡衣 underwear
class Underwear(object):
   def underwear() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '內衣睡衣'
      list['id'] = 'underwear'

      underwear = {}
      underwear['sleepwear'] = '睡衣'
      underwear['underwear'] = '內衣褲'

      list['sub'] = underwear
      return list


# 孕婦服裝 maternity-apparel
class MaternityApparel(object):
   def maternity_apparel() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '孕婦服裝'
      list['id'] = 'maternity-apparel'

      maternity_apparel = {}
      maternity_apparel['maternity-dress'] = '孕婦裝'

      list['sub'] = maternity_apparel
      return list


# 童裝及嬰幼兒食用品 children-infant-accessories
class ChildrenInfantAccessories(object):
   def children_infant_accessories() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '童裝及嬰幼兒食用品'
      list['id'] = 'children-infant-accessories'

      children_infant_accessories = {}
      children_infant_accessories['baby-food'] = '嬰兒食品'
      children_infant_accessories['kids-clothes'] = '童裝'
      children_infant_accessories['baby-products'] = '嬰兒用品'

      list['sub'] = children_infant_accessories
      return list

# 婚紗禮服 wedding-dress
class WeddingDress(object):
   def wedding_dress() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '婚紗禮服'
      list['id'] = 'wedding-dress'

      wedding_dress = {}
      wedding_dress['wedding-supplies-and-consultants'] = '結婚用品'
      wedding_dress['wedding-dress'] = '婚紗禮服'

      list['sub'] = wedding_dress
      return list

# 運動休閒服 sportswear
class Sportswear(object):
   def sportswear() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '運動休閒服'
      list['id'] = 'sportswear'

      sportswear = {}
      sportswear['jeans'] = '牛仔服飾'
      sportswear['sports-wear'] = '運動服'
      sportswear['swimming-suites'] = '游泳衣褲'

      list['sub'] = sportswear
      return list

# 特殊服裝 special-clothes
class SpecialClothes(object):
   def special_clothes() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '特殊服裝'
      list['id'] = 'special-clothes'

      special_clothes = {}
      special_clothes['costume-drama'] = '戲劇服裝'
      special_clothes['dance-clothing-dance-supplies'] = '舞蹈服裝用品'

      list['sub'] = special_clothes
      return list

# 毛織品 wool
class Wool(object):
   def wool() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '毛織品'
      list['id'] = 'wool'

      wool = {}
      wool['wool-clothes'] = '羊毛織品'
      wool['sweaters'] = '毛衣'

      list['sub'] = wool
      return list

# 穿著配件 apparel-accessories
class ApparelAccessories(object):
   def apparel_accessories() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '穿著配件'
      list['id'] = 'apparel-accessories'

      apparel_accessories = {}
      apparel_accessories['hair-accessories'] = '髮飾頭飾'
      apparel_accessories['ties'] = '領帶領結'
      apparel_accessories['ribbons'] = '緞帶絲帶織帶'
      apparel_accessories['belts'] = '皮帶'
      apparel_accessories['socks-stockings'] = '襪子、絲襪'
      apparel_accessories['hats'] = '帽子'
      apparel_accessories['gloves'] = '手套'
      apparel_accessories['handkerchief'] = '手帕'

      list['sub'] = apparel_accessories
      return list

# 鞋 shoes
class Shoes(object):
   def hoes() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '鞋'
      list['id'] = 'shoes'

      shoes = {}
      shoes['shoe-repair'] = '修鞋補鞋'
      shoes['shoes'] = '鞋'
      shoes['shoe-material-and-supplies'] = '鞋材用品'

      list['sub'] = shoes
      return list

# 衣服縫製及修改 clothing-modification
class ClothingModification(object):
   def clothing_modification() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '衣服縫製及修改'
      list['id'] = 'clothing-modification'

      clothing_modification = {}
      clothing_modification['fashion-design'] = '服裝設計'
      clothing_modification['tailor-made-clothes'] = '服裝訂製'
      clothing_modification['alteration'] = '衣服修改'
      clothing_modification['embroidering'] = '電繡'

      list['sub'] = clothing_modification
      return list

# 衣服材料 clothing-materials
class ClothingMaterials(object):
   def clothing_materials() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '衣服材料'
      list['id'] = 'clothing-materials'

      clothing_materials = {}
      clothing_materials['elastic-sidebands'] = '鬆緊帶包邊帶'
      clothing_materials['buttons'] = '鈕扣'
      clothing_materials['knitwear'] = '針織品'
      clothing_materials['garment-accessories'] = '衣著零件配料'
      clothing_materials['zippers'] = '拉鍊'

      list['sub'] = clothing_materials
      return list

# 皮件行李箱 leather-luggage
class LeatherLuggage(object):
   def leather_luggage() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '皮件行李箱'
      list['id'] = 'leather-luggage'

      leather_luggage = {}
      leather_luggage['leather-repair-clean'] = '皮件清潔保養'
      leather_luggage['leather-goods'] = '皮包皮件'
      leather_luggage['luggages'] = '旅行箱袋'
      leather_luggage['handbags'] = '手提包'

      list['sub'] = leather_luggage
      return list

# 雨具 rain-gear
class RainGear(object):
   def rain_gear() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '雨具'
      list['id'] = 'rain-gear'

      rain_gear = {}
      rain_gear['raincoat-rain-gear'] = '雨衣雨具'
      rain_gear['umbrella'] = '雨傘'

      list['sub'] = rain_gear
      return list

# 洗衣服務 laundry-services
class LaundryServices(object):
   def laundry_services() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '洗衣服務'
      list['id'] = 'laundry-services'

      laundry_services = {}
      laundry_services['laundry-supplies'] = '洗衣店配備'
      laundry_services['laundry-services'] = '洗衣店'

      list['sub'] = laundry_services
      return list

# 陳列配備 display-equipment
class DisplayEquipment(object):
   def display_equipment() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '陳列配備'
      list['id'] = 'display-equipment'

      display_equipment = {}
      display_equipment['models'] = '模特兒'
      display_equipment['hangers'] = '衣架吊架'

      list['sub'] = display_equipment
      return list

# 女裝 women-dress
class WomenDress(object):
   def women_dress() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '女裝'
      list['id'] = 'women-dress'

      women_dress = {}
      women_dress['senior-womens-wear'] = '媽媽裝'
      women_dress['womens-fashion'] = '女裝'
      women_dress['girls'] = '少女服飾'

      list['sub'] = women_dress
      return list

# 男裝 man-dress
class ManDress(object):
   def man_dress() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '男裝'
      list['id'] = 'man-dress'

      man_dress = {}
      man_dress['menswear'] = '男裝'
      man_dress['teenagers'] = '青少年服裝'

      list['sub'] = man_dress
      return list

# 衣著配件 clothing-accessories
class ClothingAccessories(BaseCategory, Textiles, FashionPopular, Garment, SecondHandClothing, 
Underwear, MaternityApparel, ChildrenInfantAccessories, WeddingDress, Sportswear, SpecialClothes, 
Wool, ApparelAccessories, Shoes, ClothingModification, ClothingMaterials, LeatherLuggage, 
RainGear, LaundryServices, DisplayEquipment, WomenDress, ManDress):
   category_name = '衣著配件'
   category_id = 'clothing-accessories'