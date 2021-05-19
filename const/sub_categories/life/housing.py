from typing import Dict
from ..base_category import BaseCategory

# 營建工程 construction-engineering
class ConstructionEngineering(object):
   def construction_engineering() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '營建工程'
      list['id'] = 'construction-engineering'

      construction_engineering = {}
      construction_engineering['removal'] = '拆遷工程'
      construction_engineering['building-cleaning'] = '建築物清洗'
      construction_engineering['road-works'] = '道路工程'
      construction_engineering['clean-rooms'] = '無塵室工程'
      construction_engineering['swimming-pools'] = '游泳池承造'
      construction_engineering['landscape'] = '景觀工程'
      construction_engineering['civil-contractors'] = '土木承包商'
      construction_engineering['scaffolding-works'] = '鷹架工程'
      construction_engineering['steel-works'] = '鋼構工程'
      construction_engineering['construction-companies'] = '營造廠'
      construction_engineering['drilling'] = '鑽探工程'
      construction_engineering['architectures'] = '建築師'
      construction_engineering['construction'] = '營建工程'
      construction_engineering['polishing-equip-supplies'] = '拋光設備用品'

      list['sub'] = construction_engineering
      return list

# 建築材料 building-materials
class BuildingMaterials(object):
   def building_materials() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '建築材料'
      list['id'] = 'building-materials'

      building_materials = {}
      building_materials['fire-retardant-materials'] = '耐火建材'
      building_materials['lumber-wallboards'] = '建築木材、隔板'
      building_materials['curtain-walls'] = '帷幕牆'
      building_materials['asphalt'] = '瀝青、柏油'
      building_materials['building-materials'] = '建築材料'
      building_materials['doors-and-windows'] = '門窗'
      building_materials['automatic-doors'] = '玻璃自動門'
      building_materials['electric-shutters'] = '電動捲門'
      building_materials['aluminum-windows-and-doors'] = '鋁門窗'
      building_materials['cement'] = '水泥'
      building_materials['concrete'] = '混凝土'
      building_materials['gravel'] = '砂石'
      building_materials['brick-tile-stone'] = '地磚石材'
      building_materials['flooring-materials'] = '地板材料'
      building_materials['ceiling'] = '天花板'
      building_materials['tiles'] = '磁磚'
      building_materials['marble'] = '大理石'

      list['sub'] = building_materials
      return list

# 建築模型及繪圖 building-model
class BuildingModel(object):
   def building_model() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '建築模型及繪圖'
      list['id'] = 'building-model'

      building_model = {}
      building_model['building-models-drawing'] = '建築模型與繪圖'

      list['sub'] = building_model
      return list

# 裝潢工程 decoration-works
class DecorationWorks(object):
   def decoration_works() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '裝潢工程'
      list['id'] = 'decoration-works'

      decoration_works = {}
      decoration_works['awnings-security-windows'] = '雨棚鐵窗工程'
      decoration_works['decorations'] = '裝潢工程'
      decoration_works['interior-designs'] = '室內設計'
      decoration_works['painting-service'] = '油漆工程'
      decoration_works['flooring'] = '地板工程'
      decoration_works['wall-papers'] = '壁紙'
      decoration_works['glass-installation'] = '玻璃安裝'
      decoration_works['tatami-paper-doors'] = '疊蓆、紙門'
      decoration_works['woodworking'] = '木工'

      list['sub'] = decoration_works
      return list

# 水電空調工程 air-conditioning-engineering
class AirConditioningEngineering(object):
   def air_conditioning_engineering() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '水電空調工程'
      list['id'] = 'air-conditioning-engineering'

      air_conditioning_engineering = {}
      air_conditioning_engineering['plumbing-and-electrical-engineering'] = '水電工程'
      air_conditioning_engineering['plumbing-and-electrical-materials'] = '水電器材'
      air_conditioning_engineering['air-condition'] = '空調工程'
      air_conditioning_engineering['water-tanks'] = '水塔'

      list['sub'] = air_conditioning_engineering
      return list

# 工程檢測 engineering-testing
class EngineeringTesting(object):
   def engineering_testing() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '工程檢測'
      list['id'] = 'engineering-testing'

      engineering_testing = {}
      engineering_testing['building-safety'] = '建築安全檢查'
      engineering_testing['concrete-test'] = '混凝土試驗'
      engineering_testing['construction-inspection'] = '工程檢測'

      list['sub'] = engineering_testing
      return list

# 防水理水工程 waterproof-engineering
class WaterproofEngineering(object):
   def waterproof_engineering() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '防水理水工程'
      list['id'] = 'waterproof-engineering'

      waterproof_engineering = {}
      waterproof_engineering['plumbers'] = '防水抓漏工程'
      waterproof_engineering['water-treatments'] = '水處理'

      list['sub'] = waterproof_engineering
      return list

