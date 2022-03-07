print('If Statements Practice')
marks = 20
# if statement block
if marks == 35:
    print(f"You are promoted with marks : {marks}")
elif marks > 35:
    print(f"You are passed with marks : {marks}  \n and ")
    if marks > 35 and marks <= 60:
        print("You Got Second Class")
    elif marks >60 and marks <= 80:
        print("You Got first class")
    elif marks > 80 and marks <= 100:
        print("Your One of the best in class")
else:
    print(f"Failed!, Better luck next time \n secured marks : {marks}")

