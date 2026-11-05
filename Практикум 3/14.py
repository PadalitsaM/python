s = input("Введите число: ")
while True:
    if s.isdigit():
        break
    s = input("Ошибка. Попробуйте еще раз. Введите число: ")

print("Введено целое число:", s)