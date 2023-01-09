yearly_fee = int(input())

shoes = yearly_fee * 0.6
shirt = shoes * 0.8
ball = shirt / 4
accessories = ball / 5

final_amount = yearly_fee + shoes + shirt + ball + accessories

print(final_amount)