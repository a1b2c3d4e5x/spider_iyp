
from typing import Any, List, Dict
from .constant import constant

from .sub_categories.life.food_catering import FoodCatering
from .sub_categories.life.clothing_accessories import ClothingAccessories
from .sub_categories.life.housing import Housing
from .sub_categories.life.shopping import Shopping
from .sub_categories.life.appliances import Appliances

from .sub_categories.culture.leisure import Leisure
from .sub_categories.culture.education import Education
from .sub_categories.culture.news_and_culture import NewsAndCulture

from .sub_categories.service.advertising_print import AdvertisingPrint
from .sub_categories.service.environmental import Environmental
from .sub_categories.service.financial import Financial
from .sub_categories.service.infocomm import Infocomm
from .sub_categories.service.media import Media
from .sub_categories.service.office_stationery import OfficeStationery
from .sub_categories.service.packaging_service import PackagingService
from .sub_categories.service.transportation import Transportation

from .sub_categories.industry.agriculture import Agriculture
from .sub_categories.industry.chemical_industry import ChemicalIndustry
from .sub_categories.industry.electrical_material import ElectricalMaterial
from .sub_categories.industry.industrial_machinery import IndustrialMachinery
from .sub_categories.industry.metal_industry import MetalIndustry
from .sub_categories.industry.textile_industry import TextileIndustry

from .sub_categories.society.healthcare import Healthcare
from .sub_categories.society.ritual_funeral import RitualFuneral
from .sub_categories.society.social_services import SocialServices
from .sub_categories.society.utilities import Utilities

class __ConstCategories(object):
   def __parseCategory(self, class_array: List[Any], target: str) -> List[Dict[str, Dict[str, str]]]:
      for c in class_array:
         if target == c.category_id:
            cla = c()
            all = []
            for item in cla.list():
               all.append(eval(cla.__class__.__name__ + '.' + item + '()'))

            return all
      return None

   @constant
   def categories() -> Dict[str, str]:
      part = []

      # ????????????
      life = {'name': '????????????', 'sub': {}}
      for c in [FoodCatering, ClothingAccessories, Housing, Shopping, Appliances]:
         life['sub'][c.category_id] = c.category_name
      part.append(life)

      # ????????????
      culture = {'name': '????????????', 'sub': {}}
      for c in [Leisure, Education, NewsAndCulture]:
         culture['sub'][c.category_id] = c.category_name
      part.append(culture)

      # ????????????
      service = {'name': '????????????', 'sub': {}}
      for c in [AdvertisingPrint, Environmental, Financial, Infocomm, Media, OfficeStationery, PackagingService, Transportation]:
         service['sub'][c.category_id] = c.category_name
      part.append(service)

      # ????????????
      industry = {'name': '????????????', 'sub': {}}
      for c in [Agriculture, ChemicalIndustry, ElectricalMaterial, IndustrialMachinery, MetalIndustry, TextileIndustry]:
         industry['sub'][c.category_id] = c.category_name
      part.append(industry)

      # ????????????
      social = {'name': '????????????', 'sub': {}}
      for c in [Healthcare, RitualFuneral, SocialServices, Utilities]:
         social['sub'][c.category_id] = c.category_name
      part.append(social)

      return part

   def sub_categories(self, main_category: str) -> List[Dict[str, Dict[str, str]]]:
      # ????????????
      result = self.__parseCategory([FoodCatering, ClothingAccessories, Housing, Shopping, Appliances], main_category)
      if None != result: return result
      
      # ????????????
      result = self.__parseCategory([Leisure, Education, NewsAndCulture], main_category)
      if None != result: return result

      # ????????????
      result = self.__parseCategory([AdvertisingPrint, Environmental, Financial, Infocomm, Media, OfficeStationery, PackagingService, Transportation], main_category)
      if None != result: return result

      # ????????????
      result = self.__parseCategory([Agriculture, ChemicalIndustry, ElectricalMaterial, IndustrialMachinery, MetalIndustry, TextileIndustry], main_category)
      if None != result: return result

      # ????????????
      result = self.__parseCategory([Healthcare, RitualFuneral, SocialServices, Utilities], main_category)
      if None != result: return result
         
      return None

categories = __ConstCategories()





"""

var list = document.getElementsByClassName('category-list').item(0).children.item(0).children
var result = ''
for (let block of list) {
    var node = block.children.item(0).children.item(0)
    var title = node.text
    var url = node.href.slice(0, -1)
    var cid = url.substring(url.lastIndexOf('/') + 1)

    var list = block.children.item(1).children
    var mainKey = title.replaceAll('\n', '').replaceAll(' ', '')
    var mainValue = cid.replaceAll('\n', '')
    var dictName = mainValue.replaceAll('-', '_')
    result += '\n# ' + mainKey + ' ' + mainValue + '\n'
    result += 'class ' + mainValue + '(object):\n'
    result += '   def ' + dictName + '() -> Dict[str, Dict[str, str]]:\n'
    result += '      list = {}\n'
    result += "      list['name'] = '" + mainKey + "'\n"
    result += "      list['id'] = '" + mainValue + "'\n\n"
    result += '      ' + dictName + ' = {}\n'

    for (let item of list) {
       var targer = item.querySelector('a')
        var name = targer.text.replaceAll('\n', '').replaceAll('  ', '')
        var path = targer.href.substring(targer.href.lastIndexOf('/') + 1).slice(0, -5)
        result += '      ' + dictName + "['" + path + "'] = '" + name + "'\n"
    }
    result += "\n      list['sub'] = " + dictName
    result += '\n      return list\n'
}

console.log(result)



"""
