number_of_pages = int(input())
pages_for_hour = int(input())
number_of_days = int(input())

hours_to_read = number_of_pages // pages_for_hour
total_days = hours_to_read / number_of_days

print(total_days)