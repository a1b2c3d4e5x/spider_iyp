from typing import Dict
from ..base_category import BaseCategory

# 航空及機場服務 aviation-and-airport-services
class AviationAndAirportServices(object):
   def aviation_and_airport_services() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '航空及機場服務'
      list['id'] = 'aviation-and-airport-services'

      aviation_and_airport_services = {}
      aviation_and_airport_services['ground-services'] = '地勤服務'
      aviation_and_airport_services['airports'] = '機場、航空站'
      aviation_and_airport_services['airlines'] = '航空業'
      aviation_and_airport_services['airplane-repair-maintenance'] = '飛機修理保養'

      list['sub'] = aviation_and_airport_services
      return list

# 客運服務 shuttle-service
class ShuttleService(object):
   def shuttle_service() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '客運服務'
      list['id'] = 'shuttle-service'

      shuttle_service = {}
      shuttle_service['railroad-services'] = '鐵路'
      shuttle_service['bus-services'] = '客運、公車'
      shuttle_service['mass-rapid-transport'] = '捷運'

      list['sub'] = shuttle_service
      return list

# 貨運服務 cargo-service
class CargoService(object):
   def cargo_service() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '貨運服務'
      list['id'] = 'cargo-service'

      cargo_service = {}
      cargo_service['motorcycle-transport'] = '機車拖運'
      cargo_service['railroad-shipping-agency'] = '鐵路承攬'
      cargo_service['machinery-relocation'] = '機器搬運'
      cargo_service['container-service'] = '貨櫃運輸'
      cargo_service['container-hire-maintenance'] = '貨櫃出租保修'
      cargo_service['air-cargo-agency'] = '航空貨運承攬'
      cargo_service['sea-cargo-agency'] = '海運承攬'
      cargo_service['special-cargo-transport'] = '特殊品運輸'
      cargo_service['freight-forwarding'] = '貨運承攬'

      list['sub'] = cargo_service
      return list

# 搬家及搬運服務 relocation-service
class RelocationService(object):
   def relocation_service() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '搬家及搬運服務'
      list['id'] = 'relocation-service'

      relocation_service = {}
      relocation_service['moving-services'] = '搬家服務'
      relocation_service['crane-services'] = '搬運起重服務'

      list['sub'] = relocation_service
      return list

# 吊車起重服務 crane-lifting-services
class CraneLiftingServices(object):
   def crane_lifting_services() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '吊車起重服務'
      list['id'] = 'crane-lifting-services'

      crane_lifting_services = {}
      crane_lifting_services['forklifts'] = '堆高機'
      crane_lifting_services['loadometer'] = '地磅'
      crane_lifting_services['cables'] = '吊索、吊纜'
      crane_lifting_services['cranes'] = '吊車、起重機'

      list['sub'] = crane_lifting_services
      return list

# 公路監理 highway-supervision
class HighwaySupervision(object):
   def highway_supervision() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '公路監理'
      list['id'] = 'highway-supervision'

      highway_supervision = {}
      highway_supervision['motor-vehicle-office'] = '監理所'

      list['sub'] = highway_supervision
      return list

# 加油站及設備 gas-station-and-equipment
class GasStationAndEquipment(object):
   def gas_station_and_equipment() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '加油站及設備'
      list['id'] = 'gas-station-and-equipment'

      gas_station_and_equipment = {}
      gas_station_and_equipment['petrol-stations'] = '加油站'
      gas_station_and_equipment['gas-station-equipment'] = '加油站設備'

      list['sub'] = gas_station_and_equipment
      return list

# 停車場及設備 parking-space
class ParkingSpace(object):
   def parking_space() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '停車場及設備'
      list['id'] = 'parking-space'

      parking_space = {}
      parking_space['car-parks'] = '停車場'
      parking_space['car-park-equipment'] = '停車場設備'

      list['sub'] = parking_space
      return list

# 汽車拖吊服務 auto-towing-service
class AutoTowingService(object):
   def auto_towing_service() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '汽車拖吊服務'
      list['id'] = 'auto-towing-service'

      auto_towing_service = {}
      auto_towing_service['car-towing-service'] = '汽車拖吊服務'

      list['sub'] = auto_towing_service
      return list

# 海運及港灣服務 marine-and-harbor-service
class MarineAndHarborService(object):
   def marine_and_harbor_service() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '海運及港灣服務'
      list['id'] = 'marine-and-harbor-service'

      marine_and_harbor_service = {}
      marine_and_harbor_service['ferry-services-boat-charters'] = '渡輪遊艇出租'
      marine_and_harbor_service['ship-building'] = '船舶建造'
      marine_and_harbor_service['marine-engineering'] = '海事工程'
      marine_and_harbor_service['boat-repair'] = '船舶維修'
      marine_and_harbor_service['terminals-service-stations'] = '碼頭船舶服務'
      marine_and_harbor_service['shipping-agents'] = '船務代理'
      marine_and_harbor_service['salvage-services'] = '打撈業'
      marine_and_harbor_service['tugboat-services'] = '拖船業'
      marine_and_harbor_service['pilotage'] = '引水人'

      list['sub'] = marine_and_harbor_service
      return list

