print("Sorting and isinstance")
lista=[1,28,3.0,2,100,10,5,'test',3,4,5.0,7.0,'test1','test2',22.444444333]
listb=[]
listc=[]
listd=[]
for i in lista:
	if(isinstance(i,int)):
		listb.append(i)
	elif(isinstance(i,float)):
		listc.append(i)
	else:
		listd.append(i)
print(lista)
print("Integer List",listb)
print("Sorted Integer List",sorted(listb))
print("Sorted Interger List in reverse order",sorted(listb,reverse=True))
print("Float List",listc)
print("String List",listd)

