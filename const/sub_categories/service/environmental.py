from typing import Dict
from ..base_category import BaseCategory

# 自然環境保護組織 environmental-protection
class EnvironmentalProtection(object):
   def environmental_protection() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '自然環境保護組織'
      list['id'] = 'environmental-protection'

      environmental_protection = {}
      environmental_protection['environmental-organization'] = '環保組織'

      list['sub'] = environmental_protection
      return list

# 污染防治 pollution-control
class PollutionControl(object):
   def pollution_control() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '污染防治'
      list['id'] = 'pollution-control'

      pollution_control = {}
      pollution_control['oil-pollution-odor-control'] = '油污、異味防治'
      pollution_control['pollution-treatment-equip'] = '污染處理設備'
      pollution_control['noise-controls'] = '噪音防治'
      pollution_control['air-pollution'] = '空氣污染'
      pollution_control['sewage-treatment'] = '污水處理'

      list['sub'] = pollution_control
      return list

# 病媒防治 vector-control
class VectorControl(object):
   def vector_control() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '病媒防治'
      list['id'] = 'vector-control'

      vector_control = {}
      vector_control['pest-controls'] = '蟲害防治'

      list['sub'] = vector_control
      return list

# 清潔消毒服務 disinfection-services
class DisinfectionServices(object):
   def disinfection_services() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '清潔消毒服務'
      list['id'] = 'disinfection-services'

      disinfection_services = {}
      disinfection_services['waste-collections'] = '垃圾清運'
      disinfection_services['cleaning-service'] = '清潔服務'

      list['sub'] = disinfection_services
      return list

# 清潔設備及用品 cleaning-supplies
class CleaningSupplies(object):
   def cleaning_supplies() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '清潔設備及用品'
      list['id'] = 'cleaning-supplies'

      cleaning_supplies = {}
      cleaning_supplies['cleaning-supplies'] = '清潔用品'

      list['sub'] = cleaning_supplies
      return list

# 焚化設備 incineration-equipment
class IncinerationEquipment(object):
   def incineration_equipment() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '焚化設備'
      list['id'] = 'incineration-equipment'

      incineration_equipment = {}
      incineration_equipment['incineration-equipment'] = '焚化設備'

      list['sub'] = incineration_equipment
      return list

# 資源回收及再生 recycling-service
class RecyclingService(object):
   def recycling_service() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '資源回收及再生'
      list['id'] = 'recycling-service'

      recycling_service = {}
      recycling_service['recycles'] = '資源回收'

      list['sub'] = recycling_service
      return list

# 廢棄物處理 cleanup
class Cleanup(object):
   def cleanup() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '廢棄物處理'
      list['id'] = 'cleanup'

      cleanup = {}
      cleanup['waste-medical-goods'] = '醫療廢棄物'
      cleanup['waste-air-treatment'] = '廢氣處理'
      cleanup['waste-disposal'] = '廢棄物處理'
      cleanup['waste-water-treatment'] = '廢水處理'
      cleanup['waste-soil-treatment'] = '廢土處理'

      list['sub'] = cleanup
      return list

# 流動廁所－出租 mobile-toilets
class MobileToilets(object):
   def mobile_toilets() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '流動廁所－出租'
      list['id'] = 'mobile-toilets'

      mobile_toilets = {}
      mobile_toilets['mobile-toilets'] = '流動廁所'

      list['sub'] = mobile_toilets
      return list

# 環境保護 environmental
class Environmental(BaseCategory, EnvironmentalProtection, PollutionControl, VectorControl,
DisinfectionServices, CleaningSupplies, IncinerationEquipment, RecyclingService, Cleanup, 
MobileToilets):
   category_name = '環境保護'
   category_id = 'environmental'