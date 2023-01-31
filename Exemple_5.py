from decimal import Decimal

def check_input():

    num = input('Введите число\n')

    is_correct = False
    while(is_correct == False):
        try:
            num = float(num)
            if(len(str(num)) < 1e+309):
                is_correct = True
            else:
                print('Большой дядя запретил пользоваться строками, а ваше число не влизает в другой тип\nВведите пожалуйста число покороче')
        except ValueError:
            print('Вы ввели не число\n')
            num = input('Введите число\n')
    return num

num = float(check_input())

a = 0.5
a = Decimal('0.0000000001')

while(0 < a < 1):
    num = num * 10
    a = (num % 10) / 10

sum = 0

while(num >= 1):
    sum = sum + num % 10
    num = num // 10

sum = int(sum)

print(f'Сумма всх цифр, введёного числа, равна {sum}')