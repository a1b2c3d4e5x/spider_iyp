from typing import Dict
from ..base_category import BaseCategory

# 家用電器 appliances
class Appliances(object):
   def appliances() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '家用電器'
      list['id'] = 'appliances'

      appliances = {}
      appliances['secondhand'] = '二手家電'
      appliances['repair'] = '家電維修'
      appliances['appliances'] = '家電'
      appliances['refrigerators'] = '冰箱'
      appliances['air-conditioners'] = '冷氣'
      appliances['TV'] = '電視機'
      appliances['VCR'] = '錄放影機'
      appliances['audio-equipment'] = '音響'
      appliances['radio-recorders'] = '錄音機'
      appliances['hair-dryers'] = '吹風機'
      appliances['dehumidifiers'] = '除濕機'
      appliances['kitchen'] = '廚房家電'
      appliances['washing-machines-dryers'] = '洗衣機、烘衣機'
      appliances['water-filters'] = '飲水機'
      appliances['vacuums'] = '吸塵器'
      appliances['fans'] = '電風扇'
      appliances['heaters'] = '電暖器、電熱器'
      appliances['sewing-machines'] = '縫紉機'

      list['sub'] = appliances
      return list

# 家用電器 appliances
class Appliances(BaseCategory, Appliances):
   category_name = '家用電器'
   category_id = 'appliances'