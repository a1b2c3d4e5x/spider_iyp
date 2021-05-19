from typing import Dict
from ..base_category import BaseCategory

# 冷凍空調設備 air-conditioning-supplies
class AirConditioningSupplies(object):
   def air_conditioning_supplies() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '冷凍空調設備'
      list['id'] = 'air-conditioning-supplies'

      air_conditioning_supplies = {}
      air_conditioning_supplies['freezers'] = '冷凍設備'
      air_conditioning_supplies['air-conditioning-equip'] = '空調設備'
      air_conditioning_supplies['dehumidification-systems'] = '除濕系統'

      list['sub'] = air_conditioning_supplies
      return list

# 電子及零件產品 electrical-materials
class ElectricalMaterials(object):
   def electrical_materials() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '電子及零件產品'
      list['id'] = 'electrical-materials'

      electrical_materials = {}
      electrical_materials['semiconductor-device'] = '半導體'
      electrical_materials['semiconductor-materials'] = '半導體材料'
      electrical_materials['optoelectronics'] = '光電產品'
      electrical_materials['PCB'] = '印刷電路板'
      electrical_materials['electronics'] = '電子產品'
      electrical_materials['electronic-parts'] = '電子零件'
      electrical_materials['electronics-electrical-instruments'] = '電子、電工儀器'
      electrical_materials['magnets'] = '磁鐵'
      electrical_materials['electronics-manufacturing-equip'] = '電子產品製造設備'

      list['sub'] = electrical_materials
      return list

# 電力系統材料設備 power-system-supplies
class PowerSystemSupplies(object):
   def power_system_supplies() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '電力系統材料設備'
      list['id'] = 'power-system-supplies'

      power_system_supplies = {}
      power_system_supplies['fuses'] = '保險絲'
      power_system_supplies['electric-boxes-panels'] = '配電盤'
      power_system_supplies['wiring-accessories'] = '配線器材'
      power_system_supplies['connectors'] = '連接器'
      power_system_supplies['plugs-sockets'] = '插頭、插座'
      power_system_supplies['switches'] = '開關'
      power_system_supplies['resistors-capacitors'] = '電阻、電容'
      power_system_supplies['wire-cable'] = '電線、電纜'
      power_system_supplies['charger'] = '變壓器、充電器'
      power_system_supplies['electric-supplies'] = '電器材料'
      power_system_supplies['rectifiers'] = '整流器調整器'
      power_system_supplies['adapters'] = '轉接器'
      power_system_supplies['regulators'] = '穩壓器'
      power_system_supplies['inverter'] = '變頻器'

      list['sub'] = power_system_supplies
      return list

# 馬達幫浦發電機 pump-motor-generator
class PumpMotorGenerator(object):
   def pump_motor_generator() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '馬達幫浦發電機'
      list['id'] = 'pump-motor-generator'

      pump_motor_generator = {}
      pump_motor_generator['water-pump'] = '抽水機、 幫浦'
      pump_motor_generator['pumping-fans'] = '抽送風機'
      pump_motor_generator['motors'] = '馬達'
      pump_motor_generator['power-generators'] = '發電機'
      pump_motor_generator['compressors'] = '壓縮機'

      list['sub'] = pump_motor_generator
      return list

# 燈具照明系統 lighting-system
class LightingSystem(object):
   def lighting_system() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '燈具照明系統'
      list['id'] = 'lighting-system'

      lighting_system = {}
      lighting_system['lightings'] = '燈具'
      lighting_system['lighting-systems'] = '照明'

      list['sub'] = lighting_system
      return list

# 電池 batteries
class Batteries(object):
   def batteries() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '電池'
      list['id'] = 'batteries'

      batteries = {}
      batteries['battery-manufacturers'] = '電池製造'
      batteries['batteries'] = '電池'

      list['sub'] = batteries
      return list

# 熔接焊接電熱 electric-welding-service
class ElectricWeldingService(object):
   def electric_welding_service() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '熔接焊接電熱'
      list['id'] = 'electric-welding-service'

      electric_welding_service = {}
      electric_welding_service['electric-heating'] = '電熱'
      electric_welding_service['welding-service'] = '熔接、焊接'

      list['sub'] = electric_welding_service
      return list

# 電工器材 electrical-material
class ElectricalMaterial(BaseCategory, AirConditioningSupplies, ElectricalMaterials, PowerSystemSupplies,
PumpMotorGenerator, LightingSystem, Batteries, ElectricWeldingService):
   category_name = '電工器材'
   category_id = 'electrical-material'