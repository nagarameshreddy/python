print ("test")
A,B=5,20
C="test"
print(A)
print("A=" +str(A))
print("A=%d and B=%d and C=%s" %(A,B,C))
print("SUme of %d and %d is %d" %(A,B,A+B))
if A<5:
	print ("Value of A is %d" %(A))
elif A>5:
	print ("Value of A(%d) is greater than 5" %(A))
else:
	print ("Value of A is 5")


while A<8:
	print(A)
	A=A+1

names=["test","test1","test2"]
for Name in names:
	print("Name:" +str(Name))
print(type(A))
A=True
print(A)
print(type(A))

for i in range(10):
	print(i)
x=10 if A>B else 20
print(x)
x=10 if B>A else 20
print(x)
import keyword
print(keyword.kwlist)
#Address of object
print(id(A))

C=5.1
print(type(C))
D=23424234987777777777777666666
print(type(D))
D=2.342423498777777777777766666699999
print(type(D))
print("----------Binary-------------")
E=0b1111
print(type(E))
print(E)
print("--------Binary---------------")
E=0B1111
print(type(E))
print(E)
print("------------Octal---------------")
E=0o1111
print(type(E))
print(E)
E=0O1111
print(type(E))
print(E)

print("------------Hexa---------------")
E=0xFac2
print(type(E))
print(E)
E=0XFac2
print(type(E))
print(E)

print(0XFac2)