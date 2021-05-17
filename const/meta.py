
from .constant import constant

class __ConstMeta(object):
	@constant
	def BUILD_DATE():
		return '2021-05-20'

	@constant
	def BUILD_VERSION():
		return '0.0.1'

	@constant
	def DEVERPER_NAME():
		return 'Guo Hao Chen'

	@constant
	def DEVERPER_EMAIL():
		return 'a1b2c3d4e5x@gmail.com'

meta = __ConstMeta()
