from typing import Dict
from ..base_category import BaseCategory

# 金屬基本工業 basic-metal-industries
class BasicMetalIndustries(object):
   def basic_metal_industries() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '金屬基本工業'
      list['id'] = 'basic-metal-industries'

      basic_metal_industries = {}
      basic_metal_industries['stainless-steel-materials'] = '不銹鋼材料'
      basic_metal_industries['stainless-steel-products'] = '不銹鋼製品'
      basic_metal_industries['angle-steel'] = '角鋼'
      basic_metal_industries['non-ferrous-metal-products'] = '非鐵金屬'
      basic_metal_industries['copper-products'] = '銅及銅製品'
      basic_metal_industries['aluminum-products'] = '鋁及鋁製品'
      basic_metal_industries['steel'] = '鋼鐵'
      basic_metal_industries['tin-products'] = '錫及錫製品'

      list['sub'] = basic_metal_industries
      return list

# 金屬工具 metal-tool
class MetalTool(object):
   def metal_tool() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '金屬工具'
      list['id'] = 'metal-tool'

      metal_tool = {}
      metal_tool['cutlery'] = '刀、剪刀'
      metal_tool['tools'] = '工具'
      metal_tool['cutting-tools'] = '切削工具'
      metal_tool['hand-tools'] = '手工具'
      metal_tool['air-tools'] = '氣動工具'
      metal_tool['grinding-tools'] = '研磨工具'
      metal_tool['power-tools'] = '電動工具'
      metal_tool['trolleys'] = '手推車'

      list['sub'] = metal_tool
      return list

# 金屬模具 metal-mold
class MetalMold(object):
   def metal_mold() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '金屬模具'
      list['id'] = 'metal-mold'

      metal_mold = {}
      metal_mold['moldings'] = '模具'
      metal_mold['press'] = '沖壓模具'
      metal_mold['plastic'] = '塑膠模具'
      metal_mold['die-casting'] = '壓鑄模具'
      metal_mold['forging'] = '鍛造模具'
      metal_mold['casting'] = '鑄造模具'

      list['sub'] = metal_mold
      return list

# 五金製品 hardware
class Hardware(object):
   def hardware() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '五金製品'
      list['id'] = 'hardware'

      hardware = {}
      hardware['valves'] = '凡而、考克'
      hardware['tinplate'] = '馬口鐵'
      hardware['marine-hardware'] = '船舶五金'
      hardware['locks'] = '鎖類五金'
      hardware['steel-products'] = '鋼'
      hardware['hardware-manufacturers'] = '五金製造'
      hardware['hardware'] = '五金製品'

      list['sub'] = hardware
      return list

# 金屬冶煉鍛鑄 malleable-metal-smelting
class MalleableMetalSmelting(object):
   def malleable_metal_smelting() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '金屬冶煉鍛鑄'
      list['id'] = 'malleable-metal-smelting'

      malleable_metal_smelting = {}
      malleable_metal_smelting['metal-smelting'] = '金屬冶煉'
      malleable_metal_smelting['extrusion-rolling-pressure'] = '金屬擠壓、軋壓'
      malleable_metal_smelting['metal-cutting'] = '金屬切割'
      malleable_metal_smelting['powder-metallurgy'] = '粉末冶金'
      malleable_metal_smelting['alloy'] = '合金'
      malleable_metal_smelting['die-casting'] = '壓鑄'
      malleable_metal_smelting['forging'] = '鍛造'
      malleable_metal_smelting['casting'] = '鑄造'
      malleable_metal_smelting['ironware-casting'] = '鐵器、鑄件'

      list['sub'] = malleable_metal_smelting
      return list

# 金屬表面處理 metal-surface-treatment
class MetalSurfaceTreatment(object):
   def metal_surface_treatment() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '金屬表面處理'
      list['id'] = 'metal-surface-treatment'

      metal_surface_treatment = {}
      metal_surface_treatment['heat-treatment'] = '熱處理'
      metal_surface_treatment['plating'] = '電鍍'
      metal_surface_treatment['welding'] = '電焊'
      metal_surface_treatment['painting-spraying'] = '塗裝、噴漆'
      metal_surface_treatment['surface-treatment'] = '表面處理'

      list['sub'] = metal_surface_treatment
      return list

# 廢五金 scrap
class Scrap(object):
   def scrap() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '廢五金'
      list['id'] = 'scrap'

      scrap = {}
      scrap['scrap'] = '五金廢料'

      list['sub'] = scrap
      return list

# 金屬工業 metal-industry
class MetalIndustry(BaseCategory, BasicMetalIndustries, MetalTool, MetalMold, Hardware, MalleableMetalSmelting, 
MetalSurfaceTreatment, Scrap):
   category_name = '金屬工業'
   category_id = 'metal-industry'