nylon_needed = int(input())
paint_needed = int(input())
mixer_needed = int(input())
hours_needed = int(input())

nylon = 1.50
paint = 14.50
mixer = 5.00

paint_needed += paint_needed * 0.10
nylon_needed += 2
bags = 0.40

total_materials = (nylon_needed * nylon + paint_needed * paint + mixer_needed * mixer + bags)

working_hours_pay = (total_materials * 0.3) * hours_needed

final_amount = total_materials + working_hours_pay

print(final_amount)
