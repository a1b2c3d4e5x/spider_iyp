from typing import Dict
from ..base_category import BaseCategory

# 行動通信服務 mobile-service
class MobileService(object):
   def mobile_service() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '行動通信服務'
      list['id'] = 'mobile-service'

      mobile_service = {}
      mobile_service['telecom'] = '行動通信服務'
      mobile_service['mobile'] = '手機'
      mobile_service['accessaries'] = '行動週邊配備'
      mobile_service['devices'] = '手持行動裝置'

      list['sub'] = mobile_service
      return list

# 網際網路服務供應 internet-service
class InternetService(object):
   def internet_service() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '網際網路服務供應'
      list['id'] = 'internet-service'

      internet_service = {}
      internet_service['web-service'] = '網路'
      internet_service['web-design'] = '網頁設計'
      internet_service['e-commerce'] = '電子商務'
      internet_service['software'] = '網路軟體'

      list['sub'] = internet_service
      return list

# 航太科技 aerospace-technology
class AerospaceTechnology(object):
   def aerospace_technology() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '航太科技'
      list['id'] = 'aerospace-technology'

      aerospace_technology = {}
      aerospace_technology['aviation'] = '航太科技'

      list['sub'] = aerospace_technology
      return list

# 通信工程及器材 communication-engineering
class CommunicationEngineering(object):
   def communication_engineering() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '通信工程及器材'
      list['id'] = 'communication-engineering'

      communication_engineering = {}
      communication_engineering['optical-fiber'] = '光纖通信'
      communication_engineering['ship-radio'] = '船舶無線電'
      communication_engineering['radio'] = '無線電通訊'
      communication_engineering['satellite'] = '衛星通訊'
      communication_engineering['GPS'] = '衛星導航'
      communication_engineering['landline'] = '固網服務'
      communication_engineering['equipment'] = '電信器材'
      communication_engineering['parts'] = '通訊零組件'
      communication_engineering['radar-microwave'] = '雷達微波通訊'
      communication_engineering['inspection'] = '通訊工業檢測'

      list['sub'] = communication_engineering
      return list

# 電腦機房工程及設備 computer-room-supplies
class ComputerRoomSupplies(object):
   def computer_room_supplies() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '電腦機房工程及設備'
      list['id'] = 'computer-room-supplies'

      computer_room_supplies = {}
      computer_room_supplies['IDC-equip'] = '電腦機房設備'
      computer_room_supplies['UPS'] = '不斷電系統'

      list['sub'] = computer_room_supplies
      return list

# 電腦網路系統設備 network-equipment
class NetworkEquipment(object):
   def network_equipment() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '電腦網路系統設備'
      list['id'] = 'network-equipment'

      network_equipment = {}
      network_equipment['routers'] = '路由器'
      network_equipment['hubs'] = '集線器'
      network_equipment['modem'] = '數據機'
      network_equipment['equipment'] = '網路通訊設備'

      list['sub'] = network_equipment
      return list

# 電腦硬體 computer-hardware
class ComputerHardware(object):
   def computer_hardware() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '電腦硬體'
      list['id'] = 'computer-hardware'

      computer_hardware = {}
      computer_hardware['cards'] = '電腦版卡'
      computer_hardware['terminals'] = '終端機'
      computer_hardware['servers'] = '伺服器'
      computer_hardware['desktop'] = '桌上型電腦'
      computer_hardware['notebook'] = '筆記型電腦'
      computer_hardware['cases'] = '電腦機殼'
      computer_hardware['hardware'] = '電腦硬體'
      computer_hardware['parts'] = '電腦零組件'
      computer_hardware['power-supplies'] = '電源供應器'
      computer_hardware['storages'] = '電腦儲存裝置'
      computer_hardware['IC'] = 'IC積體電路'
      computer_hardware['output-devices'] = '輸出裝置'
      computer_hardware['input-devices'] = '輸入裝置'

      list['sub'] = computer_hardware
      return list

# 電腦軟體 software
class Software(object):
   def software() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '電腦軟體'
      list['id'] = 'software'

      software = {}
      software['software'] = '電腦軟體'

      list['sub'] = software
      return list

# 電腦週邊設備耗材 computer-peripheral
class ComputerPeripheral(object):
   def computer_peripheral() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '電腦週邊設備耗材'
      list['id'] = 'computer-peripheral'

      computer_peripheral = {}
      computer_peripheral['CD-tapes'] = '光碟片、磁帶'
      computer_peripheral['card-readers'] = '讀卡機'
      computer_peripheral['scanners'] = '掃描器'
      computer_peripheral['printers'] = '印表機'
      computer_peripheral['printer-cartridges'] = '碳粉色帶'
      computer_peripheral['mouses'] = '滑鼠'
      computer_peripheral['keyboards'] = '鍵盤'
      computer_peripheral['displays'] = '顯示器'
      computer_peripheral['digital-cameras'] = '數位相機'
      computer_peripheral['USB'] = '隨身碟'
      computer_peripheral['accessories-consumable'] = '電腦配件及耗材'

      list['sub'] = computer_peripheral
      return list

# 電腦買賣及維修 computer-maintenance
class ComputerMaintenance(object):
   def computer_maintenance() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '電腦買賣及維修'
      list['id'] = 'computer-maintenance'

      computer_maintenance = {}
      computer_maintenance['rental'] = '電腦出租'
      computer_maintenance['secondhand'] = '二手電腦'
      computer_maintenance['stores'] = '電腦賣場'
      computer_maintenance['repair'] = '電腦維修'
      computer_maintenance['computers'] = '電腦'

      list['sub'] = computer_maintenance
      return list

# 電腦資訊服務 computer-info-service
class ComputerInfoService(object):
   def computer_info_service() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '電腦資訊服務'
      list['id'] = 'computer-info-service'

      computer_info_service = {}
      computer_info_service['media-design'] = '多媒體設計'
      computer_info_service['coding'] = '程式設計'
      computer_info_service['drawing'] = '電腦繪圖'
      computer_info_service['consultant'] = '資訊系統諮詢服務'

      list['sub'] = computer_info_service
      return list

# 電話機及交換系統 switching-system
class SwitchingSystem(object):
   def switching_system() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '電話機及交換系統'
      list['id'] = 'switching-system'

      switching_system = {}
      switching_system['broadcasting'] = '廣播系統'
      switching_system['telephone'] = '電話'
      switching_system['switching'] = '交換機'
      switching_system['telephone-system'] = '電話器材及系統'

      list['sub'] = switching_system
      return list

# 對講機廣播監控設備 radio-monitoring
class RadioMonitoring(object):
   def radio_monitoring() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '對講機廣播監控設備'
      list['id'] = 'radio-monitoring'

      radio_monitoring = {}
      radio_monitoring['intercom'] = '對講機'
      radio_monitoring['monitor'] = '監控系統'
      radio_monitoring['video-phone'] = '視訊電話'

      list['sub'] = radio_monitoring
      return list

# 閉路電視 cctv
class Cctv(object):
   def cctv() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '閉路電視'
      list['id'] = 'cctv'

      cctv = {}
      cctv['cctv'] = '閉路電視'

      list['sub'] = cctv
      return list

# 資訊通信 infocomm
class Infocomm(BaseCategory, MobileService, InternetService, AerospaceTechnology, CommunicationEngineering, 
ComputerRoomSupplies, NetworkEquipment, ComputerHardware, Software, ComputerPeripheral, ComputerMaintenance,
ComputerInfoService, SwitchingSystem, RadioMonitoring, Cctv):
   category_name = '資訊通信'
   category_id = 'infocomm'