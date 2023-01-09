amount_in_deposit = float(input())
deposit_term = int(input())
yearly_percentage = float(input()) / 100

final_amount = amount_in_deposit + deposit_term\
               * ((amount_in_deposit*yearly_percentage) / 12)

print(final_amount)
