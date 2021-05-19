from typing import Dict
from ..base_category import BaseCategory

# 金融服務 finance
class Finance(object):
   def finance() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '金融服務'
      list['id'] = 'finance'

      finance = {}
      finance['banks'] = '銀行'
      finance['credit-unions'] = '信用合作社'
      finance['financial-service'] = '金融服務'

      list['sub'] = finance
      return list

# 投資理財 investment
class Investment(object):
   def investment() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '投資理財'
      list['id'] = 'investment'

      investment = {}
      investment['invest-service'] = '投資服務'
      investment['trust-service'] = '信託服務'
      investment['insurance'] = '保險'
      investment['bills-finance'] = '票券金融'

      list['sub'] = investment
      return list

# 不動產投資管理 real-estate
class RealEstate(object):
   def real_estate() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '不動產投資管理'
      list['id'] = 'real-estate'

      real_estate = {}
      real_estate['agents'] = '房地產仲介'
      real_estate['escrow-service'] = '代書、地政士'

      list['sub'] = real_estate
      return list

# 貿易工商服務 trade-service
class TradeService(object):
   def trade_service() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '貿易工商服務'
      list['id'] = 'trade-service'

      trade_service = {}
      trade_service['business-service'] = '工商服務'
      trade_service['telemarketing'] = '市調、電話行銷'
      trade_service['property-management'] = '建築經理'
      trade_service['rental-service'] = '租賃'
      trade_service['product-design'] = '產品設計'
      trade_service['trading'] = '貿易'
      trade_service['direct-marketing'] = '直銷'

      list['sub'] = trade_service
      return list

# 顧問諮詢 consultant
class Consultant(object):
   def consultant() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '顧問諮詢'
      list['id'] = 'consultant'

      consultant = {}
      consultant['PR'] = '公關顧問'
      consultant['engineer'] = '技師、工程師'
      consultant['construction'] = '土木工程顧問'
      consultant['industrial-safety'] = '工業技師、工安技師'
      consultant['electrical'] = '電機'
      consultant['invest-financial'] = '投資財務顧問'
      consultant['environmental'] = '環境工程'
      consultant['business-admin'] = '企業管理顧問'

      list['sub'] = consultant
      return list

# 律師 lawyer
class Lawyer(object):
   def lawyer() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '律師'
      list['id'] = 'lawyer'

      lawyer = {}
      lawyer['lawyers'] = '律師'

      list['sub'] = lawyer
      return list

# 會計師 accountant
class Accountant(object):
   def accountant() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '會計師'
      list['id'] = 'accountant'

      accountant = {}
      accountant['accountants'] = '會計師'

      list['sub'] = accountant
      return list

# 稅務帳務代理 booking-service
class BookingService(object):
   def booking_service() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '稅務帳務代理'
      list['id'] = 'booking-service'

      booking_service = {}
      booking_service['receivable-management'] = '應收帳款管理'
      booking_service['bookkeepers'] = '記帳士'

      list['sub'] = booking_service
      return list

# 專利商標代理 patent-and-trademark
class PatentAndTrademark(object):
   def patent_and_trademark() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '專利商標代理'
      list['id'] = 'patent-and-trademark'

      patent_and_trademark = {}
      patent_and_trademark['intellectual-property'] = '專利、智財'

      list['sub'] = patent_and_trademark
      return list

# 人力仲介 recruitment-agency
class RecruitmentAgency(object):
   def recruitment_agency() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '人力仲介'
      list['id'] = 'recruitment-agency'

      recruitment_agency = {}
      recruitment_agency['employment-service'] = '人力仲介'

      list['sub'] = recruitment_agency
      return list

# 翻譯移民服務 immigrationservices
class Immigrationservices(object):
   def immigrationservices() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '翻譯移民服務'
      list['id'] = 'immigrationservices'

      immigrationservices = {}
      immigrationservices['migration-service'] = '移民服務'
      immigrationservices['translation-service'] = '翻譯服務'

      list['sub'] = immigrationservices
      return list

# 徵信社 credit-information
class CreditInformation(object):
   def credit_information() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '徵信社'
      list['id'] = 'credit-information'

      credit_information = {}
      credit_information['credit-report'] = '徵信社'

      list['sub'] = credit_information
      return list

# 資料處理 data-processing
class DataProcessing(object):
   def data_processing() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '資料處理'
      list['id'] = 'data-processing'

      data_processing = {}
      data_processing['data-processing'] = '資料處理'

      list['sub'] = data_processing
      return list

# 會議商展 conference-expo
class ConferenceExpo(object):
   def conference_expo() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '會議商展'
      list['id'] = 'conference-expo'

      conference_expo = {}
      conference_expo['exhibition-service'] = '展覽服務'
      conference_expo['conference-centers'] = '會議中心'

      list['sub'] = conference_expo
      return list

# ＳＯＨＯ族工作室 soho-studio
class SohoStudio(object):
   def soho_studio() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = 'ＳＯＨＯ族工作室'
      list['id'] = 'soho-studio'

      soho_studio = {}
      soho_studio['studio'] = '個人工作室'

      list['sub'] = soho_studio
      return list

# 公證 notary
class Notary(object):
   def notary() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '公證'
      list['id'] = 'notary'

      notary = {}
      notary['notary-service'] = '公證服務'

      list['sub'] = notary
      return list

# 命理堪輿 fortune-teller
class FortuneTeller(object):
   def fortune_teller() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '命理堪輿'
      list['id'] = 'fortune-teller'

      fortune_teller = {}
      fortune_teller['fortune-telling'] = '命理卜卦'
      fortune_teller['geomancy'] = '擇日、堪輿'

      list['sub'] = fortune_teller
      return list

# 典當質押 pawn-service
class PawnService(object):
   def pawn_service() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '典當質押'
      list['id'] = 'pawn-service'

      pawn_service = {}
      pawn_service['pawnshops'] = '當舖'

      list['sub'] = pawn_service
      return list

# 免稅商店 duty-free-shops
class DutyFreeShops(object):
   def duty_free_shops() -> Dict[str, Dict[str, str]]:
      list = {}
      list['name'] = '免稅商店'
      list['id'] = 'duty-free-shops'

      duty_free_shops = {}
      duty_free_shops['duty-free-shops'] = '免稅商店'

      list['sub'] = duty_free_shops
      return list

# 金融工商 financial
class Financial(BaseCategory, Finance, Investment, RealEstate, TradeService, Consultant, Lawyer,
Accountant, BookingService, PatentAndTrademark, RecruitmentAgency, Immigrationservices,
CreditInformation, DataProcessing, ConferenceExpo, SohoStudio, Notary, FortuneTeller,
PawnService, DutyFreeShops):
   category_name = '金融工商'
   category_id = 'financial'