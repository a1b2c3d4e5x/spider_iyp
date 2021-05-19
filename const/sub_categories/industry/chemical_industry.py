from typing import Dict
from ..base_category import BaseCategory

# 化工及石化原料 petrochemical-materials
class PetrochemicalMaterials(object):
   def petrochemical_materials() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '化工及石化原料'
      list['id'] = 'petrochemical-materials'

      petrochemical_materials = {}
      petrochemical_materials['man-made-fiber-materials'] = '人造纖維原料'
      petrochemical_materials['chemical-materials'] = '化工原料'
      petrochemical_materials['glass-fiber-materials'] = '玻璃纖維原料'
      petrochemical_materials['petrochemical-materials'] = '石化原料'
      petrochemical_materials['starch'] = '澱粉'
      petrochemical_materials['chemical-products'] = '化學'
      petrochemical_materials['plastic-waste'] = '塑膠廢料'

      list['sub'] = petrochemical_materials
      return list

# 石化產品 petrochemicals
class Petrochemicals(object):
   def petrochemicals() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '石化產品'
      list['id'] = 'petrochemicals'

      petrochemicals = {}
      petrochemicals['synthetic-leather'] = '合成皮'
      petrochemicals['foams-sponges'] = '海綿、泡綿'
      petrochemicals['glass-fiber-products'] = '玻璃纖維製品'
      petrochemicals['acrylic-products'] = '壓克力'
      petrochemicals['wax'] = '蠟'

      list['sub'] = petrochemicals
      return list

# 油品 oil
class Oil(object):
   def oil() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '油品'
      list['id'] = 'oil'

      oil = {}
      oil['petroleum'] = '油'
      oil['transportation-equip'] = '油品儲運設備'

      list['sub'] = oil
      return list

# 瓦斯業 gas-service
class GasService(object):
   def gas_service() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '瓦斯業'
      list['id'] = 'gas-service'

      gas_service = {}
      gas_service['gas'] = '瓦斯業'

      list['sub'] = gas_service
      return list

# 中間體 intermediate
class Intermediate(object):
   def intermediate() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '中間體'
      list['id'] = 'intermediate'

      intermediate = {}
      intermediate['aromatizer'] = '香精、香料'
      intermediate['intermediate'] = '中間體'
      intermediate['abrasive'] = '磨料'
      intermediate['camphor'] = '樟腦'

      list['sub'] = intermediate
      return list

# 玻璃 glass
class Glass(object):
   def glass() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '玻璃'
      list['id'] = 'glass'

      glass = {}
      glass['glass-manufacturers'] = '玻璃製造'
      glass['glass'] = '玻璃'

      list['sub'] = glass
      return list

# 氣體 gas
class Gas(object):
   def gas() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '氣體'
      list['id'] = 'gas'

      gas = {}
      gas['gas'] = '氣體'

      list['sub'] = gas
      return list

# 農藥品 pesticides
class Pesticides(object):
   def pesticides() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '農藥品'
      list['id'] = 'pesticides'

      pesticides = {}
      pesticides['pesticide'] = '農藥'

      list['sub'] = pesticides
      return list

# 消毒殺蟲藥劑 insecticide
class Insecticide(object):
   def insecticide() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '消毒殺蟲藥劑'
      list['id'] = 'insecticide'

      insecticide = {}
      insecticide['insecticide'] = '殺蟲劑'
      insecticide['disinfectant-cleaner'] = '消毒清潔劑'

      list['sub'] = insecticide
      return list

# 紙品 paper
class Paper(object):
   def paper() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '紙品'
      list['id'] = 'paper'

      paper = {}
      paper['papermaking-pulp'] = '造紙、紙漿'
      paper['paper-processing'] = '紙品加工'
      paper['papers'] = '紙'
      paper['industrial-paper'] = '工業用紙'
      paper['packaging-papers'] = '包裝紙'
      paper['cultural-papers'] = '文化用紙'
      paper['household-papers'] = '家庭用紙'

      list['sub'] = paper
      return list

# 塑膠橡膠 plastics-and-rubber
class PlasticsAndRubber(object):
   def plastics_and_rubber() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '塑膠橡膠'
      list['id'] = 'plastics-and-rubber'

      plastics_and_rubber = {}
      plastics_and_rubber['plastic-material'] = '塑膠原料'
      plastics_and_rubber['plastic-additives-color-agent'] = '塑膠添加劑'
      plastics_and_rubber['plastic-products'] = '塑膠製品'
      plastics_and_rubber['plastic-processing'] = '塑膠模型'
      plastics_and_rubber['rubber-materials'] = '橡膠原料'
      plastics_and_rubber['rubber-additive'] = '橡膠添加劑'
      plastics_and_rubber['rubber-products'] = '橡膠製品'

      list['sub'] = plastics_and_rubber
      return list

# 塗料染料 paint-and-dye
class PaintAndDye(object):
   def paint_and_dye() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '塗料染料'
      list['id'] = 'paint-and-dye'

      paint_and_dye = {}
      paint_and_dye['paint-coating'] = '油漆、塗料'
      paint_and_dye['pigment-dyestuff'] = '顏料、色料、染料'
      paint_and_dye['coating-service'] = '塗膠服務'

      list['sub'] = paint_and_dye
      return list

# 溶劑黏劑 solvent-and-adhesives
class SolventAndAdhesives(object):
   def solvent_and_adhesives() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '溶劑黏劑'
      list['id'] = 'solvent-and-adhesives'

      solvent_and_adhesives = {}
      solvent_and_adhesives['solvent'] = '溶劑'
      solvent_and_adhesives['adhesive'] = '樹脂'

      list['sub'] = solvent_and_adhesives
      return list

# 能源設備及產品 energy-products
class EnergyProducts(object):
   def energy_products() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '能源設備及產品'
      list['id'] = 'energy-products'

      energy_products = {}
      energy_products['energy-equip'] = '能源設備'

      list['sub'] = energy_products
      return list

# 化學工業 chemical-industry
class ChemicalIndustry(BaseCategory, PetrochemicalMaterials, Petrochemicals, Oil, GasService, Intermediate, 
Glass, Gas, Pesticides, Insecticide, Paper, PlasticsAndRubber, PaintAndDye, SolventAndAdhesives, EnergyProducts):
   category_name = '化學工業'
   category_id = 'chemical-industry'