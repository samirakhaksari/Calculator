from tkinter import *

# A simple calculator by Sam Khaksari

# functions

# click botton

def button_click(number):
    global operator
    operator= operator + str(number)
    input_numbers.set(operator)

# Clear button

def clear_button():
    global operator
    operator = ''
    input_numbers.set('')
    
# Equal button

def equal_button():
    global operator
    sumup = str(eval(operator))
    input_numbers.set(sumup)
    operator=""
    
# settings

root = Tk()

root.geometry('320x550')
root.title('Samculator!')
root.resizable(width=False, height=False)
root.configure(bg='gray15')

root.iconbitmap(r'calculator.ico')

operator=''
input_numbers = StringVar()

# frames


# entry frame
entry_frame = Frame(root, width=320, height=166, bg='gray15')
entry_frame.pack(side=TOP)

# Button frame

operation_btn_frame = Frame(root, width=320, height=70, bg='gray15')
operation_btn_frame.pack(side=TOP)

# numbers frame

# numbers 1,2,3
numbers_123_frame = Frame(root, width=320, height=70, bg='gray20')
numbers_123_frame.pack(side=TOP)

# numbers 4,5,6

numbers_456_frame = Frame(root, width=320, height=70, bg='gray20')
numbers_456_frame.pack(side=TOP)

# numbers 7,8,9

numbers_789_frame = Frame(root, width=320, height=70, bg='gray20')
numbers_789_frame.pack(side=TOP)

# numbers c,0,.

numbers_c0_frame = Frame(root, width=320, height=70, bg='gray20')
numbers_c0_frame.pack(side=TOP)



# Menu part

menu_bar = Menu(root, bg='gray15')
about_menu = Menu(menu_bar, tearoff=0, bg='gray27', fg='white')
about_menu.add_command(label='This is a simple calculator, Enjoy!')
menu_bar.add_cascade(label='About', menu=about_menu)
root.config(menu=menu_bar, bg='gray15')

# Entry part

num_entry = Entry(entry_frame, textvariable= input_numbers,
                  bg='gray20', font=('Tahoma', 20), fg='white')
num_entry.place(x=10, y=8, width=300, height=166)

# operation button part

plus_btn = Button(operation_btn_frame, text='+', font='Tahoma',
                  width=5, height=2, bg='gray24', fg='white', command=lambda:button_click('+'))
plus_btn.place(x=12, y=10)

subtraction_btn = Button(operation_btn_frame, text='-', font='Tahoma',
                   width=5, height=2, bg='gray24', fg='white', command=lambda:button_click('-'))
subtraction_btn.place(x=73, y=10)

multiply_btn = Button(operation_btn_frame, text='*',
                      font='Tahoma',  width=5, height=2, bg='gray24', fg='white', command=lambda:button_click('*'))
multiply_btn.place(x=134, y=10)

division_btn = Button(operation_btn_frame, text='/', font='Tahoma',
                    width=5, height=2, bg='gray24', fg='white', command=lambda:button_click('/'))
division_btn.place(x=195, y=10)

equal_btn = Button(operation_btn_frame, text='=',
                   font='Tahoma',  width=5, height=2, bg='gray24', fg='white', command= equal_button)
equal_btn.place(x=256, y=10)

# numbers button part

# numbers 1,2,3

btn_1 = Button(numbers_123_frame, text='1', font='Tahoma',
               width=8, height=2, bg='gray24', fg='white', command=lambda:button_click(1))
btn_1.place(x=12, y=10)

btn_2 = Button(numbers_123_frame, text='2', font='Tahoma',
               width=8, height=2, bg='gray24', fg='white', command=lambda:button_click('2'))
btn_2.place(x=121, y=10)

btn_3 = Button(numbers_123_frame, text='3', font='Tahoma',
               width=8, height=2, bg='gray24', fg='white', command=lambda:button_click('3'))
btn_3.place(x=229, y=10)

# numbers 4,5,6

btn_4 = Button(numbers_456_frame, text='4', font='Tahoma',
               width=8, height=2, bg='gray24', fg='white', command=lambda:button_click('4'))
btn_4.place(x=12, y=10)

btn_5 = Button(numbers_456_frame, text='5', font='Tahoma',
               width=8, height=2, bg='gray24', fg='white', command=lambda:button_click('5'))
btn_5.place(x=121, y=10)

btn_6 = Button(numbers_456_frame, text='6', font='Tahoma',
               width=8, height=2, bg='gray24', fg='white', command=lambda:button_click('6'))
btn_6.place(x=229, y=10)


# numbers 7,8,9

btn_7 = Button(numbers_789_frame, text='7', font='Tahoma',
               width=8, height=2, bg='gray24', fg='white', command=lambda:button_click('7'))
btn_7.place(x=12, y=10)

btn_8 = Button(numbers_789_frame, text='8', font='Tahoma',
               width=8, height=2, bg='gray24', fg='white', command=lambda:button_click('8'))
btn_8.place(x=121, y=10)

btn_9 = Button(numbers_789_frame, text='9', font='Tahoma',
               width=8, height=2, bg='gray24', fg='white', command=lambda:button_click('9'))
btn_9.place(x=229, y=10)

# numbers c,0,.

btn_c = Button(numbers_c0_frame, text='C', font='Tahoma',
               width=8, height=2, bg='gray24', fg='white', command= clear_button)
btn_c.place(x=12, y=10)

btn_0 = Button(numbers_c0_frame, text='0', font='Tahoma',
               width=8, height=2, bg='gray24', fg='white', command=lambda:button_click('0'))
btn_0.place(x=121, y=10)

btn_dot = Button(numbers_c0_frame, text='.', font='Tahoma',
                 width=8, height=2, bg='gray24', fg='white', command=lambda:button_click('.'))
btn_dot.place(x=229, y=10)


root.mainloop()
