#-*- coding: UTF-8 -*-
import pymongo
import talib
import numpy

con=pymongo.MongoClient('10.105.21.158',27017)
db=con.bntest
ss=db["ss"]
#print(ss.count({'Date':'2010-01-14'}))


def GetAllCode():
	return ss.distinct("Code");

def Calc(code):
	allData=[];
	allAdj=[];
	cursor=ss.find({"Code":code,'Volume':{"$gt":0}},{"AdjClose":1}).sort([("Date",1)])#.limit(100);
	for c in cursor:
		#print(c);
		allData.append(c);
		allAdj.append(c["AdjClose"]);

	ma1Result_5 = talib.MA(numpy.array(allAdj),5,matype=0);
	ma1Result_10 = talib.MA(numpy.array(allAdj),10,matype=0)
	ma1Result_20 = talib.MA(numpy.array(allAdj),20,matype=0)

	l=len(allData);
	for x in range(0,l):
		ss.update({"_id":allData[x]['_id']},{"$set":{"M_5":ma1Result_5[x],"M_10":ma1Result_10[x],"M_20":ma1Result_20[x]}})
		#allData[x]["M_5"]=ma1Result_5[x];
		#allData[x]["M_10"]=ma1Result_10[x];
		#allData[x]["M_20"]=ma1Result_20[x];
	#print(allData)
	return

def SetM_X_Values():
	allCodes=GetAllCode();
	for co in allCodes:
		Calc(co)
	return

def Get_Through(d=10,target=0.1):
	tlist=[];
	oklist=[];
	max_min_list=[];
	v_max_rate_list=[];	
	v_mim_rate_list=[];
	cursor=ss.find({"$where":"this.Open<this.Close&&this.Open<this.M_5&&this.Close>this.M_5&&this.Open<this.M_10&&this.Close>this.M_10&&this.Open<this.M_20&&this.Close>this.M_20&&this.Volume>0"},{"_id":0,"Code":1,"Date":1,"AdjClose":1})#.limit(10);
	for c in cursor:
		tlist.append(c);

	for c in tlist:
		next_x_days=ss.find({"Code":c["Code"],"Date":{"$gt":c["Date"]},'Volume':{"$gt":0}},{"_id":0,"High":1,'Low':1}).sort([("Date",1)]).limit(d);
		v_max=0;
		v_min=1000;
		for n in next_x_days:
			if(n['High']>v_max):
				v_max=n['High'];
			if(n['Low']<v_min):
				v_min=n['Low'];			
		v_max_rate=(v_max-c['AdjClose'])/c['AdjClose']
		v_mim_rate=(v_min-c['AdjClose'])/c['AdjClose']
		v_max_rate_list.append(v_max_rate)
		v_mim_rate_list.append(v_mim_rate)
		if(v_max_rate>=target):
			oklist.append(c);

	return (len(tlist),len(oklist),v_max_rate_list,v_mim_rate_list);

def GetSummary(rate,r=True):
	rate.sort(reverse=r);
	total=len(rate);
	summary=[];
	for x in range(1,10):
		index=int(x*0.1*total-1);
		summary.append("{0:.0f}%".format(x*0.1*100)+' history :>'+str("{0:.0f}%".format(rate[index]*100)))		
	return summary
#SetM_X_Values();
tlist=Get_Through();
#print(tlist);
print(tlist[0])
print(tlist[1])
print("Max rate")
print(GetSummary(tlist[2]))
print("Min rate")
print(GetSummary(tlist[3],False))
#print(tlist[3])
print('done')