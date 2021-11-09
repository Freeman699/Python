#8.3
def make_shirt(shirt_size, shirt_text):
    print(f'\nSelected shirt size: {shirt_size}')
    print(f'Selected text to print on a shirt: "{shirt_text}"')

make_shirt('M', 'I believe in Python supremacy')
make_shirt(shirt_size = 'L', shirt_text = 'It`s so sad that Steve Jobs died of ligma')

print()

#8.4
def make_shirt(shirt_size='L', shirt_text='I love Python'):
    print(f'\nSelected shirt size: {shirt_size}')
    print(f'Selected text to print on a shirt: "{shirt_text}"')

make_shirt()
make_shirt(shirt_size = 'M', shirt_text = 'printf("Hello World!");')

print()

#8.5
def describe_city(city, location='Germany'):
    print(f'{city.title()} is in {location.title()}')

describe_city('Kyiv', 'Ukraine')
describe_city('Berlin')
describe_city('london', 'UK')