#Write a function called highest_number. highest_number should
#have one parameter: a string representing a filename. Inside
#the file, there will be a list of numbers separated by commas
#on each line. In the dropdown box in the top left, you may
#select a_few_numbers.txt to see an example of such a file.
#
#highest_number should return the highest number found in the
#file. For example, for the contents of a_few_numbers.txt, the
#highest number is 99, the second-to-last value on the second
#line.


#Write your function here!

def highest_number(filename):
    highest_num = 0
    file = open(filename, "r")
    for line in file:
        list = line.strip().split(",")
        for num in list:
            num = int(num)
            if num > highest_num:
                highest_num = num
    file.close()
    return highest_num


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 99
print(highest_number("a_few_numbers.txt"))


