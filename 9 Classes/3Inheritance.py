#9.6
from SuperClasses import Restaurant, User

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    
    def add_flavors(self, *flavors):
        for flavor in flavors:
            self.flavors.append(flavor)
    
    def print_flavors(self):
        print(f'List of flavors: {self.flavors}')


new_iceCream_stand = IceCreamStand('Holly Colly', 'UK')
new_iceCream_stand.print_flavors()
new_iceCream_stand.add_flavors(
                        'Vanila',
                        'Choco',
                        'Cherry',
                        'Mint'
                        )
new_iceCream_stand.print_flavors()



print()
#9.8
class Privileges():

    def __init__(self):
        self.privileges = []
    
    def add_privilege(self, privileges_list):
        for privilege in privileges_list:
            self.privileges.append(privilege)

    def show_privileges(self, first_name, last_name):
        print(f'Priviges of {first_name.title()} {last_name.title()}:')
        for i in self.privileges:
            print(f'\t||\t {i} \t||')



print()
#9.7
class Admin(User):

    def __init__(self, first_name, last_name, age, gender=None):
        super().__init__(first_name, last_name, age, gender)   
        self.privileges = Privileges()

test_admin = Admin('TF','TL','0','male')
privileges = [
    'Add users',
    'Del users',
    'Ban users',
    'Kick users'
    ]
test_admin.privileges.add_privilege(privileges)
test_admin.privileges.show_privileges(test_admin.first_name,test_admin.last_name)

