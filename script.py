from food import Food
from drink import Drink

food1 = Food('Sandwich', 7, 252)
food2 = Food('Pasta', 12, 131)
food3 = Food('Soup', 6, 56)

foods = [food1, food2, food3]

drink1 = Drink('Coffee', 6, 180)
drink2 = Drink('Lemon Tea', 5, 350)
drink3 = Drink('Milk', 2, 30)

drinks = [drink1, drink2, drink3]

print('Foods')
index = 0
for food in foods:
    print(str(index) + '. ' + food.info())
    index += 1

print('Drinks')
index = 0
for drink in drinks:
    print(str(index) + '. ' + drink.info())
    index +=1

print('--------------------')

food_order = int(input('Insert food number: '))
selected_food = foods[food_order]

drink_order = int(input('Insert drink number: '))
selected_drink = drinks[drink_order]

count = int(input('How many foods and drinks do you want to buy? (10% discount for 3 or more): '))

result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

print('The total price is $' + str(result))