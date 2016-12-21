#-*- coding: UTF-8 -*-

import support
import bnUtils
#返回的列表容纳了在一个模块里定义的所有模块，变量和函数
#print dir(support)
bnUtils.log_error('xxxx')
support.log_error('xxxx')
support.log_debug('xxxx')

print(globals().keys())
print(locals().keys())
#from support import *
#from support import log_error,log_info
#log_error('xxxx')