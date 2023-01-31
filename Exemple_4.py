"""
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника)
"""

def check_input(massege):

    num = input(massege)

    is_correct = False
    while(is_correct == False):
        if (num.isdigit()):
            if(0 < int(num)):
                is_correct = True
            else:
                print('Похоже такой шоколадки не существует\n')
                num = input(massege)
        else:
            print('Упс :(\n Вы ввели не число долек, а что-то другое\n')
            num = input(massege)
    return num

lenght = int(check_input('Введите длину шоколадки в дольках\n'))
width = int(check_input('Введите ширину шоколадки в дольках\n'))
part_of_chocolate = int(check_input('Какое количество кусочков хотите отломить\n'))

if (part_of_chocolate < lenght * width): 
    if (part_of_chocolate % lenght == 0 or part_of_chocolate % width== 0):
        print('Вы можете отломить целое количество долек :)\n Ваш внутренний перфикционист будет доволен')
    else:
        print('Упс :( \n К сожалению вам не удасться уйти незамеченым и все увидят, что вы съели кусок шоколадки')
else:
    print('Ой :( \nКажется это слишком большой кусок или мы говорим не про эту шоколадку')
