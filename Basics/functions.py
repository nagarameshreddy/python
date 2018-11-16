print("Functions")

def helloworld():
    print("Hello world")
helloworld()
helloworld()
def addab(a,b):
    print(a,'+',b,'=',a+b)
def subab(a,b):
    print(a,'-',b,'=',a-b)
def mulab(a,b):
    print(a,'X',b,'=',a*b)
a = int(input("Input a number: "))
b = int(input("Input another number: "))

def returnadd(a,b):
    return(a+b)

addab(a,b)
subab(a,b)
mulab(a,b)
sum=returnadd(a,b)
print(sum)