# калькулятор
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
just_fix_windows_console()

print ( Back.GREEN )
print ( Fore.BLACK )
what = input("Выберите действие? ( +, -, /, * ): ")
# ввести команду, при невыполнении условия выдавал "Выбрана неверная команда"
print ( Back.CYAN )
a = float( input("введите первое число: "))
b = float( input("введите второе число: "))
print (Back.RED )
if what == "+":
    c=a+b
    print( "Результат :"+str(c) )
elif what == "-":
    c=a-b
    print( "Результат :"+str(c) )
elif what == "/":
    c = a / b
    print( "Результат :" + str(c))
elif what == "*":
    c = a * b
    print( "Результат :" + str(c))
else:
    print( "Выбрана неверная информация" )
input()