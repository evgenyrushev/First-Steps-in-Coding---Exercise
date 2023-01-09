number_of_pens = int(input())
number_of_marker = int(input())
litres_of_detergent = int(input())
discount = int(input()) / 100

pens = 5.80
marker = 7.20
detergent = 1.20

total_amount = (number_of_pens * pens + number_of_marker * marker
+ litres_of_detergent * detergent)

final_amount = total_amount - total_amount*discount

print(final_amount)