from typing import Dict
from ..base_category import BaseCategory

# 自動化設備 automation
class Automation(object):
   def automation() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '自動化設備'
      list['id'] = 'automation'

      automation = {}
      automation['automation-machinery'] = '自動化機械'
      automation['robots'] = '機器人設備'
      automation['auto-storage-system'] = '自動倉儲系統'

      list['sub'] = automation
      return list

# 工具機 machining-centers
class MachiningCenters(object):
   def machining_centers() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '工具機'
      list['id'] = 'machining-centers'

      machining_centers = {}
      machining_centers['machine-tools'] = '工作母機'
      machining_centers['cutting-machinery'] = '金屬切削工具機'
      machining_centers['forming-machinery'] = '金屬成型工具機'

      list['sub'] = machining_centers
      return list

# 農業機械及裝備 agricultural-machinery
class AgriculturalMachinery(object):
   def agricultural_machinery() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '農業機械及裝備'
      list['id'] = 'agricultural-machinery'

      agricultural_machinery = {}
      agricultural_machinery['agriculture-machinery'] = '農機設備'

      list['sub'] = agricultural_machinery
      return list

# 食品及製藥機械 pharmaceutical-machinery
class PharmaceuticalMachinery(object):
   def pharmaceutical_machinery() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '食品及製藥機械'
      list['id'] = 'pharmaceutical-machinery'

      pharmaceutical_machinery = {}
      pharmaceutical_machinery['food-manufacturing-machinery'] = '食品製造機械'
      pharmaceutical_machinery['pharmaceutical-machinery'] = '製藥機械'

      list['sub'] = pharmaceutical_machinery
      return list

# 紡織製衣機械 textile-machine
class TextileMachine(object):
   def textile_machine() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '紡織製衣機械'
      list['id'] = 'textile-machine'

      textile_machine = {}
      textile_machine['textile-machinery'] = '紡織機械'
      textile_machine['apparel-machinery'] = '製衣機械'

      list['sub'] = textile_machine
      return list

# 營建機械及裝備 construction-machinery
class ConstructionMachinery(object):
   def construction_machinery() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '營建機械及裝備'
      list['id'] = 'construction-machinery'

      construction_machinery = {}
      construction_machinery['construction-machinery'] = '營建機械'

      list['sub'] = construction_machinery
      return list

# 木工機械 woodworking-machinery
class WoodworkingMachinery(object):
   def woodworking_machinery() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '木工機械'
      list['id'] = 'woodworking-machinery'

      woodworking_machinery = {}
      woodworking_machinery['woodworking-machinery'] = '木工機械'

      list['sub'] = woodworking_machinery
      return list

# 化工機械 chemical-machinery
class ChemicalMachinery(object):
   def chemical_machinery() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '化工機械'
      list['id'] = 'chemical-machinery'

      chemical_machinery = {}
      chemical_machinery['chemical-machinery'] = '化工機械'

      list['sub'] = chemical_machinery
      return list

# 塑膠及橡膠機械 plastics-and-rubber-machinery
class PlasticsAndRubberMachinery(object):
   def plastics_and_rubber_machinery() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '塑膠及橡膠機械'
      list['id'] = 'plastics-and-rubber-machinery'

      plastics_and_rubber_machinery = {}
      plastics_and_rubber_machinery['plastic-forming-machinery'] = '塑膠成型機'
      plastics_and_rubber_machinery['rubber-machinery'] = '橡膠機械'

      list['sub'] = plastics_and_rubber_machinery
      return list

# 印刷機械 printing-machinery
class PrintingMachinery(object):
   def printing_machinery() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '印刷機械'
      list['id'] = 'printing-machinery'

      printing_machinery = {}
      printing_machinery['printing-machinery'] = '印刷機械'
      printing_machinery['hot-stamping-machinery'] = '燙金機械'

      list['sub'] = printing_machinery
      return list

# 製鞋及皮革機械 shoe-and-leather-machinery
class ShoeAndLeatherMachinery(object):
   def shoe_and_leather_machinery() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '製鞋及皮革機械'
      list['id'] = 'shoe-and-leather-machinery'

      shoe_and_leather_machinery = {}
      shoe_and_leather_machinery['leather-processing-machines'] = '皮革加工機械'
      shoe_and_leather_machinery['shoes-making-machines'] = '製鞋機械'

      list['sub'] = shoe_and_leather_machinery
      return list

# 輸送及物流設備 transportation-and-logistics
class TransportationAndLogistics(object):
   def transportation_and_logistics() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '輸送及物流設備'
      list['id'] = 'transportation-and-logistics'

      transportation_and_logistics = {}
      transportation_and_logistics['conveyors'] = '輸送設備'
      transportation_and_logistics['cranes'] = '吊車天車'

      list['sub'] = transportation_and_logistics
      return list

# 表面處理機械 surface-treatment-machinery
class SurfaceTreatmentMachinery(object):
   def surface_treatment_machinery() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '表面處理機械'
      list['id'] = 'surface-treatment-machinery'

      surface_treatment_machinery = {}
      surface_treatment_machinery['painting-equip'] = '塗裝機械'
      surface_treatment_machinery['plating-equip'] = '電鍍機械'

      list['sub'] = surface_treatment_machinery
      return list