# 衛浴設備及用品 bathroom-supplies
class BathroomSupplies(object):
   def bathroom_supplies() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '衛浴設備及用品'
      list['id'] = 'bathroom-supplies'

      bathroom_supplies = {}
      bathroom_supplies['bathroom-fixtures'] = '衛浴設備'
      bathroom_supplies['water-heaters'] = '熱水器'
      bathroom_supplies['solar-power-water-heaters'] = '太陽能熱水器'
      bathroom_supplies['sauna-equipment'] = '三溫暖設備'

      list['sub'] = bathroom_supplies
      return list

# 廚具爐具 kitchen-appliances
class KitchenAppliances(object):
   def kitchen_appliances() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '廚具爐具'
      list['id'] = 'kitchen-appliances'

      kitchen_appliances = {}
      kitchen_appliances['cookware'] = '烹飪用具'
      kitchen_appliances['range-hood'] = '抽油煙機'
      kitchen_appliances['gas-supplies'] = '瓦斯煤氣行'
      kitchen_appliances['gas-stoves'] = '瓦斯爐'
      kitchen_appliances['kitchen-equip'] = '廚具流理台設備'

      list['sub'] = kitchen_appliances
      return list

# 電梯升降設備 lifting-equipment
class LiftingEquipment(object):
   def lifting_equipment() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '電梯升降設備'
      list['id'] = 'lifting-equipment'

      lifting_equipment = {}
      lifting_equipment['elevators-lifts'] = '電梯、升降機'

      list['sub'] = lifting_equipment
      return list

# 公寓大廈管理 building-management
class BuildingManagement(object):
   def building_management() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '公寓大廈管理'
      list['id'] = 'building-management'

      building_management = {}
      building_management['apartment-management'] = '公寓大廈管理'

      list['sub'] = building_management
      return list

# 保全消防 home-security
class HomeSecurity(object):
   def home_security() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '保全消防'
      list['id'] = 'home-security'

      home_security = {}
      home_security['fire-equipment'] = '消防設備'
      home_security['security-equipment'] = '安全設備用品'
      home_security['security-equip-alarm-system'] = '保全監視系統'

      list['sub'] = home_security
      return list

# 家具賣場 furniture
class Furniture(object):
   def furniture() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '家具賣場'
      list['id'] = 'furniture'

      furniture = {}
      furniture['furniture-stores'] = '家具賣場'

      list['sub'] = furniture
      return list

# 家具燈飾 furniture-and-light
class FurnitureAndLight(object):
   def furniture_and_light() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '家具燈飾'
      list['id'] = 'furniture-and-light'

      furniture_and_light = {}
      furniture_and_light['lightings'] = '燈飾'
      furniture_and_light['outdoor-furniture'] = '戶外休閒家具'
      furniture_and_light['furniture-repairs'] = '家具維修'
      furniture_and_light['antique-furniture'] = '古董家具'
      furniture_and_light['secondhand-furniture'] = '中古家具'
      furniture_and_light['furniture-designs'] = '家具設計'
      furniture_and_light['kids-furniture'] = '兒童家具'
      furniture_and_light['bamboo-rattan-furniture'] = '竹、籐家具'
      furniture_and_light['metal-furniture'] = '金屬家具'
      furniture_and_light['furniture'] = '家具'

      list['sub'] = furniture_and_light
      return list

# 家飾寢具 bedding-and-mattress
class BeddingAndMattress(object):
   def bedding_and_mattress() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '家飾寢具'
      list['id'] = 'bedding-and-mattress'

      bedding_and_mattress = {}
      bedding_and_mattress['table-clothes'] = '桌巾、餐墊'
      bedding_and_mattress['bedding-blankets'] = '寢具、被毯'
      bedding_and_mattress['beds'] = '床'
      bedding_and_mattress['curtains-blinds'] = '窗簾、百葉窗'
      bedding_and_mattress['carpets'] = '地毯'

      list['sub'] = bedding_and_mattress
      return list

# 園藝 horticultural
class Horticultural(object):
   def horticultural() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '園藝'
      list['id'] = 'horticultural'

      horticultural = {}
      horticultural['florists'] = '花店'
      horticultural['landscape'] = '園藝設計工程'
      horticultural['garden-nursery'] = '花圃、苗圃'
      horticultural['garden-supplies'] = '園藝器具資材'

      list['sub'] = horticultural
      return list

# 住屋居家 housing
class Housing(BaseCategory, ConstructionEngineering, BuildingMaterials, BuildingModel, DecorationWorks, 
AirConditioningEngineering, EngineeringTesting, WaterproofEngineering, BathroomSupplies, KitchenAppliances, 
LiftingEquipment, BuildingManagement, HomeSecurity, Furniture, FurnitureAndLight, BeddingAndMattress,
Horticultural):
   category_name = '住屋居家'
   category_id = 'housing'
