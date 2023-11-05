import random

#Part A
weeks = 16
print("Weeks:",weeks)
classes = 5
print("Classes:",classes)
tuition = 6000
print("Tuition:",tuition)
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 3
print("Classes per week:" , classes_per_week)
cost_per_class = (cost_per_week / classes_per_week)
print("Cost per class:", cost_per_class)


#Part B
myList = ['a',65,'o',"star",3]

rndObj = random.choice(myList)

print("\nRandom Object:",rndObj)