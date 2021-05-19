from typing import Dict
from ..base_category import BaseCategory

# 瓦斯服務 gas-services
class GasServices(object):
   def gas_services() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '瓦斯服務'
      list['id'] = 'gas-services'

      gas_services = {}
      gas_services['gas'] = '瓦斯服務'

      list['sub'] = gas_services
      return list

# 石油服務 petroleum-services
class PetroleumServices(object):
   def petroleum_services() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '石油服務'
      list['id'] = 'petroleum-services'

      petroleum_services = {}
      petroleum_services['petroleum'] = '石油服務'

      list['sub'] = petroleum_services
      return list

# 自來水服務 water-services
class WaterServices(object):
   def water_services() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '自來水服務'
      list['id'] = 'water-services'

      water_services = {}
      water_services['water'] = '自來水服務'

      list['sub'] = water_services
      return list

# 氣象服務 weather-services
class WeatherServices(object):
   def weather_services() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '氣象服務'
      list['id'] = 'weather-services'

      weather_services = {}
      weather_services['weather'] = '氣象服務'

      list['sub'] = weather_services
      return list

# 郵政服務 postal-services
class PostalServices(object):
   def postal_services() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '郵政服務'
      list['id'] = 'postal-services'

      postal_services = {}
      postal_services['post'] = '郵政服務'

      list['sub'] = postal_services
      return list

# 電力服務 electric-services
class ElectricServices(object):
   def electric_services() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '電力服務'
      list['id'] = 'electric-services'

      electric_services = {}
      electric_services['electricity'] = '電力服務'

      list['sub'] = electric_services
      return list

# 電信通信服務 telecommunication-services
class TelecommunicationServices(object):
   def telecommunication_services() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '電信通信服務'
      list['id'] = 'telecommunication-services'

      telecommunication_services = {}
      telecommunication_services['satellite'] = '衛星通信網路'
      telecommunication_services['landline'] = '固定通信網路'
      telecommunication_services['telecom'] = '電信服務'
      telecommunication_services['mobile'] = '行動通信網路'

      list['sub'] = telecommunication_services
      return list

# 外國使館機構 embassies
class Embassies(object):
   def embassies() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '外國使館機構'
      list['id'] = 'embassies'

      embassies = {}
      embassies['foreign-embassies-institutions'] = '外國使館機構'

      list['sub'] = embassies
      return list

# 消防 firefighter
class Firefighter(object):
   def firefighter() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '消防'
      list['id'] = 'firefighter'

      firefighter = {}
      firefighter['firefighter'] = '消防'

      list['sub'] = firefighter
      return list

# 憲警 military-police
class MilitaryPolice(object):
   def military_police() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '憲警'
      list['id'] = 'military-police'

      military_police = {}
      military_police['polices'] = '警察'
      military_police['military-police'] = '憲兵'

      list['sub'] = military_police
      return list

# 中央機關 central-authority
class CentralAuthority(object):
   def central_authority() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '中央機關'
      list['id'] = 'central-authority'

      central_authority = {}
      central_authority['personnel-administration'] = '人事行政局'
      central_authority['government-information-office'] = '行政院新聞局'
      central_authority['environmental-protection-administration'] = '行政院環保署'
      central_authority['department-of-health'] = '行政院衛生署'
      central_authority['DGBAS'] = '行政院主計處'
      central_authority['ministry-of-transportation-and-communications'] = '交通部'
      central_authority['ministry-of-justice'] = '法務部'
      central_authority['ministry-of-education'] = '教育部'
      central_authority['ministry-of-economic-affairs'] = '經濟部'
      central_authority['ministry-of-finance'] = '財政部'
      central_authority['ministry-of-national-defense'] = '國防部'
      central_authority['ministry-of-diplomacy'] = '外交部'
      central_authority['ministry-of-internal-affairs'] = '內政部'
      central_authority['executive-yuan-councils'] = '行政院委員會'
      central_authority['control-yuan'] = '監察院'
      central_authority['judicial-yuan'] = '司法院'
      central_authority['examination-yuan'] = '考試院'
      central_authority['office-of-president'] = '總統府'
      central_authority['legislative-yuan'] = '立法院'

      list['sub'] = central_authority
      return list

# 地方機關 local-authorities
class LocalAuthorities(object):
   def local_authorities() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '地方機關'
      list['id'] = 'local-authorities'

      local_authorities = {}
      local_authorities['village-office'] = '村里辦公室'
      local_authorities['city-council-township-representatives'] = '議會代表會'
      local_authorities['city-government'] = '縣市政府機關'

      list['sub'] = local_authorities
      return list

# 公用事業 utilities
class Utilities(BaseCategory, GasServices, PetroleumServices, WaterServices, WeatherServices, 
PostalServices, ElectricServices, TelecommunicationServices, Embassies, Firefighter, MilitaryPolice,
CentralAuthority, LocalAuthorities):
   category_name = '公用事業'
   category_id = 'utilities'