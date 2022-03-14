############################
#                          #
#   Print sum of 1 to N    #
#                          #
############################

n = int(input('Enter the last number : '))
x = n
sumf = 0
# using for loop
for x in range(1, n+1):
    sumf += x

print(" Sum of 1 to {} is {} Using For Loop".format(str(n), str(sumf)))

# using while loop
sumw = 0
while n > 0:
    sumw += n
    n -= 1
n = x
print(" Sum of 1 to {} is {} Using While Loop".format(str(n), str(sumw)))

# using formula

n = x
# using formula
sumFomula = (n * (n + 1))/2
print(" Sum of 1 to {} is {} Using Formula  (n * (n + 1))/2".format(str(n), str(sumFomula)))

def SumOfN(n):
    sum_of_n = (n * (n + 1))/2
    print(" Sum of 1 to {} is {} Using Custom Function".format(str(n), str(sum_of_n)))

SumOfN(n)