# 工業用爐及鍋爐 industrial-furnaces-and-boilers
class IndustrialFurnacesAndBoilers(object):
   def industrial_furnaces_and_boilers() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '工業用爐及鍋爐'
      list['id'] = 'industrial-furnaces-and-boilers'

      industrial_furnaces_and_boilers = {}
      industrial_furnaces_and_boilers['furnace'] = '工業用爐'

      list['sub'] = industrial_furnaces_and_boilers
      return list

# 空油壓設備 air-hydraulic-equipment
class AirHydraulicEquipment(object):
   def air_hydraulic_equipment() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '空油壓設備'
      list['id'] = 'air-hydraulic-equipment'

      air_hydraulic_equipment = {}
      air_hydraulic_equipment['air-hydraulic-machinery'] = '空油壓機械'
      air_hydraulic_equipment['marine-equip'] = '船用設備'
      air_hydraulic_equipment['crushing-equip'] = '粉碎機'

      list['sub'] = air_hydraulic_equipment
      return list

# 其它機械裝備 machinery-and-equipment
class MachineryAndEquipment(object):
   def machinery_and_equipment() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '其它機械裝備'
      list['id'] = 'machinery-and-equipment'

      machinery_and_equipment = {}
      machinery_and_equipment['machine-processing'] = '機械加工'
      machinery_and_equipment['hardware-machines'] = '五金製品機械'
      machinery_and_equipment['die-casting-machine'] = '壓鑄機'
      machinery_and_equipment['water-cooler'] = '水冷器'
      machinery_and_equipment['vending-machines'] = '自動販賣機'
      machinery_and_equipment['laundry-machine'] = '洗衣機'
      machinery_and_equipment['glass-manufacturing-machines'] = '玻璃製作機器'
      machinery_and_equipment['grinders'] = '砂輪機'
      machinery_and_equipment['paper-machines'] = '造紙機械'
      machinery_and_equipment['dryers'] = '乾燥機'
      machinery_and_equipment['mixers-blenders'] = '攪拌機'
      machinery_and_equipment['grinding-machine'] = '研磨機'
      machinery_and_equipment['ultrasonic-equipment'] = '超音波'
      machinery_and_equipment['game-room-equip'] = '遊戲機'
      machinery_and_equipment['car-washing-machines'] = '洗車機'
      machinery_and_equipment['wire-cable-equipment'] = '電線電纜'
      machinery_and_equipment['feeder'] = '飼料機'
      machinery_and_equipment['heat-exchange-equip'] = '熱交換器'
      machinery_and_equipment['burner'] = '燃燒機'
      machinery_and_equipment['light-manufacturing-equip'] = '燈泡機械'
      machinery_and_equipment['oil-well-drilling-equip'] = '油井探採設備'
      machinery_and_equipment['casting-machinery'] = '鑄造機械'
      machinery_and_equipment['extracting-machinery-equipment'] = '萃取機械及設備'
      machinery_and_equipment['industrial-water-chiller'] = '冰水機'

      list['sub'] = machinery_and_equipment
      return list

# 整廠設備 plant-equipment
class PlantEquipment(object):
   def plant_equipment() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '整廠設備'
      list['id'] = 'plant-equipment'

      plant_equipment = {}
      plant_equipment['turn-key-plants'] = '整廠設備'

      list['sub'] = plant_equipment
      return list

# 公害處理設備 pollution-treatment-equipment
class PollutionTreatmentEquipment(object):
   def pollution_treatment_equipment() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '公害處理設備'
      list['id'] = 'pollution-treatment-equipment'

      pollution_treatment_equipment = {}
      pollution_treatment_equipment['dust-collection-equip'] = '集塵吸塵設備'
      pollution_treatment_equipment['filter-equip'] = '過濾設備'

      list['sub'] = pollution_treatment_equipment
      return list

# 機械零組件 mechanical-components
class MechanicalComponents(object):
   def mechanical_components() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '機械零組件'
      list['id'] = 'mechanical-components'

      mechanical_components = {}
      mechanical_components['machinery-accessaries'] = '機械零配件'
      mechanical_components['decelerator-transmission'] = '減速機、變速機'

      list['sub'] = mechanical_components
      return list

# 工業設備 industrial-equipment
class IndustrialEquipment(object):
   def industrial_equipment() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '工業設備'
      list['id'] = 'industrial-equipment'

      industrial_equipment = {}
      industrial_equipment['industrial-safety-equip'] = '工業安全器材'
      industrial_equipment['industrial-equip'] = '工業設備'

      list['sub'] = industrial_equipment
      return list

# 工業機械 industrial-machinery
class IndustrialMachinery(BaseCategory, Automation, MachiningCenters, AgriculturalMachinery, 
PharmaceuticalMachinery, TextileMachine, ConstructionMachinery, WoodworkingMachinery, 
ChemicalMachinery, PlasticsAndRubberMachinery, PrintingMachinery, ShoeAndLeatherMachinery, 
TransportationAndLogistics, SurfaceTreatmentMachinery, IndustrialFurnacesAndBoilers, 
AirHydraulicEquipment, MachineryAndEquipment, PlantEquipment, PollutionTreatmentEquipment, 
MechanicalComponents, IndustrialEquipment):
   category_name = '工業機械'
   category_id = 'industrial-machinery'