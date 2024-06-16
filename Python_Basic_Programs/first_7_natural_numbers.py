a = []
print("type first 7 natural numbers")
for i in range(7):
    num = int(input("enter num" + str(i + 1)))
    a.append(num)
print(a)

add = 0
for i in a:
    add = add + i
print(add) 