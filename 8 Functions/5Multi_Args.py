#8.12
def sandwich(*args):
    print('Ingredients to add to the sandwich:')
    for ingredient in args:
        print(f'- {ingredient}')

sandwich('meat balls', 'onion rings', 'mayo')
sandwich('sausage', 'ketchup')
sandwich('BREAD')

print()

#8.13
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
  
user_profile = build_profile('Max','Yurchenko',
                            languages = 'C, C++, C#, Python',
                            location = 'Kiev, Ukraine',
                            education = 'KPI')
print(user_profile)

print()

#8.14
def car_info(model, manufacturer, **kwargs):
    kwargs['model'] = model
    kwargs['manufacturer'] = manufacturer
    return kwargs

temp_car = car_info('nissan', 'nissan manifacturing',
                    color = 'black', 
                    mileage = '0')

print(temp_car)