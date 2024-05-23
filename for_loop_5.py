div_by_3 = 0
div_by_5 = 0
for i in range(1,101):
    if i % 3 == 0:
        div_by_3 = div_by_3 + 1
    if i % 5 == 0:
        div_by_5 = div_by_5 + 1
print(div_by_3)
print(div_by_5)
