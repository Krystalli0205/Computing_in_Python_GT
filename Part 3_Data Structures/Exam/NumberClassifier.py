#Write a function called classify_numbers. classify_numbers should
#take as input a list. You may assume every item in the list will
#be an integer.
#
#classify_numbers should return a dictionary with the following
#five keys: evens, odds, positives, negatives, zeros
#
#The values associated with those keys should be the number of
#times each type of number appears in the list.
#
#For example:
#
#classify_numbers([-2, -1, 0, 1, 2]) ->
#{"evens": 3, "odds": 2, "positives": 2, "negatives": 2, "zeros": 1}
#
#Note that every number in the list will be counted twice: once
#as either even or odd, and once as either positive, negative,
#or zero. 0 should be considered an even number. If a type of
#number never appears, the key should still appear with a value of
#0.


#Write your function here!

def classify_numbers(a_list):
    even_count = 0
    odd_count = 0
    positive_count = 0
    negative_count = 0
    zero_count = 0
    for num in a_list:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1

    return {"evens": even_count, "odds": odd_count, "positives": positive_count, "negatives": negative_count, "zeros": zero_count}

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#
#{"evens": 3, "odds": 2, "positives": 2, "negatives": 2, "zeros": 1}
#{"evens": 3, "odds": 4, "positives": 6, "negatives": 0, "zeros": 1}
print(classify_numbers([-2, -1, 0, 1, 2]))
print(classify_numbers([8, 6, 7, 5, 3, 0, 9]))


