class const():

	class ConstError(TypeError):
		pass
	class ConstCaseError(ConstError):
		pass

	def __setattr__(self, name, value):
		if name in self.__dict__:
			raise self.ConstError("can't change const(%s)"%name)
		if not name.isupper():
			raise self.ConstCaseError('const name is not all uppercase')
		self.__dict__[name] = value

import sys
sys.modules[__name__] = const()