# 報關業 customs-industry
class CustomsIndustry(object):
   def customs_industry() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '報關業'
      list['id'] = 'customs-industry'

      customs_industry = {}
      customs_industry['custom-brokers'] = '報關業'

      list['sub'] = customs_industry
      return list

# 倉儲服務 warehouse
class Warehouse(object):
   def warehouse() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '倉儲服務'
      list['id'] = 'warehouse'

      warehouse = {}
      warehouse['refrigerated-storages'] = '低溫倉儲'
      warehouse['storage-services'] = '倉儲'
      warehouse['storage-equipments'] = '倉庫設備用品'

      list['sub'] = warehouse
      return list

# 租車服務 car-rental
class CarRental(object):
   def car_rental() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '租車服務'
      list['id'] = 'car-rental'

      car_rental = {}
      car_rental['motorcycle-rentals'] = '機車出租'
      car_rental['tour-bus-rentals'] = '遊覽車出租'
      car_rental['car-rentals'] = '汽車出租'
      car_rental['truck-rentals'] = '貨車出租'
      car_rental['bicycle-rentals'] = '自行車出租'

      list['sub'] = car_rental
      return list

# 計程車服務 taxi-services
class TaxiServices(object):
   def taxi_services() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '計程車服務'
      list['id'] = 'taxi-services'

      taxi_services = {}
      taxi_services['taxis'] = '計程車'

      list['sub'] = taxi_services
      return list

# 快捷及快遞服務 courier-services
class CourierServices(object):
   def courier_services() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '快捷及快遞服務'
      list['id'] = 'courier-services'

      courier_services = {}
      courier_services['couriers'] = '快遞服務'

      list['sub'] = courier_services
      return list

# 汽車 automobile
class Automobile(object):
   def automobile() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '汽車'
      list['id'] = 'automobile'

      automobile = {}
      automobile['auto-electrical-equipment'] = '汽車電機設備'
      automobile['transmission-systems'] = '傳動變速系統'
      automobile['vehicle-recycling'] = '廢車回收'
      automobile['repair-equipment'] = '汽車修理配備'
      automobile['repair-maintenance'] = '汽車維修保養'
      automobile['car-accessories'] = '汽車百貨'
      automobile['car-velvet'] = '汽車美容'
      automobile['car-washing-supplies'] = '洗車業設備'
      automobile['new-car-dealers'] = '新車買賣'
      automobile['secondhand-car-dealers'] = '二手車買賣'
      automobile['car-stereo'] = '汽車音響'
      automobile['car-alarm-systems'] = '汽車防盜系統'
      automobile['car-parts'] = '汽車零配件'

      list['sub'] = automobile
      return list

# 自行車機車 bike-and-motorcycle
class BikeAndMotorcycle(object):
   def bike_and_motorcycle() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '自行車機車'
      list['id'] = 'bike-and-motorcycle'

      bike_and_motorcycle = {}
      bike_and_motorcycle['bicycles'] = '自行車'
      bike_and_motorcycle['motorcycles'] = '機車'

      list['sub'] = bike_and_motorcycle
      return list

# 輪胎 tire-and-tyre
class TireAndTyre(object):
   def tire_and_tyre() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '輪胎'
      list['id'] = 'tire-and-tyre'

      tire_and_tyre = {}
      tire_and_tyre['tires'] = '輪胎'

      list['sub'] = tire_and_tyre
      return list

# 交通安全器材 safety-equipment
class SafetyEquipment(object):
   def safety_equipment() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '交通安全器材'
      list['id'] = 'safety-equipment'

      safety_equipment = {}
      safety_equipment['traffic-signs'] = '交通號誌'
      safety_equipment['road-safety-equipment'] = '道路安全控制器材及工程'

      list['sub'] = safety_equipment
      return list

# 安全帽 safety-helmet
class SafetyHelmet(object):
   def safety_helmet() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '安全帽'
      list['id'] = 'safety-helmet'

      safety_helmet = {}
      safety_helmet['helmets'] = '安全帽'

      list['sub'] = safety_helmet
      return list

# 行車運輸 transportation
class Transportation(BaseCategory, AviationAndAirportServices, ShuttleService, CargoService, RelocationService,
CraneLiftingServices, HighwaySupervision, GasStationAndEquipment, ParkingSpace, AutoTowingService,
MarineAndHarborService, CustomsIndustry, Warehouse, CarRental, TaxiServices, CourierServices, Automobile,
BikeAndMotorcycle, TireAndTyre, SafetyEquipment, SafetyHelmet):
   category_name = '行車運輸'
   category_id = 'transportation'