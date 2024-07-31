#Copy your Burrito class from the last exercise. Now, add
#a method called "get_cost" to the Burrito class. It should
#accept zero arguments (except for "self", of course) and
#it will return a float. Here's how the cost should be
#computed:
#
# - The base cost of a burrito is $5.00
# - If the burrito's meat is "chicken", "pork" or "tofu", 
#   add $1.00 to the cost
# - If the burrito's meat is "steak", add $1.50 to the cost
# - If extra_meat is True and meat is not set to False, add
#   $1.00 to the cost
# - If guacamole is True, add $0.75 to the cost
#
#Make sure to return the result as a float even if the total
#is a round number (e.g. for burrito with no meat or
#guacamole, return 5.0 instead of 5).


#Write your code here!

class Burrito:

    def __init__(self, meat, to_go, rice, beans, extra_meat = False, guacamole = False, cheese = False, pico = False, corn = False):
        self.set_meat(meat)
        self.set_to_go(to_go)
        self.set_rice(rice)
        self.set_beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)

    valid_meat = ["chicken", "pork", "steak", "tofu", False]
    valid_rice = ["brown", "white", False]
    valid_beans = ["black", "pinto", False]

    

    def get_meat(self):
        return self.meat
    
    def set_meat(self, new_meat):
        if new_meat in self.valid_meat:
            self.meat = new_meat
        else:
            self.meat = False

    def get_to_go(self):
        return self.to_go
    
    def set_to_go(self, new_to_go):
        if isinstance(new_to_go, bool):
            self.to_go = new_to_go
        else:
            self.to_go = False
    
    def get_rice(self):
        return self.rice

    def set_rice(self, new_rice):
        if new_rice in self.valid_rice:
            self.rice = new_rice
        else:
            self.rice = False

    def get_beans(self):
        return self.beans

    def set_beans(self, new_beans):
        if new_beans in self.valid_beans:
            self.beans = new_beans
        else:
            self.beans = False
    
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
        if self.meat in ["chicken", "pork", "tofu"]:
            base_cost += 1
        elif self.meat == "steak":
            base_cost += 1.5
        if self.extra_meat == True and self.meat != False:
            base_cost += 1
        if self.guacamole == True:
            base_cost += 0.75
        return float(base_cost)

#Below are some lines of code that will test your class.
#You can change the value of the variable(s) to test your
#class with different inputs.
#
#If your function works correctly, this will originally
#print: 7.75
a_burrito = Burrito("pork", False, "white", "black", extra_meat = True, guacamole = True)
print(a_burrito.get_cost())

