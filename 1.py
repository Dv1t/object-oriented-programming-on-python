def write_to_file(numbers):  #вывод в файл выведен в отдельную функцию, потому что это отдельное
    # действие которое возможно надо будет повторять
    f = open("file.txt", 'w')   #тип файла txt, потому что вводим обычную текстовую информацию
    for number in numbers:
        f.write(str(round(number,2))+'\n')

def print_number(number):   #вывод в консоль в требуемом формате, чтобы упростить вывод в основной части программы
    print(round(number,2))

print("Последовательно вводите числа, по окончанию ввода введите букву s")
a = input()
b=[]
while (a!='s'):
    b.append(float(a)*0.13)
    a = input()
b.sort()
for number in b:
    print_number(number)
write_to_file(b)


