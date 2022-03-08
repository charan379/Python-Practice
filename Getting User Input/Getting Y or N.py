# Geting Yes(Y) or No(N) from user

choice = str(input("Please enter y / n :  ")[0]).strip().lower()
while (len(choice) != 1 or choice.isalpha() == False) or choice not in ['y','n']:
    print("Please enter only a single character \n y for yes \n n for no ")
    choice = input("Please enter y / n :  ")

print(choice.isalpha())
print(choice)