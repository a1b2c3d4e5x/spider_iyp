from typing import Dict
from ..base_category import BaseCategory

# 旅行 travel-agency
class TravelAgency(object):
   def travel_agency() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '旅行'
      list['id'] = 'travel-agency'

      travel_agency = {}
      travel_agency['travel-agents'] = '旅行社'
      travel_agency['travel-supplies'] = '旅行用品'

      list['sub'] = travel_agency
      return list

# 飯店旅館 hotel-service
class HotelService(object):
   def hotel_service() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '飯店旅館'
      list['id'] = 'hotel-service'

      hotel_service = {}
      hotel_service['bed-and-breakfast'] = '民宿'
      hotel_service['Motels'] = '汽車旅館'
      hotel_service['Hotels'] = '飯店、旅館'
      hotel_service['hotel-supplies'] = '飯店備品'

      list['sub'] = hotel_service
      return list

# 畫及畫廊 art-galleries
class ArtGalleries(object):
   def art_galleries() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '畫及畫廊'
      list['id'] = 'art-galleries'

      art_galleries = {}
      art_galleries['art-galleries'] = '畫廊、藝廊'
      art_galleries['picture-framing'] = '裱框'

      list['sub'] = art_galleries
      return list

# 嗜好 hobby
class Hobby(object):
   def hobby() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '嗜好'
      list['id'] = 'hobby'

      hobby = {}
      hobby['music-class'] = '音樂教室'
      hobby['stamps-coins'] = '郵票、古幣'
      hobby['chess-clubs'] = '棋社'
      hobby['antiques'] = '古玩藝品'

      list['sub'] = hobby
      return list

# 音樂 music
class Music(object):
   def music() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '音樂'
      list['id'] = 'music'

      music = {}
      music['choir-orchestra'] = '合唱團、樂團'
      music['pianos'] = '鋼琴'
      music['musical-instruments'] = '樂器'

      list['sub'] = music
      return list

# 電影製片及發行 film-production
class FilmProduction(object):
   def film_production() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '電影製片及發行'
      list['id'] = 'film-production'

      film_production = {}
      film_production['movie-equipment'] = '電影器材'
      film_production['movie-production'] = '影片製片'

      list['sub'] = film_production
      return list

# 戲劇 drama
class Drama(object):
   def drama() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '戲劇'
      list['id'] = 'drama'

      drama = {}
      drama['Song-and-Dance-Troupe'] = '康樂隊、歌舞團'
      drama['program-planning'] = '節目企劃'
      drama['performance-groups'] = '舞團、劇團'
      drama['folk-art-performances'] = '民俗藝術表演'
      drama['drama-production'] = '戲劇製作'

      list['sub'] = drama
      return list

# 寵物 pet
class Pet(object):
   def pet() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '寵物'
      list['id'] = 'pet'

      pet = {}
      pet['pet-training'] = '寵物訓練'
      pet['pet-shops'] = '寵物店'
      pet['aquarium-supplies'] = '水族館'
      pet['bird-farms'] = '鳥園'

      list['sub'] = pet
      return list

# 體育團體及協會 sports-bodies
class SportsBodies(object):
   def sports_bodies() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '體育團體及協會'
      list['id'] = 'sports-bodies'

      sports_bodies = {}
      sports_bodies['sport-associations'] = '體育協會、運動團體'

      list['sub'] = sports_bodies
      return list

# 國術功夫 martial-arts
class MartialArts(object):
   def martial_arts() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '國術功夫'
      list['id'] = 'martial-arts'

      martial_arts = {}
      martial_arts['martial-arts'] = '武術道館'
      martial_arts['traditional-chinese-boxing'] = '國術館'

      list['sub'] = martial_arts
      return list

# 娛樂用品 entertainment-supplies
class EntertainmentSupplies(object):
   def entertainment_supplies() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '娛樂用品'
      list['id'] = 'entertainment-supplies'

      entertainment_supplies = {}
      entertainment_supplies['games'] = '遊戲用品'
      entertainment_supplies['mahjong'] = '麻將'
      entertainment_supplies['playing-cards'] = '撲克牌、紙牌'

      list['sub'] = entertainment_supplies
      return list

