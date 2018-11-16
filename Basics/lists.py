print("lists")

shoplist = ["Apples" , "Bananas" , "manogs" , "Grapes"]

print(shoplist)
print("\n")
print("First element of list")
print(shoplist[0])
print("\n")
print("4th element of list")
print(shoplist[3])
print("\n")
print("up to 2nd element in list")
print(shoplist[:2])
print("\n")
print("Elements between 2nd and 4th")
print(shoplist[1:3])
print("\n")
print("Append one more element in list")
print(shoplist)
shoplist.append("oranges")
print(shoplist)
print("\n")
print("Replace existing items in list")
shoplist[0] = "Blueberries"
print(shoplist)
print("\n")
print("delete item from list")
print(shoplist)
del shoplist[1]
print(shoplist)
print("length of list")
print(len(shoplist))

print(shoplist*2)

shoplist1 = ["cricket", "soccer" , "Tennis"]
print("\n")
print(shoplist1)


print("append two lists")

print(shoplist+shoplist1)

list1=[1,2,3,4,6,7,8,9]
print(list1)
print("-------------------------------------------------")
print("length of list",len(list1))
print("Highest value in list",max(list1))
print("lowet value in list",min(list1))

#to delete last item from list
list1.pop()
print("after deleting the last element from list",list1)

list1.pop(4)
print("After deleteion of 5th element from list",list1)