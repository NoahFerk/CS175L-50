#Noah Ferker
#CS 175L 50
#February 14 2022

keep_going = 'y'
vegetarian = False
vegan = False
gluten_free = False

while keep_going == 'y':
    is_vegetarian = input('Is anyone in your party vegetarian?')
    is_vegan = input('Is anyone in your party vegan?')
    is_gluten_free = input('Is anyone in your party gluten free?')

    if is_vegetarian == 'yes':
        vegetarian = True
    if is_vegan == 'yes':
        vegan = True
    if is_gluten_free == 'yes':
        gluten_free = True

    print('Here are your resaurant choices:')

    if vegetarian == False and vegan == False and gluten_free == False:
        print('Joe\'s Gourmet Burgers')

    if vegan == False and gluten_free == False:
        print('Mama\'s Fine Italian')

    if vegan == False:
        print('Main Street Pizza')

    print('Corner Cafe')
    print('Chef\'s Kitchen')
    keep_going = input('Would you like to search again? ')