# 休閒用品 leisure-supplies
class LeisureSupplies(object):
   def leisure_supplies() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '休閒用品'
      list['id'] = 'leisure-supplies'

      leisure_supplies = {}
      leisure_supplies['leisure-supplies'] = '休閒用品'
      leisure_supplies['mountain-gears'] = '登山用品'
      leisure_supplies['diving-equipment'] = '潛水器材'
      leisure_supplies['fishing-gears'] = '漁具用品'
      leisure_supplies['horse-riding'] = '馬術'
      leisure_supplies['camping-gears'] = '露營用品'

      list['sub'] = leisure_supplies
      return list

# 運動器材及用品 sports-supplies
class SportsSupplies(object):
   def sports_supplies() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '運動器材及用品'
      list['id'] = 'sports-supplies'

      sports_supplies = {}
      sports_supplies['bowling-alley'] = '保齡球場'
      sports_supplies['Balls'] = '球類器材'
      sports_supplies['fitness-equip'] = '健身運動器材'
      sports_supplies['golf'] = '高爾夫球'
      sports_supplies['water-sports'] = '水上運動'

      list['sub'] = sports_supplies
      return list

# 運動場所 sports-venues
class SportsVenues(object):
   def sports_venues() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '運動場所'
      list['id'] = 'sports-venues'

      sports_venues = {}
      sports_venues['tennis-courts'] = '網球場'
      sports_venues['baseball-fields'] = '棒球場'
      sports_venues['stadiums'] = '體育場'
      sports_venues['horse-riding-fields'] = '騎馬場'
      sports_venues['skating-rink'] = '溜冰場'
      sports_venues['swimming-pools'] = '游泳池'
      sports_venues['golf-course'] = '高爾夫球場'
      sports_venues['fitness-centers'] = '健身中心'
      sports_venues['badminton-courts'] = '羽球館'

      list['sub'] = sports_venues
      return list

# 電影院 cinema
class Cinema(object):
   def cinema() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '電影院'
      list['id'] = 'cinema'

      cinema = {}
      cinema['theaters'] = '電影院'

      list['sub'] = cinema
      return list

# 娛樂場所 entertainment
class Entertainment(object):
   def entertainment() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '娛樂場所'
      list['id'] = 'entertainment'

      entertainment = {}
      entertainment['resorts'] = '渡假休閒中心'
      entertainment['whale-watching-boating'] = '賞鯨、泛舟'
      entertainment['pubs'] = '夜店'
      entertainment['amusement-places'] = '遊樂場'
      entertainment['KTV'] = 'KTV'
      entertainment['fishing-shrimp-playground'] = '釣魚、釣蝦場'
      entertainment['entertainment-business'] = '娛樂事業'
      entertainment['dance-halls-karaoke-bars'] = '舞廳、歌廳'
      entertainment['clubs'] = '俱樂部、夜總會'
      entertainment['SPA-hot-springs'] = '泡湯'

      list['sub'] = entertainment
      return list

# 景點名勝 sightseeing
class Sightseeing(object):
   def sightseeing() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '景點名勝'
      list['id'] = 'sightseeing'

      sightseeing = {}
      sightseeing['tourist-farms'] = '觀光農場'
      sightseeing['scenery-stops'] = '旅遊景點'

      list['sub'] = sightseeing
      return list

# 彩券 lottery
class Lottery(object):
   def lottery() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '彩券'
      list['id'] = 'lottery'

      lottery = {}
      lottery['lottery-shops'] = '彩券行'

      list['sub'] = lottery
      return list

# 樂在休閒 leisure
class Leisure(BaseCategory, TravelAgency, HotelService, ArtGalleries, Hobby, Music, FilmProduction,
Drama, Pet, SportsBodies, MartialArts, EntertainmentSupplies, LeisureSupplies, SportsSupplies, 
SportsVenues, Cinema, Entertainment, Sightseeing, Lottery):
   category_name = '樂在休閒'
   category_id = 'leisure'