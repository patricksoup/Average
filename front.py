"""
Frontend for Average Calculator
By PatrickSoup

EXIT CODES:
0: Program finished successfully
1: Unknown Error
2: User pressed cancel
3: Invalid Response from gui backend
4: Invalid Response from calc backend
"""

import easygui.easygui as gui  # TODO: Program GUI myself
import back

CHOICES = ['Mean', 'Median', 'Mode', 'Range', 'Change Numbers', 'Exit']

numbers = []


def main():
    if True:
        number = gui.enterbox('Enter your first number.', 'Average')
        if number is None:
            exit(2)  # user pressed cancel
        while number is not None:  # until user pressed cancel
            # ask for number
            number = gui.enterbox('Enter the next number, press cancel to finish adding numbers.', 'Average')

            try:
                number = float(number)  # make sure is a number

            except Exception:  # TODO: Find out what exception needs to be caught
                if number is None: break
                if gui.buttonbox('Invalid input.', 'Average', ['Try Again', 'Close Program']) == 'Try Again':
                    continue
                else:
                    exit(2)
            numbers.append(number)  # add to list
    choose()


def choose():
    while True:
        # choices are mean, median, mode, range, exit, new numbers
        choice = gui.buttonbox('What is your function?\nThe numbers are\n'+str(numbers), 'Average', CHOICES)
        try:
            if choice == 'Mean':
                gui.msgbox('The mean is ' + str(back.mean(numbers)))
            elif choice == 'Median':
                gui.msgbox('The median is ' + str(back.median(numbers)))
            elif choice == 'Mode':
                gui.msgbox('The mode is ' + str(back.mode(numbers)))
            elif choice == 'Range':
                gui.msgbox('The median is ' + str(back.median(numbers)))
            elif choice == 'Exit':
                exit(0)
            elif choice == 'Change Numbers':
                main()
            else:
                exit(3)
        except Exception:  # TODO: Find out what exception needs to be caught
            exit(4)

if __name__ == "__main__":
    main()