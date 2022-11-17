from pyfiglet import Figlet
import sys
import random


figlet = Figlet()
usr_input = input()
fonts = figlet.getFonts()
if len(sys.argv) == 1:
    choose_font = random.choice(figlet.getFonts())
    set_font = figlet.setFont(font=choose_font)
    print(figlet.renderText(usr_input))
elif len(sys.argv) == 3 and sys.argv[2] in fonts and sys.argv[1] == '-f' or sys.argv[1] == '--font' :
    set_font = figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(usr_input))
else:
    sys.exit()


