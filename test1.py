# -*- coding: UTF-8 -*-
name=raw_input("\n\n enter some value")

if name=="aa":
	print 'this is aa'
else:
	name+=" other"
	print name
#print name


#string
print "-------------------------string---------------------------------"
s='ilovepython'
print s[0]	#i
print s[1:5] #love
print s[2:] #lovepython
print s*2 #ilovepythonilovepython
print s+"test" #ilovepythontest

#array
print "-------------------------array---------------------------------"
list=['abc',123,45.0,'json',789]
tinylist=[123,'josn']
print list
print list[1]
print list[1:3]
print list[1:]
print tinylist *2
print list+tinylist

if('abc' in list):
	print 'abc'+' is in the list'
else:
	print 'abc'+' is not in the list'

#tuple
print "-------------------------tuple 元组---------------------------------"
tuple=('abc',123,45.0,'json',789)
tinytuple=(123,'josn')
print tuple
print tuple[1]
print tuple[1:3]
print tuple[1:]
print tinytuple *2
print tuple+tinytuple


#dic
print "-------------------------dictionnary---------------------------------"
dic={};
dic["one"]="this is one"
dic[2]='this is two'
tinydic={'name':'john','age':22,'dept':'sales'}
print dic['notfound']
print dic['one']
print dic.keys()
print tinydic.keys()
print tinydic.values()


#conver 
print "-------------------------data convert---------------------------------"
t_int=int('1');
print t_int
print str(t_int)
#print list(('ad',13,'df'))


#calc
print "-------------------------calc-----------------------------------------"
a=10
b=20
print a**b #a**b 为10的20次方， 输出结果 100000000000000000000
print 9//2 #9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
raw_input("\n\n press the enter key to exit")