#9.13
from random import randint
from time import sleep

class Die():

    def __init__(self, side = 6):
        self.side = side

    def roll_die(self):
        print(randint(1 , self.side))


d10 = Die(10)
d20 = Die(20)

print("\n\nRolling D10:")
for i in range(10):
    d10.roll_die()

print('\n\nRolling D20')
for i in range(10):
    d20.roll_die()



print()
#9.14
from random import choices

class Lottery():

    def __init__(self,nums_words_list):
        self.nums_words_list = nums_words_list

    def rand_choice(self):
        win_list = choices(self.nums_words_list, k=4)
        return win_list
    

rand_token_list = [
            '1','5','8',
            '8','93','3',
            '7','9','44',
            '40',
            'u','j','o',
            'y','e'
            ]
test_ticket = Lottery(rand_token_list)
win_list = test_ticket.rand_choice()
print(f'Win lottery list:{win_list}')



#9.14
def lottery_analyzer(win_list,print_generated_tickets_flag):
    token_list = ['']
    temp_ticket = Lottery(rand_token_list)
    cnt = 0

    while token_list != win_list:
        token_list = temp_ticket.rand_choice()
        if print_generated_tickets_flag: print(f'{token_list}')
        cnt += 1

    print(f'\nYour ticket: {win_list}')
    print(f'Generated ticket: {token_list}')
    print(f'\n||| Number of attempts: {cnt} |||')


answer = input('Do you want to see all generated lottery tickets?\ty/n\n---->')
flag = False
if answer == 'y': flag = True
elif answer == 'n': flag = False
else: print('Missinput, flag set to False')

lottery_analyzer(win_list,flag)