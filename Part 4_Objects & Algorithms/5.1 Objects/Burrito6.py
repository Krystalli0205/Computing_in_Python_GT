#In this exercise, you won't edit any of your code from the
#Burrito class. Instead, you're just going to write a
#function to use instances of the Burrito class. You don't
#actually have to copy/paste your previous code here if you
#don't want to, although you'll need to if you want to write
#some test code at the bottom.
#
#Write a function called total_cost. total_cost should take
#as input a list of instances of Burrito, and return the
#total cost of all those burritos together as a float.
#
#Hint: Don't reinvent the wheel. Use the work that you've
#already done. The function can be written in only five
#lines, including the function declaration.
#
#Hint 2: The exercise here is to write a function, not a
#method. That means this function should *not* be part of
#the Burrito class.


#If you'd like to use the test code, paste your previous
#code here.

class Burrito:

    def __init__(self, meat, to_go, rice, beans, extra_meat = False, guacamole = False, cheese = False, pico = False, corn = False):
        self.meat = Meat(meat)
        self.rice = Rice(rice)
        self.beans = Beans(beans)
        self.set_to_go(to_go)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)

    valid_meat = ["chicken", "pork", "steak", "tofu", False]
    valid_rice = ["brown", "white", False]
    valid_beans = ["black", "pinto", False]

    

    def get_meat(self):
        return self.meat.get_value()
    
    def set_meat(self, new_meat):
        self.meat.set_value(new_meat)

    def get_to_go(self):
        return self.to_go
    
    def set_to_go(self, new_to_go):
        if isinstance(new_to_go, bool):
            self.to_go = new_to_go
        else:
            self.to_go = False
    
    def get_rice(self):
        return self.rice.get_value()

    def set_rice(self, new_rice):
        self.rice.get_value(new_rice)

    def get_beans(self):
        return self.beans.get_value()

    def set_beans(self, new_beans):
        self.beans.set_value(new_beans)
    
    def get_extra_meat(self):
        return self.extra_meat

    def set_extra_meat(self, new_meat):
        if isinstance(new_meat, bool):
            self.extra_meat = new_meat
        else:
            self.extra_meat = False

    def get_guacamole(self):
        return self.guacamole

    def set_guacamole(self, new_guac):
        if isinstance(new_guac, bool):
            self.guacamole = new_guac
        else:
            self.guacamole = False

    def get_cheese(self):
        return self.cheese

    def set_cheese(self, new_cheese):
        if isinstance(new_cheese, bool):
            self.cheese = new_cheese
        else:
            self.cheese = False

    def get_pico(self):
        return self.pico

    def set_pico(self, new_pico):
        if isinstance(new_pico, bool):
            self.pico = new_pico
        else:
            self.pico = False

    def get_corn(self):
        return self.corn

    def set_corn(self, new_corn):
        if isinstance(new_corn, bool):
            self.corn = new_corn
        else:
            self.corn = False

    def get_cost(self):
        base_cost = 5
        meat_val = self.get_meat()
        if meat_val in ["chicken", "pork", "tofu"]:
            base_cost += 1
        elif meat_val == "steak":
            base_cost += 1.5
        if self.get_extra_meat() and meat_val != False:
            base_cost += 1
        if self.get_guacamole():
            base_cost += 0.75
        return float(base_cost)

class Meat:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["chicken", "pork", "steak", "tofu"]:
            self.value = value
        else:
            self.value = False

class Rice:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["brown", "white"]:
            self.value = value
        else:
            self.value = False
            
class Beans:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["black", "pinto"]:
            self.value = value
        else:
            self.value = False
            
#Write your new function here.

def total_cost(burrito_list):
    total_cost = 0
    for burrito in burrito_list:
        total_cost += burrito.get_cost()
    
    return total_cost


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs. Note that these lines
#will ONLY work if you copy/paste your Burrito, Meat,
#Beans, and Rice classes in.
#
#If your function works correctly, this will originally
#print: 28.0
burrito_1 = Burrito("tofu", True, "white", "black")
burrito_2 = Burrito("steak", True, "white", "pinto", extra_meat = True)
burrito_3 = Burrito("pork", True, "brown", "black", guacamole = True)
burrito_4 = Burrito("chicken", True, "brown", "pinto", extra_meat = True, guacamole = True)
burrito_list = [burrito_1, burrito_2, burrito_3, burrito_4]
print(total_cost(burrito_list))



