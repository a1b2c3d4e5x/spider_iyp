
from .constant import constant

class __ConstColor(object):
   @constant
   def PURPLE():
      return '\033[95m'

   @constant
   def CYAN():
      return '\033[96m'

   @constant
   def DARKCYAN():
      return '\033[36m'

   @constant
   def BLUE():
      return '\033[94m'

   @constant
   def GREEN():
      return '\033[92m'

   @constant
   def YELLOW():
      return '\033[93m'

   @constant
   def RED():
      return '\033[91m'

   @constant
   def BOLD():
      return '\033[1m'

   @constant
   def UNDERLINE():
      return '\033[4m'

   @constant
   def END():
      return '\033[0m'

color = __ConstColor()



