from typing import Dict
from ..base_category import BaseCategory

# 辦公事務器械及用品 office-supplies
class OfficeSupplies(object):
   def office_supplies() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '辦公事務器械及用品'
      list['id'] = 'office-supplies'

      office_supplies = {}
      office_supplies['office-service-machines'] = '辦公事務機'
      office_supplies['office-supplies'] = '辦公室用品'
      office_supplies['office-furniture-manufacturers'] = '辦公傢俱製造'

      list['sub'] = office_supplies
      return list

# 辦公室傢俱 office-furniture
class OfficeFurniture(object):
   def office_furniture() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '辦公室傢俱'
      list['id'] = 'office-furniture'

      office_furniture = {}
      office_furniture['office-furniture'] = '辦公傢俱'

      list['sub'] = office_furniture
      return list

# 文具 stationery
class Stationery(object):
   def stationery() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '文具'
      list['id'] = 'stationery'

      stationery = {}
      stationery['diaries-calendars'] = '工商日誌、月曆'
      stationery['stationaries-manufacturers'] = '文具製造'
      stationery['envelops-greeting-cards'] = '信封賀卡製造'
      stationery['stationaries'] = '文具'

      list['sub'] = stationery
      return list

# 教育用品 education-supply
class EducationSupply(object):
   def education_supply() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '教育用品'
      list['id'] = 'education-supply'

      education_supply = {}
      education_supply['school-supplies'] = '教育用品'
      education_supply['blackboards-whitebaords'] = '黑、白板'

      list['sub'] = education_supply
      return list

# 影印及護貝服務 printing-and-laminating-service
class PrintingAndLaminatingService(object):
   def printing_and_laminating_service() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '影印及護貝服務'
      list['id'] = 'printing-and-laminating-service'

      printing_and_laminating_service = {}
      printing_and_laminating_service['copy-service'] = '影印服務'
      printing_and_laminating_service['laminating-supplies'] = '護貝用品'

      list['sub'] = printing_and_laminating_service
      return list

# 事務文具 office-stationery
class OfficeStationery(BaseCategory, OfficeSupplies, OfficeFurniture, Stationery, EducationSupply, PrintingAndLaminatingService):
   category_name = '事務文具'
   category_id = 'office-stationery'