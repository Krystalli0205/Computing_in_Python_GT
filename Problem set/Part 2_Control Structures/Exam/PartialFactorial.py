minimum = 2
maximum = 5

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Print the result of multiplying every number from minimum to
#maximum, including both minimum and maximum.
#
#For example, if minimum = 2 and maximum = 5, you would print
#120: 2 * 3 * 4 * 5 = 120.
#
#You may assume minimum will always be less than
#maximum.


#Add your code here!

product = 1
for num in range(minimum, maximum+1):
    product *= num

print(product)