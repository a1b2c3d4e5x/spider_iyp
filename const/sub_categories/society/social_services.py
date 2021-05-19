from typing import Dict
from ..base_category import BaseCategory

# 宗教及宗教用品 religious-supplies
class ReligiousSupplies(object):
   def religious_supplies() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '宗教及宗教用品'
      list['id'] = 'religious-supplies'

      religious_supplies = {}
      religious_supplies['temples'] = '寺廟'
      religious_supplies['religious-groups'] = '宗教團體'
      religious_supplies['churches'] = '教堂、教會'
      religious_supplies['sandalwood'] = '檀香'
      religious_supplies['religious-supplies'] = '宗教物品'

      list['sub'] = religious_supplies
      return list

# 政治團體 political-groups
class PoliticalGroups(object):
   def political_groups() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '政治團體'
      list['id'] = 'political-groups'

      political_groups = {}
      political_groups['political-groups'] = '政黨團體'
      political_groups['representatives-service'] = '民意代表'
      political_groups['public-service-agency'] = '民眾服務社'

      list['sub'] = political_groups
      return list

# 社會團體 social-groups
class SocialGroups(object):
   def social_groups() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '社會團體'
      list['id'] = 'social-groups'

      social_groups = {}
      social_groups['social-groups'] = '社會團體'

      list['sub'] = social_groups
      return list

# 農漁民團體 farmers-group
class FarmersGroup(object):
   def farmers_group() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '農漁民團體'
      list['id'] = 'farmers-group'

      farmers_group = {}
      farmers_group['farmer-association'] = '農會'
      farmers_group['fishermen-association'] = '漁會'
      farmers_group['irrigation-association'] = '水利會'

      list['sub'] = farmers_group
      return list

# 工商團體 business-organization
class BusinessOrganization(object):
   def business_organization() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '工商團體'
      list['id'] = 'business-organization'

      business_organization = {}
      business_organization['industrial-association'] = '工會'
      business_organization['chamber-of-commerce'] = '商會'
      business_organization['association'] = '同業公會'

      list['sub'] = business_organization
      return list

# 婚姻 marriage
class Marriage(object):
   def marriage() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '婚姻'
      list['id'] = 'marriage'

      marriage = {}
      marriage['matchmaking'] = '婚姻介紹'

      list['sub'] = marriage
      return list

# 社會福利 social-welfare
class SocialWelfare(object):
   def social_welfare() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '社會福利'
      list['id'] = 'social-welfare'

      social_welfare = {}
      social_welfare['welfare-organization'] = '社福機構'

      list['sub'] = social_welfare
      return list

# 老人安養院 nursing-home
class NursingHome(object):
   def nursing_home() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '老人安養院'
      list['id'] = 'nursing-home'

      nursing_home = {}
      nursing_home['nursing-home'] = '老人安養院'

      list['sub'] = nursing_home
      return list

# 社區組織 community
class Community(object):
   def community() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '社區組織'
      list['id'] = 'community'

      community = {}
      community['community-organization'] = '社區組織'

      list['sub'] = community
      return list

# 社會服務 social-services
class SocialServices(BaseCategory, ReligiousSupplies, PoliticalGroups, SocialGroups, FarmersGroup, 
BusinessOrganization, Marriage, SocialWelfare, NursingHome, Community):
   category_name = '社會服務'
   category_id = 'social-services'