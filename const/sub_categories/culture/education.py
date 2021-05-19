from typing import Dict
from ..base_category import BaseCategory

# 學術研究機構 academic-institutes
class AcademicInstitutes(object):
   def academic_institutes() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '學術研究機構'
      list['id'] = 'academic-institutes'

      academic_institutes = {}
      academic_institutes['research-institutions'] = '學術研究機構'

      list['sub'] = academic_institutes
      return list

# 學校 schools
class Schools(object):
   def schools() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '學校'
      list['id'] = 'schools'

      schools = {}
      schools['supplementary-correspondence-education'] = '補校、函授'
      schools['colleges-universities'] = '大專院校'
      schools['primary-schools'] = '小學'
      schools['high-schools'] = '中學'
      schools['kindergartens'] = '幼兒園'

      list['sub'] = schools
      return list

# 補習教育 remedial-education
class RemedialEducation(object):
   def remedial_education() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '補習教育'
      list['id'] = 'remedial-education'

      remedial_education = {}
      remedial_education['languages'] = '語文補習班'
      remedial_education['dancing-yoga'] = '舞蹈、瑜伽'
      remedial_education['computers'] = '電腦補習班'
      remedial_education['specialties'] = '專業技能'
      remedial_education['studying-tutorials'] = '升學補習班'
      remedial_education['training-centers'] = '補習班'
      remedial_education['talent-learning'] = '才藝補習班'

      list['sub'] = remedial_education
      return list

# 訓練 training
class Training(object):
   def training() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '訓練'
      list['id'] = 'training'

      training = {}
      training['training-courses'] = '訓練課程'

      list['sub'] = training
      return list

# 安親班 daycare-center
class DaycareCenter(object):
   def daycare_center() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '安親班'
      list['id'] = 'daycare-center'

      daycare_center = {}
      daycare_center['after-school-care'] = '課輔安親'

      list['sub'] = daycare_center
      return list

# 駕訓班 driving-training-course
class DrivingTrainingCourse(object):
   def driving_training_course() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '駕訓班'
      list['id'] = 'driving-training-course'

      driving_training_course = {}
      driving_training_course['driving-schools'] = '駕訓班'

      list['sub'] = driving_training_course
      return list

# 留學服務 study-service
class StudyService(object):
   def study_service() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '留學服務'
      list['id'] = 'study-service'

      study_service = {}
      study_service['international-education-services'] = '留學服務'

      list['sub'] = study_service
      return list

# 圖書館及設備 library-and-equipment
class LibraryAndEquipment(object):
   def library_and_equipment() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '圖書館及設備'
      list['id'] = 'library-and-equipment'

      library_and_equipment = {}
      library_and_equipment['libraries'] = '圖書館'
      library_and_equipment['library-equipments'] = '圖書設備及用品'

      list['sub'] = library_and_equipment
      return list

# Ｋ書中心 reading-center
class ReadingCenter(object):
   def reading_center() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = 'Ｋ書中心'
      list['id'] = 'reading-center'

      reading_center = {}
      reading_center['studying-centers'] = 'Ｋ書中心'

      list['sub'] = reading_center
      return list

# 藝文、科學中心 art-science-center
class ArtScienceCenter(object):
   def art_science_center() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '藝文、科學中心'
      list['id'] = 'art-science-center'

      art_science_center = {}
      art_science_center['museums'] = '美術館、博物館'
      art_science_center['educational-cultural-centers'] = '社教、文化中心'
      art_science_center['astronomy-science-museum'] = '天文、科學館'

      list['sub'] = art_science_center
      return list

# 育才學術 education
class Education(BaseCategory, AcademicInstitutes, Schools, RemedialEducation, Training, DaycareCenter,
DrivingTrainingCourse, StudyService, LibraryAndEquipment, ReadingCenter, ArtScienceCenter):
   category_name = '育才學術'
   category_id = 'education'