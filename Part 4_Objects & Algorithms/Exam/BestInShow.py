#Write a function called select_from_list. select_from_list
#should have two parameters: a list of integers and a list
#of strings.
#
#The list of integers represents the indices of the items to
#remove from the list of strings and add to a separate list.
#The function should return a 2-tuple with two lists; the first
#list should be the items that were selected based on their
#indices, the second list should be those left over that were
#not selected.
#
#For example:
#
# select_from_list([0, 1, 4, 5], ["a", "b", "c", "d", "e", "f"])
#
#...would return the following tuple:
#
# (["a", "b", "e", "f"], ["c", "d"]). Note that the indices 0, 1,
#4, and 5 correspond to the values "a", "b", "e", and "f", and so
#those letters are in the first list; "c" and "d" are left over
#and thus included in the second list.
#
#You may assume that there are no duplicate items in the list
#of strings.
#
#There is more than one way to do this, so if you find yourself
#struggling with one way, try a different one!


#Write your function here!
def select_from_list(list_int, list_string):
    list_1 = []
    list_2 = []

    remove_indices = set(list_int)

    for index, char in enumerate(list_string):
        if index in remove_indices:
            list_1.append(char)
        else:
            list_2.append(char)
    
    return (list_1, list_2)
    



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#(['a', 'b', 'e', 'f'], ['c', 'd'])
#(['c', 'd'], ['a', 'b', 'e', 'f'])
print(select_from_list([0, 1, 4, 5], ["a", "b", "c", "d", "e", "f"]))
print(select_from_list([2, 3], ["a", "b", "c", "d", "e", "f"]))



