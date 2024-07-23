slices_per_pizza = 6
pizzas = 3
students = 4

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Imagine you are throwing a pizza party for some students.
#You order some number of pizzas, each with some number of
#slices. You want each student to receive the same number
#of slices, even if that means some slices are left over.
#
#The number of pizzas, number of slices per pizza, and
#number of students are given by the variables
#slices_per_pizza, pizzas, and students. Using this information,
#write some code that prints out a sentence like the following:
#
#Each student gets 4 slices, and there will be 2 left over.
#
#The number of slices per person will be calculated as the total
#number of slices (number of pizzas times slices per pizza)
#divided by the number of students rounded down to a whole
#number. The number of slices left over will be whatever is left
#after that calculation.


#Write your code here!
per_slice = slices_per_pizza * pizzas // students
left = slices_per_pizza * pizzas % students
print("Each student gets {} slices, and there will be {} left over.".format(per_slice, left))