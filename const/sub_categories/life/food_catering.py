from typing import Dict
from ..base_category import BaseCategory

class NativeGoods(object):
   def native_goods() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '土產品'
      list['id'] = 'native-goods'

      native_goods = {}
      native_goods['famous'] = '名特產'
      native_goods['local-special'] = '土產品'

      list['sub'] = native_goods
      return list

# 農產品 agricultural-products
class AgriculturalProducts(object):
   def agricultural_products() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '農產品'
      list['id'] = 'agricultural-products'

      agricultural_products = {}
      agricultural_products['agriculture-trade'] = '農產品進出口'
      agricultural_products['agriculture-processing'] = '農產品加工'
      agricultural_products['organic'] = '有機農產品'
      agricultural_products['rice'] = '米'
      agricultural_products['grain'] = '糧食穀類'
      agricultural_products['mushroom'] = '香菇'

      list['sub'] = agricultural_products
      return list

# 生鮮食品 fresh-food
class FreshFood(object):
   def fresh_food() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '生鮮食品'
      list['id'] = 'fresh-food'

      fresh_food = {}
      fresh_food['meat'] = '肉品'
      fresh_food['egg'] = '蛋'
      fresh_food['vegetable'] = '蔬菜'
      fresh_food['fruit'] = '水果'
      fresh_food['fisheries'] = '水產海鮮'

      list['sub'] = fresh_food
      return list

# 食品 food
class Food(object):
   def food() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '食品'
      list['id'] = 'food'

      food = {}
      food['cooked-food'] = '油飯調理食品'
      food['canned-food'] = '罐頭食品'
      food['vegetarian-food'] = '素食食品'
      food['organic-diet'] = '生機飲食'
      food['markets'] = '市場超市'
      food['stewed-meat'] = '滷味肉乾'
      food['smoked-food'] = '煙燻燒臘'
      food['food-processing'] = '食品加工'
      food['food-dealers'] = '食品買賣'
      food['food-materials'] = '食品原料'
      food['spice'] = '香料添加物'
      food['grocery'] = '南北貨'
      food['lactic-acid'] = '乳酸'
      food['bean-curd'] = '豆類製品'

      list['sub'] = food
      return list

# 冷凍食品 frozen-foods
class FrozenFoods(object):
   def frozen_foods() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '冷凍食品'
      list['id'] = 'frozen-foods'

      frozen_foods = {}
      frozen_foods['frozen-food'] = '冷凍食品'

      list['sub'] = frozen_foods
      return list

# 食用油 edible-oils
class EdibleOils(object):
   def edible_oils() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '食用油'
      list['id'] = 'edible-oils'

      edible_oils = {}
      edible_oils['cooking-oil'] = '食用油'

      list['sub'] = edible_oils
      return list

# 調味品 flavoring-extracts
class FlavoringExtracts(object):
   def flavoring_extracts() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '調味品'
      list['id'] = 'flavoring-extracts'

      flavoring_extracts = {}
      flavoring_extracts['seasoning'] = '調味料'
      flavoring_extracts['soy-sauce-oyster-sauce'] = '醬油蠔油'

      list['sub'] = flavoring_extracts
      return list

# 休閒零食 snack-food
class SnackFood(object):
   def snack_food() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '休閒零食'
      list['id'] = 'snack-food'

      snack_food = {}
      snack_food['areca'] = '檳榔'
      snack_food['cookies'] = '餅乾'
      snack_food['candied-fruit'] = '蜜餞'
      snack_food['confectionery'] = '糖果糕點'
      snack_food['snack-food'] = '休閒零食'

      list['sub'] = snack_food
      return list

# 飲料冰品 beverage
class Beverage(object):
   def beverage() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '飲料冰品'
      list['id'] = 'beverage'

      beverage = {}
      beverage['beverage-material-supplies'] = '飲料原料'
      beverage['distilled-water-mineral-water'] = '蒸餾礦泉水'
      beverage['tea'] = '茶葉'
      beverage['juice'] = '果汁'
      beverage['ice'] = '冰品'
      beverage['coffee'] = '咖啡'
      beverage['beverage'] = '飲料'
      beverage['soda'] = '汽水'
      beverage['milk-and-dairy-products'] = '牛奶及奶製品'

      list['sub'] = beverage
      return list

# 菸酒 wine-cigarette
class WineCigarette(object):
   def wine_cigarette() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '菸酒'
      list['id'] = 'wine-cigarette'

      wine_cigarette = {}
      wine_cigarette['cigar-tobacco'] = '雪茄煙草'
      wine_cigarette['cigarette-filter'] = '香煙濾嘴'
      wine_cigarette['beer'] = '啤酒'
      wine_cigarette['wine-and-cigarette'] = '菸酒'
      wine_cigarette['imported-cigarette-and-liquor'] = '洋菸洋酒'

      list['sub'] = wine_cigarette
      return list

