odd = 0
even = 0
for i in range(1,21):
    if i % 2 == 0:
        even = even + 1
    if i % 2 != 0:
        odd = odd + 1
print(even)
print(odd)

