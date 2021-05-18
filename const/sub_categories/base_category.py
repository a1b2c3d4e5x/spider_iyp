
from typing import List

class BaseCategory(object):
   def list(self) -> List[str]:
      all = []

      method_list = [method for method in dir(self) if method.startswith('_') is False]
      for item in method_list:
         if 'category_name' == item:
            continue
         elif 'category_id' == item:
            continue
         elif BaseCategory.list.__name__ == item:
            continue
         all.append(item)
      return all