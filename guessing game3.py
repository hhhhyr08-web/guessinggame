numbers=[5,20,50,120,8,75]
for number in numbers:
    if number <=10:
        print(number,":easy")
    elif 10< number <= 40:
        print(number,":hard")
    elif 40< number <= 100:
        print(number,":very hard")
    else:
        print(number,":impossible")
