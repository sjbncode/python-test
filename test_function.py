#-*- coding: UTF-8 -*-

# define a function
def log(msg):
	"打印日志"
	print (msg);
	return;

def testPassValue(a):
	"传入参数 对外部影响测试"
	a*=2;
	print (a);

# 可变参数是一个元祖类型
def testParamter(arg1,agr2=30,*otherParas):
	"函数参数,默认参数->可变参数"
	print ('--------testParamter begin------------')
	print (arg1)
	print (agr2)
	for x in otherParas:
		print (x)
	print (otherParas)
	print ('--------testParamter end  ------------')
	return;

# invoke function
# name1=input("\n\n enter some value")
log('abc')

raw="ww";
testPassValue(raw);
log(raw)

raw_ref=[123,122,333];
testPassValue(raw_ref);
log(raw_ref);

testParamter(10)
testParamter(10,20,30,40);

#lambda 表达式  lambda [arg1 [,arg2,.....argn]]:expression
#lambda函数的语法只包含一个语句
sum=lambda a1,a2:a1+a2;

log(sum(1,3))