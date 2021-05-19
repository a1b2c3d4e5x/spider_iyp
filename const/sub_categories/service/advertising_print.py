from typing import Dict
from ..base_category import BaseCategory

# 廣告招牌 signboards
class Signboards(object):
   def signboards() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '廣告招牌'
      list['id'] = 'signboards'

      signboards = {}
      signboards['signboards'] = '招牌'
      signboards['flags'] = '旗幟'
      signboards['ads'] = '廣告'
      signboards['venue-decoration'] = '會場佈置'
      signboards['neon-equipment'] = '霓虹燈'
      signboards['posters'] = '海報'

      list['sub'] = signboards
      return list

# 商標標籤 label
class Label(object):
   def label() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '商標標籤'
      list['id'] = 'label'

      label = {}
      label['logo'] = '商標'
      label['label'] = '標籤'
      label['anti-counterfeit'] = '防偽技術產品'

      list['sub'] = label
      return list

# 印刷排版裝訂 printing-and-binding
class PrintingAndBinding(object):
   def printing_and_binding() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '印刷排版裝訂'
      list['id'] = 'printing-and-binding'

      printing_and_binding = {}
      printing_and_binding['printing-materials'] = '印刷材料'
      printing_and_binding['printing'] = '印刷'
      printing_and_binding['typist'] = '打字行'
      printing_and_binding['blueprint'] = '晒圖'
      printing_and_binding['typeset'] = '排版'
      printing_and_binding['binding'] = '裝訂'
      printing_and_binding['plate-making'] = '製版'
      printing_and_binding['card-making'] = '製卡'
      printing_and_binding['equipment'] = '印刷器材'

      list['sub'] = printing_and_binding
      return list

# 刻印鑄字 seal-carving-service
class SealCarvingService(object):
   def seal_carving_service() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '刻印鑄字'
      list['id'] = 'seal-carving-service'

      seal_carving_service = {}
      seal_carving_service['stamps'] = '印章'
      seal_carving_service['craving'] = '鑄字、刻字'

      list['sub'] = seal_carving_service
      return list

# 美工設計及用品 graphic-supplies
class GraphicSupplies(object):
   def graphic_supplies() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '美工設計及用品'
      list['id'] = 'graphic-supplies'

      graphic_supplies = {}
      graphic_supplies['commercial-industrial-design'] = '工業設計'
      graphic_supplies['supplies'] = '美工用品'

      list['sub'] = graphic_supplies
      return list

# 模型 model
class Model(object):
   def model() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '模型'
      list['id'] = 'model'

      model = {}
      model['display'] = '陳列設計'
      model['manufacture'] = '模型製造'

      list['sub'] = model
      return list

# 廣告印刷 advertising-print
class AdvertisingPrint(BaseCategory, Signboards, Label, PrintingAndBinding, SealCarvingService,
GraphicSupplies, Model):
   category_name = '廣告印刷'
   category_id = 'advertising-print'