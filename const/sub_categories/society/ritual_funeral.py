from typing import Dict
from ..base_category import BaseCategory

# 殯儀服務 funeral-services
class FuneralServices(object):
   def funeral_services() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '殯儀服務'
      list['id'] = 'funeral-services'

      funeral_services = {}
      funeral_services['funeral-service'] = '殯葬服務'

      list['sub'] = funeral_services
      return list

# 墓園及墓地 cemetery-and-the-cemetery
class CemeteryAndTheCemetery(object):
   def cemetery_and_the_cemetery() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '墓園及墓地'
      list['id'] = 'cemetery-and-the-cemetery'

      cemetery_and_the_cemetery = {}
      cemetery_and_the_cemetery['ossuaries-cemeteries'] = '納骨塔、墓地'

      list['sub'] = cemetery_and_the_cemetery
      return list

# 香燭紙料 Incense-paper
class IncensePaper(object):
   def Incense_paper() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '香燭紙料'
      list['id'] = 'incense-paper'

      Incense_paper = {}
      Incense_paper['incense-papers'] = '香燭紙料'

      list['sub'] = Incense_paper
      return list

# 生命禮儀 ritual-funeral
class RitualFuneral(BaseCategory, FuneralServices, CemeteryAndTheCemetery, IncensePaper):
   category_name = '生命禮儀'
   category_id = 'ritual-funeral'