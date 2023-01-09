number_chicken_menu = int(input())
number_fish_menu = int(input())
number_veggie_menu = int(input())

chicken_menu = 10.35
fish_menu = 12.40
veggie_menu = 8.15
delivery = 2.50

food_ordered = (number_chicken_menu * chicken_menu + number_fish_menu * fish_menu + number_veggie_menu * veggie_menu)

dessert = food_ordered * 0.2

final_amount = food_ordered + dessert + delivery

print(final_amount)