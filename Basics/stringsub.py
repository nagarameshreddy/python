print("String Substitution")
print("This is {var} string".format(var="cool"))
print("This is {var1} string".format(var1="Very cool"))
print("This is {0} {1}".format('test','msg'))
var2="this is {0} {1} {2}"
print("var2 =",var2.format('very','cool','msg'))

var3="this is {var} {var1}"
print(var3.format(var="cool",var1="String"))


print("String Substitution using %")

print("This is %s msg"%("test"))
print("This is Integer %d" %(5))
print("This Float value of 12.3123 with 2 decimal %.2f" %(12.3123))
print("This Float value of 12.3123 with 5 decimal %.5f" %(12.3123))