# 西點麵食 pasta
class Pasta(object):
   def pasta() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '西點麵食'
      list['id'] = 'pasta'

      pasta = {}
      pasta['wedding-cake'] = '喜餅'
      pasta['noodle'] = '麵條製品'
      pasta['bread-biscuit'] = '麵包糕餅'

      list['sub'] = pasta
      return list

# 速食外賣 order-food-delivery
class OrderFoodDelivery(object):
   def order_food_delivery() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '速食外賣'
      list['id'] = 'order-food-delivery'

      order_food_delivery = {}
      order_food_delivery['western-fast-food'] = '西式速食'
      order_food_delivery['Japanese-fast-food'] = '日式速食'
      order_food_delivery['Chinese-fast-food'] = '中式速食'

      list['sub'] = order_food_delivery
      return list

# 美食佳餚 cuisine
class Cuisine(object):
   def cuisine() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '美食佳餚'
      list['id'] = 'cuisine'

      cuisine = {}
      cuisine['italina-cuisine'] = '義式料理'
      cuisine['restaurants'] = '餐廳'
      cuisine['BBQ'] = '烤肉、燒烤'
      cuisine['teppanyaki'] = '鐵板燒'
      cuisine['noodle-pastry'] = '麵食點心'
      cuisine['fast-food'] = '速食店'
      cuisine['beer-house'] = '啤酒屋'
      cuisine['vegetarian'] = '素食'
      cuisine['steak-house'] = '牛排西餐'
      cuisine['Germany'] = '德式料理'
      cuisine['American'] = '美式料理'
      cuisine['French'] = '法式料理'
      cuisine['Vietnam'] = '越南菜'
      cuisine['Indian'] = '印度料理'
      cuisine['Korean'] = '韓國料理'
      cuisine['Thai'] = '泰式料理'
      cuisine['Japanese'] = '日式料理'
      cuisine['regimen'] = '養生藥膳'
      cuisine['ginger-duck'] = '薑母鴨'
      cuisine['Hakka-cuisine'] = '客家菜'
      cuisine['goat-meat-pot'] = '羊肉爐'
      cuisine['abalone-and-shark-fin'] = '鮑翅'
      cuisine['dim-sum'] = '港式飲茶'
      cuisine['Shanghai-Zhejiang-cuisine'] = '上海江浙菜'
      cuisine['Hunan-cuisine'] = '湘菜'
      cuisine['Taiwanese-cuisine'] = '台菜'
      cuisine['garden-restaurant'] = '庭園餐廳'
      cuisine['Beijing-cuisine'] = '北平菜'
      cuisine['edible-wild-herbs'] = '山產野菜'
      cuisine['snack-stand'] = '小吃'
      cuisine['cafe'] = '咖啡館'
      cuisine['tea-room'] = '茶藝館'
      cuisine['bubble-tea'] = '泡沫紅茶'
      cuisine['seafood'] = '海鮮料理'
      cuisine['Zhou-dishes'] = '清粥小菜'
      cuisine['hot-pot-shabu-shabu'] = '火鍋涮涮鍋'
      cuisine['breakfast'] = '早餐店'
      cuisine['Soybean-milk-sesame-biscuits'] = '豆漿燒餅'
      cuisine['ice-shops'] = '冰品店'

      list['sub'] = cuisine
      return list

# 餐盒業 lunch-box
class LunchBox(object):
   def lunch_box() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '餐盒業'
      list['id'] = 'lunch-box'

      lunch_box = {}
      lunch_box['lunch-boxes'] = '便當餐盒'

      list['sub'] = lunch_box
      return list

# 辦桌外燴 catering-service
class CateringService(object):
   def catering_service() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '辦桌外燴'
      list['id'] = 'catering-service'

      catering_service = {}
      catering_service['catering-banquet-supplies'] = '外燴筵席用品'
      catering_service['Catering-banquet'] = '辦桌外燴'

      list['sub'] = catering_service
      return list

# 飲食業設備用品 catering-appliance
class CateringAppliance(object):
   def catering_appliance() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '飲食業設備用品'
      list['id'] = 'catering-appliance'

      catering_appliance = {}
      catering_appliance['restaurant-equip'] = '餐飲設備用品'

      list['sub'] = catering_appliance
      return list

# 食品餐飲 food-catering
class FoodCatering(BaseCategory, NativeGoods, AgriculturalProducts, FreshFood, Food,
FrozenFoods, EdibleOils, FlavoringExtracts, SnackFood, Beverage,WineCigarette,
Pasta, OrderFoodDelivery, Cuisine, LunchBox, CateringService, CateringAppliance):
   category_name = '食品餐飲'
   category_id = 'food-catering'

