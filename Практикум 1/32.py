n = float(input())
hour = 360 / 12
minute = 360 / 12 / 60
hours = int(n // hour)
minutes = int((n % hour)/minute)
print(hours, minutes)