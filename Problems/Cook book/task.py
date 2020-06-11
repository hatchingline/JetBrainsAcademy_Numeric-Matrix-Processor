pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"
foods = [pasta, apple_pie, ratatouille, chocolate_cake, omelette]
foods_name = ['pasta', 'apple pie', 'ratatouille', 'chocolate cake', 'omelette']
ingredient = input()
for i in range(len(foods)):
    if ingredient in foods[i]:
        print('{} time!'.format(foods_name[i]))
    else:
        pass
