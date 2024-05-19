score = int(input("enter a score:"))
if score < 35:
    print("poor student")
elif score > 35 and score < 70:
    print("average student")
else:
    print("good student")