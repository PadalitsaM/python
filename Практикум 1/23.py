time = int(input())
hours = time // 3600
minutes = (time // 60) - (hours * 60)
seconds = time % 60
print(f'{hours} часов {minutes} минут {seconds} секунд')
