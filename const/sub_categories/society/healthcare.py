from typing import Dict
from ..base_category import BaseCategory

# 衛生機關及單位 health-agencies
class HealthAgencies(object):
   def health_agencies() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '衛生機關及單位'
      list['id'] = 'health-agencies'

      health_agencies = {}
      health_agencies['health-authorities'] = '衛生機關'

      list['sub'] = health_agencies
      return list

# 中醫 tcm-healthcare
class TcmHealthcare(object):
   def tcm_healthcare() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '中醫'
      list['id'] = 'tcm-healthcare'

      tcm_healthcare = {}
      tcm_healthcare['Chinese-medicines'] = '中醫'

      list['sub'] = tcm_healthcare
      return list

# 西醫 western-healthcare
class WesternHealthcare(object):
   def western_healthcare() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '西醫'
      list['id'] = 'western-healthcare'

      western_healthcare = {}
      western_healthcare['rehabilitation'] = '復健科'
      western_healthcare['ophthalmology'] = '眼科'
      western_healthcare['gynecology-and-obstetrics'] = '婦產科'
      western_healthcare['otolaryngology'] = '耳鼻喉科'
      western_healthcare['urology'] = '泌尿科'
      western_healthcare['dermatology'] = '皮膚科'
      western_healthcare['surgery'] = '外科'
      western_healthcare['pediatric'] = '內兒科'
      western_healthcare['dentistry'] = '牙科'
      western_healthcare['physiology'] = '心理精神科'
      western_healthcare['western-medicine'] = '西醫'

      list['sub'] = western_healthcare
      return list

# Ｘ光線院、醫學化驗院 x-ray
class XRay(object):
   def x_ray() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = 'Ｘ光線院、醫學化驗院'
      list['id'] = 'x-ray'

      x_ray = {}
      x_ray['laboratory'] = '檢驗所'

      list['sub'] = x_ray
      return list

# 藥品及藥材 drugs-and-medicine
class DrugsAndMedicine(object):
   def drugs_and_medicine() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '藥品及藥材'
      list['id'] = 'drugs-and-medicine'

      drugs_and_medicine = {}
      drugs_and_medicine['pharmacy'] = '藥局'
      drugs_and_medicine['Chinese-medicines'] = '中藥行'
      drugs_and_medicine['pharmaceutical-companies'] = '藥商'

      list['sub'] = drugs_and_medicine
      return list

# 動物醫院及藥品 veterinary
class Veterinary(object):
   def veterinary() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '動物醫院及藥品'
      list['id'] = 'veterinary'

      veterinary = {}
      veterinary['veterinary'] = '動物醫院'
      veterinary['veterinary-medicine'] = '動物藥品'

      list['sub'] = veterinary
      return list

# 民俗療法及用品 folk-medicine
class FolkMedicine(object):
   def folk_medicine() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '民俗療法及用品'
      list['id'] = 'folk-medicine'

      folk_medicine = {}
      folk_medicine['herbal-shops'] = '青草店'
      folk_medicine['folk-medicine-equipment'] = '民俗療法設備'
      folk_medicine['folk-medicine'] = '民俗療法'

      list['sub'] = folk_medicine
      return list

# 生物科技、奈米科技 biotechnology
class Biotechnology(object):
   def biotechnology() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '生物科技、奈米科技'
      list['id'] = 'biotechnology'

      biotechnology = {}
      biotechnology['nanotechnology'] = '奈米科技'
      biotechnology['biotechnology'] = '生物科技'

      list['sub'] = biotechnology
      return list

# 醫療器材 medical-supplies
class MedicalSupplies(object):
   def medical_supplies() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '醫療器材'
      list['id'] = 'medical-supplies'

      medical_supplies = {}
      medical_supplies['dental-supplies-dental-cast'] = '齒模'
      medical_supplies['medical-equipment'] = '醫療器材'
      medical_supplies['medical-equip-manufacturers'] = '醫療器材製造'
      medical_supplies['hospital-supplies'] = '醫院設備'
      medical_supplies['rehabilitation-equipment'] = '復健器材'

      list['sub'] = medical_supplies
      return list

# 醫事管理服務 medical-management
class MedicalManagement(object):
   def medical_management() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '醫事管理服務'
      list['id'] = 'medical-management'

      medical_management = {}
      medical_management['medical-management'] = '醫事管理'

      list['sub'] = medical_management
      return list

# 醫療救傷 medical-care
class MedicalCare(object):
   def medical_care() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '醫療救傷'
      list['id'] = 'medical-care'

      medical_care = {}
      medical_care['first-aids'] = '醫療服務'

      list['sub'] = medical_care
      return list

# 醫療矯正訓練 medical-remedial-training
class MedicalRemedialTraining(object):
   def medical_remedial_training() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '醫療矯正訓練'
      list['id'] = 'medical-remedial-training'

      medical_remedial_training = {}
      medical_remedial_training['medical-remedial-training'] = '醫療矯正訓練'

      list['sub'] = medical_remedial_training
      return list

# 安養看護服務 nursing-services
class NursingServices(object):
   def nursing_services() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '安養看護服務'
      list['id'] = 'nursing-services'

      nursing_services = {}
      nursing_services['child-care-centers'] = '保母'
      nursing_services['maternity-centers'] = '坐月子中心'
      nursing_services['rest-homes'] = '安養中心'

      list['sub'] = nursing_services
      return list

# 美容美髮 beauty-salon
class BeautySalon(object):
   def beauty_salon() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '美容美髮'
      list['id'] = 'beauty-salon'

      beauty_salon = {}
      beauty_salon['wigs'] = '假髮'
      beauty_salon['tattoo'] = '紋身'
      beauty_salon['nail-art'] = '指甲彩繪'
      beauty_salon['hair-salons'] = '沙龍美髮'
      beauty_salon['beauty-shops'] = '美容護膚'
      beauty_salon['salon-equip'] = '美容設備'

      list['sub'] = beauty_salon
      return list

# 減肥及營養指導 diet-and-nutrition-center
class DietAndNutritionCenter(object):
   def diet_and_nutrition_center() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '減肥及營養指導'
      list['id'] = 'diet-and-nutrition-center'

      diet_and_nutrition_center = {}
      diet_and_nutrition_center['diet-nutrition-center'] = '減肥塑身'

      list['sub'] = diet_and_nutrition_center
      return list

# 衛生用品 sanitary-supplies
class SanitarySupplies(object):
   def sanitary_supplies() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '衛生用品'
      list['id'] = 'sanitary-supplies'

      sanitary_supplies = {}
      sanitary_supplies['masks-towels'] = '口罩、毛巾'
      sanitary_supplies['personal-hygiene'] = '個人衛生用品'
      sanitary_supplies['personal-hygiene-manufacturers'] = '衛生用品製造'

      list['sub'] = sanitary_supplies
      return list

# 醫療保健 healthcare
class Healthcare(BaseCategory, HealthAgencies, TcmHealthcare, WesternHealthcare, XRay, DrugsAndMedicine,
Veterinary, FolkMedicine, Biotechnology, MedicalSupplies, MedicalManagement, MedicalCare, MedicalRemedialTraining,
NursingServices, BeautySalon, DietAndNutritionCenter, SanitarySupplies):
   category_name = '醫療保健'
   category_id = 'healthcare'