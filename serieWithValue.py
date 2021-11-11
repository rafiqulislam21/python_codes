n = int(input("Enter the last number : "))

sumVal = 0
#avoid builtin names, here sum is a built in name in python
for x in range(1, n+1, 1):
# here for x in range(1 = start value, n = end value, 1 = increasing value)
    if x != n:
        print(str(x)+" + ", end =" ") #this line will show 1+2+3+............
        # end = " " means print will show with ount line break
        sumVal = sumVal + x #this line will calculate sum 1+2+3+............
    else:
        print(str(x) + " = ", end=" ")#this line will show last value of series 5 = ............
        sumVal = sumVal + x
print(sumVal) #this line will show final sum result of series............
