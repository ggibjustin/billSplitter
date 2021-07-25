# the list "walks" is already defined
# your code here
total = 0
for i in walks:
    total += i.get("distance")

print(int(total / len(walks)))
