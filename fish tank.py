length, width, height = int(input()), int(input()), int(input())
percentage = float(input()) / 100

volume = (length * width * height) / 1000
final_volume = volume - volume * percentage

print(final_volume)