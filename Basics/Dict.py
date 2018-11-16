print("Dictionaries")

students = {"Ram":5,"Vijay":7, "Sam":9}

print(students)

print(students["Ram"])

print(students["Vijay"])

print(students["Sam"])
print("size of Dictionary")
print(len(students))
students['new']=5
print("size of Dictionary")
print(len(students))

print("update dictionary")
students["Ram"]=10
print(students)
del students["Ram"]
print(students)


print("-------------------------------------------------")
students["test"]=students
print(students)
print("-------------------------------------------------")
print(students["test"])