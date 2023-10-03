from cmath import pi, sin, cos, tan
import math

def inputValue(choice):
    while(True):
        try:
            if choice in ("1", "2", "3", "4", "5"):
                a = float( input("Введит 1-ое число "))
                b = float( input("Введит 2-ое число "))
                return a, b
            else:
                a = float( input("Введит число "))
                return a


        except ValueError:
            print("Упс! Введены неправильные символы.  Пробуйте снова...")

  
   

print("Привет случайный пользователь данного калькулятора")

while True:
    print(" ")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    print("0. Выход")
    print(" ")

    choice = input("Выберите действие: ")
    if choice == '1':
        a, b = inputValue(choice)
        c = a + b
        print("Результат: " + str(c))

    elif choice == '2':
        a, b = inputValue(choice)
        c = a - b
        print("Результат: " + str(c))
    
    elif choice == '3':
        a, b = inputValue(choice)
        c = a * b
        print("Результат: " + str(c))

    elif choice == '4':
        a, b = inputValue(choice)
        if b == 0: 
            print('На 0 делить нельзя')
        else: 
            c = a / b
            print("Результат: " + str(c))

    elif choice == '5':
        a, b = inputValue(choice)
        c = a ** b
        print("Результат: " + str(c))

    elif choice == '6':
        a = inputValue(choice)
        c = a ** 0.5
        print("Результат: " + str(c))

    elif choice == '7':
        a = inputValue(choice)
        if a < 0: 
            print('Факториал не может быть отрицательным')
        else: 
            print(math.factorial(a))
 

    elif choice == '8':
        a = inputValue(choice)
        c = sin(pi/a)
        print("Результат: " + str(c))

    elif choice == '9':
        a = inputValue(choice)
        c = cos(pi/a)
        print("Результат: " + str(c))

    elif choice == '10':
        a = inputValue(choice)
        c = tan(pi/a)
        print("Результат: " + str(c))

    elif choice == '0':
        print("До свидания")
        break

    else: 
        print("Что-то пошло не так. Попробуйте снова")