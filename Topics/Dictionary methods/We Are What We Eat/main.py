# the list "meals" is already defined
# your code here
cals = 0
for i in meals:
    cals += i.get("kcal")

print(cals)
