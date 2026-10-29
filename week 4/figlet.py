import sys
from pyfiglet import Figlet
import random

figlet=Figlet()
fonts=figlet.getFonts()

total_arguments=len(sys.argv)

if total_arguments == 1:
    figlet.setFont(font=random.choice(fonts))

elif total_arguments ==3 and sys.argv[1] in ("-f","--font") and sys.argv[2] in fonts:
    figlet.setFont(font=sys.argv[2])

else:
    exit("Invalid usage")

text = input("Input: ")

print(f"Output: {figlet.renderText(text)}")