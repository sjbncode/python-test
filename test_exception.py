#-*- coding: UTF-8 -*-

class BnException(Exception):
	"""docstring for BnException"""
	def __init__(self, arg):
		super(BnException, self).__init__(arg)
		self.arg = arg

class BN(BnException):
	"""docstring for BN"""
	def __init__(self, arg):
		super(BN, self).__init__(arg)
		self.arg = arg
		


try:
	fs=open("test2","w");
	fs.write("write something")
	
	raise BN('aba')

except Exception as e:
	print(e)
	#raise
else:
	print("OK")
finally:
	print("finally")