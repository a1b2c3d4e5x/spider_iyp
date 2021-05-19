from typing import Dict
from ..base_category import BaseCategory

# 包裝及設計 packaging
class Packaging(object):
   def packaging() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '包裝及設計'
      list['id'] = 'packaging'

      packaging = {}
      packaging['design'] = '包裝設計'
      packaging['service'] = '包裝服務'

      list['sub'] = packaging
      return list

# 包裝容器 containers
class Containers(object):
   def containers() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '包裝容器'
      list['id'] = 'containers'

      containers = {}
      containers['plastic-bags'] = '塑膠袋'
      containers['containers'] = '容器'
      containers['paper-containers'] = '紙質容器'
      containers['glass-containers'] = '玻璃容器'
      containers['plastic-containers'] = '塑膠容器'
      containers['metal-containers'] = '金屬容器'
      containers['wooden-containers'] = '木質容器'

      list['sub'] = containers
      return list

# 包裝材料 packaging-materials
class PackagingMaterials(object):
   def packaging_materials() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '包裝材料'
      list['id'] = 'packaging-materials'

      packaging_materials = {}
      packaging_materials['materials'] = '包裝材料'
      packaging_materials['cork'] = '軟木製品'

      list['sub'] = packaging_materials
      return list

# 包裝機器及工具 packaging-machinery
class PackagingMachinery(object):
   def packaging_machinery() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '包裝機器及工具'
      list['id'] = 'packaging-machinery'

      packaging_machinery = {}
      packaging_machinery['equipment'] = '包裝機'

      list['sub'] = packaging_machinery
      return list

# 包裝服務 packaging-service
class PackagingService(BaseCategory, Packaging, Containers, PackagingMaterials, PackagingMachinery):
   category_name = '包裝服務'
   category_id = 'packaging-service'