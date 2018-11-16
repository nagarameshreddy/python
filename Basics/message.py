import datetime
print("Message for list of memebers")
names1=['Justin','Ross','john','emile']
amounts1=[10,20,30,40]

#print(names1)
#print(amounts1)
msg1=""" Hi {name}!
 test Message. Your price is {amount}.
 on date {today_date}"""



def messagefunc(names,amounts):
 	messages=[]
 	if len(names)==len(amounts):
 		i=0
 		for name in names:
 			new_msg=msg1.format(name=name.capitalize(),amount=amounts[i],today_date=datetime.datetime.now())
 			print(new_msg)
 			i += 1
messagefunc(names1,amounts1)