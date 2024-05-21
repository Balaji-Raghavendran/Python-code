batsman = input("enter your name:")
score = int(input("enter your last match score:"))
if score >= 65:
    average = float(input("enter your batting avg:"))
    if average >= 50:
        strikerate = float(input("enter your strikerate:"))
        if strikerate >= 135:
            print("you are selected for the team")
        else:
            print("your strikerate is less")
    else:
        print("your average is less")
else:
    print("your score is less")
