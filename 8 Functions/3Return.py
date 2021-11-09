#8.6
def city_country(city, country):
    formated = f"{city}, {country}"
    return formated.title()

formated_data = city_country('katowice', 'poland')
print(formated_data)

formated_data = city_country('kyiv', 'ukraine')
print(formated_data)

formated_data = city_country('Tokio', 'japan')
print(formated_data)

print()

#8.7
def make_album(album_name, album_autor, number_of_songs = None):
    if number_of_songs:
        album = {
            'album name': album_name,
            'album auror': album_autor,
            'numbe of songs': number_of_songs
            }
    else:
        album = {
            'album name': album_name,
            'album auror': album_autor,
            'number of songs': ''
            }
    return album

temp_album = make_album('Ugly is beautiful', 'oliver tree')
print(temp_album)

temp_album = make_album('Discovery', 'Daft Punk')
print(temp_album)

temp_album = make_album(album_name='Homework', album_autor='daft punk')
print(temp_album)

temp_album = make_album(album_name='Californication', album_autor='Red Hot Chili Peppers', number_of_songs='15')
print(temp_album)

temp_album = make_album('How To Be A Human Being', 'Glass Animals', '11')
print(temp_album)

print()

#8.8

while True:
    continue_response = input('Do you want to add new album? (y/n) ')
    if continue_response == 'no' or continue_response == 'n':
        break

    temp_album_name = input('Enter album name: ')
    temp_album_autor = input('Enter album autor: ')
    temp_album_number_of_songs = input('Enter number of songs: ')
    new_album = make_album(album_name=temp_album_name, album_autor=temp_album_autor, number_of_songs=temp_album_number_of_songs)

    print()
    for key, value in new_album.items():
        print(f'{key.title()}: {value.title()}')