#Найдите сумму цифр трехзначного числа.

def check_input():

    num = input('Введите трехзначное число\n')

    is_correct = False
    while(is_correct == False):
        if (num.isdigit()):
            if(99 < int(num) < 1000 ):
                is_correct = True
            else:
                print('Вы ввели не трехзначное число\n')
                num = input('Введите трехзначное число\n')
        else:
            print('Вы ввели не число или дробное число\n')
            num = input('Введите целое трехзначное число\n')
    return num

num = check_input()

     
sum = 0

for i in range(len(num)):
    sum_num = num[i]
    sum_num = int(sum_num)
    sum = sum + sum_num

print (sum)