# -*- coding: UTF-8 -*-

class Person(object):
	"""docstring for Person"""
	def __init__(self, name):
		self.name = name+"Person"
	def getName(self):
		return "from Person";
	def getTest(self):
		return "test from Person";	
class Person2(object):
	"""docstring for Person2"""
	def __init__(self, arg,agr2):
		super(Person2, self).__init__()
		self.name2 = arg+"Person2"
	def getName(self):
		return "from Person2";					


class Employee(Person,Person2):
	"""docstring for Employee"""
	#private私有变量
	__count=0;
	#public变量
	empCount=0;
	#static 类变量 --->Employee.empCount2+=1;
	empCount2=0

	#构造函数
	def __init__(self, name,salary):
		super(Employee, self).__init__(name);
		self.salary=salary;
		Employee.empCount2+=1;
		self.empCount+=1;
		self.__count+=1;

	def __testPrivateMethod():
		return 1;
	def displayCount(self):
		print("-------------")
		print(str(self.empCount2));
		print(str(self.empCount));
		print(str(self.__count));
		print("-------------")
	def displayEmployee(self):
		print("Name:"+self.name+", Salary:"+str(self.salary));
		#print("arg:"+self.name2) #由于应用了Person的构造函数， 所以person2.name2 未实现
		
	#方法重载
	def getTest(self):
		return "test from Employee";

	#操作符重载
	def __str__(self):
		return "toString override Name:"+self.name;


	#析构函数
	def __del__(self):
		cname=self.__class__.__name__
		print(cname+"销毁")

emp1=Employee('a',100);
emp2=Employee('b',200);

emp1.displayEmployee();
emp2.displayEmployee();
emp1.displayCount();
emp2.displayCount();
print(str(Employee.empCount))
print(str(emp1.empCount))
print(isinstance(emp1,Person))
print(isinstance(emp1,Person2))
print(emp1.getName())#多重继承，从左往右找,(supper 查找规则一样)
print(emp1.getTest())#重载
print(emp1)
#del emp1
'''
print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__
'''
