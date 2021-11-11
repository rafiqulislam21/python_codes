n = int(input("Enter the last number : "))

sumVal = 0
#avoid builtin names, here sum is a built in name in python
for x in range(1, n+1, 1):
# here for x in range(1 = start value, n = end value, 1 = increasing value)
    sumVal = sumVal + 1
print(sumVal)
