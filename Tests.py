from UserData import User

max = User()

max.add_pref('blue', 'color')
max.add_pref('shirt', 'item')
max.add_pref('red', 'color')
max.add_pref('shorts', 'item')

max.add_pref('green', 'color', 'shirt')
max.add_pref('orange', 'color', 'shirt')

max.add_pref('red', 'color', 'shoes')
max.add_pref('purple', 'color', 'shoes')

print("Tests for get_pref:\n")

print('Color Preferences:')
print(max.get_pref('color'))
print()
print('Item Preferences:')
print(max.get_pref('item'))
print()
print('Shirt Color Preferences')
print(max.get_pref('color', 'shirt'))
print()
print('Shoe Color Preferences')
print(max.get_pref('color', 'shoes'))

print('\n\nTests for get_recom_items\n')
max.get_recom_items(1)

print('\n\nTests for get_recom_perItem\n\nShirts:')
max.get_recom_perItem('shirt', 2)
print('\nShoes:')
max.get_recom_perItem('shoes', 2)