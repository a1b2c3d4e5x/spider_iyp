from typing import Dict
from ..base_category import BaseCategory

# ＣＤ錄音帶 cd-and-tape
class CdAndTape(object):
   def cd_and_tape() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = 'ＣＤ錄音帶'
      list['id'] = 'cd-and-tape'

      cd_and_tape = {}
      cd_and_tape['CD-tapes-manufacturers'] = 'CD片、錄音帶製造'
      cd_and_tape['music-shops'] = '唱片行'

      list['sub'] = cd_and_tape
      return list

# 影帶影碟光碟 dvd-and-vcd
class DvdAndVcd(object):
   def dvd_and_vcd() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '影帶影碟光碟'
      list['id'] = 'dvd-and-vcd'

      dvd_and_vcd = {}
      dvd_and_vcd['video-tapes-DVD-manufacturers'] = '錄影帶、DVD製造'
      dvd_and_vcd['video-tapes-rental'] = '錄影帶出租'
      dvd_and_vcd['video-tapes-DVD'] = '錄影帶、DVD'

      list['sub'] = dvd_and_vcd
      return list

# 錄音錄影 recording-video
class RecordingVideo(object):
   def recording_video() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '錄音錄影'
      list['id'] = 'recording-video'

      recording_video = {}
      recording_video['production-service'] = '視聽製作服務'
      recording_video['recording-equip-manufacturers'] = '影音設備製造'

      list['sub'] = recording_video
      return list

# 眼鏡 glasses
class Glasses(object):
   def glasses() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '眼鏡'
      list['id'] = 'glasses'

      glasses = {}
      glasses['glasses-contact-lenses'] = '眼鏡、隱形眼鏡'
      glasses['glasses-manufacturers'] = '眼鏡製造'

      list['sub'] = glasses
      return list

# 鐘錶 watches-and-clocks
class WatchesAndClocks(object):
   def watches_and_clocks() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '鐘錶'
      list['id'] = 'watches-and-clocks'

      watches_and_clocks = {}
      watches_and_clocks['watch-manufacturers'] = '鐘錶製造'
      watches_and_clocks['watches'] = '鐘錶'

      list['sub'] = watches_and_clocks
      return list

# 攝影 photography
class Photography(object):
   def photography() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '攝影'
      list['id'] = 'photography'

      photography = {}
      photography['image-equip-materials'] = '影像設備材料'
      photography['photo-processing'] = '相片沖洗'
      photography['camera-supplies'] = '相機、攝影器材製造'
      photography['camera'] = '相機、攝影機'
      photography['photo-service'] = '攝影服務'

      list['sub'] = photography
      return list

# 視聽工程器材 media-supplies
class MediaSupplies(object):
   def media_supplies() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '視聽工程器材'
      list['id'] = 'media-supplies'

      media_supplies = {}
      media_supplies['cable-tv-equip'] = '有線電視設備'
      media_supplies['stage-engineering'] = '舞台工程'
      media_supplies['audio-video-engineering'] = '視聽工程'

      list['sub'] = media_supplies
      return list

# 儀器 instrument
class Instrument(object):
   def instrument() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '儀器'
      list['id'] = 'instrument'

      instrument = {}
      instrument['optical'] = '光學儀器'
      instrument['weighting'] = '度量衡儀器'
      instrument['surveying'] = '測量儀器'
      instrument['temp-humidity'] = '溫濕度儀器'
      instrument['laboratory'] = '科學實驗室設備'
      instrument['instrument'] = '儀器'

      list['sub'] = instrument
      return list

# 數位錄放設備 digital-record-device
class DigitalRecordDevice(object):
   def digital_record_device() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '數位錄放設備'
      list['id'] = 'digital-record-device'

      digital_record_device = {}
      digital_record_device['digital-recording-equip'] = '數位錄放設備'

      list['sub'] = digital_record_device
      return list

# 聲光影視 media
class Media(BaseCategory, CdAndTape, DvdAndVcd, RecordingVideo, Glasses, WatchesAndClocks,
Photography, MediaSupplies, Instrument, DigitalRecordDevice):
   category_name = '聲光影視'
   category_id = 'media'