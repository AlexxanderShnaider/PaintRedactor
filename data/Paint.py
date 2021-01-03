from tkinter.colorchooser import *
from tkinter import *
from data import Config as c
from data.Setup import load_image
from tkinter import filedialog
from tkinter import messagebox


root = Tk()
menu = menu = Menu(root)
root.config(menu=menu)


def save_file():
    file_name = filedialog.asksaveasfilename(initialdir='/', title='Select file', filetypes=(('Text Documents', '*.txt'), ('all files', '*.*')))
    if file_name:
        f = open(file_name, 'w')
        text_save = str(text.get(1.0, END))
        f.write(text_save+'\n')
        f.close()

def open_file():
    file_name = filedialog.askopenfilename(initialdir='/', title='Open file', filetypes=(('Text Documents', '*.txt'), ('all files', '*.*')))
    if file_name:
        f = open(file_name, 'r')
        text_open = f.read()
        if text_open != NONE:
            text.delete(1.0, END)
            text.insert(END, text_open)

def clear():
    global text
    if text != NONE:
        text.delete(1.0, END)

file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label='New', command=clear)
file_menu.add_command(label='Open..', command=open_file)
file_menu.add_command(label='Save as..', command=save_file)
file_menu.add_command(label='Exit', command=exit)

help_menu = Menu(menu, tearoff=0)
help_menu.add_command(label='Help')
help_menu.add_command(label='About')

menu.add_cascade(label='File', menu=file_menu)
menu.add_cascade(label='Help', menu=help_menu)



brush_size = c.BRUSH_SIZE
color = c.DEFAULT_COLOR

def active_paint(event):
    global brush_size
    global color
    w.bind('<B1-Motion>', draw)
    w.bind('<ButtonPress-1>', draw)

def draw(event):
    x1 = event.x - brush_size
    y1 = event.y - brush_size
    x2 = event.x + brush_size
    y2 = event.y + brush_size
    w.create_oval(x1, y1, x2, y2, fill=color, outline=color)

def decrease_brush_size():
    global brush_size
    if brush_size > 5:
        brush_size -= 1

def increase_brush_size():
    global brush_size
    if brush_size < 20:
        brush_size += 1
def color_change(new_color):
    global color
    color = new_color
def get_color():
    global color
    color = askcolor(title='Color Picker')
    color_change(color[1])

def del_all():
    confirmed = messagebox.askyesno('Please Confirm', 'Do you really want to delete all?')
    if confirmed:
        w.delete('all')



root.title('Paint')
w = Canvas(root, width=c.WIDTH, height=c.HEIGHT, bg=c.BG_COLOR)
w.bind('<1>', active_paint)




eraser_icon = load_image('eraser.png')
increase_icon = load_image('inbrush.png')
decrease_icon = load_image('debrush.png')
brush_icon = load_image('brush.png')


decrease_btn = Button(image=decrease_icon, command=lambda: decrease_brush_size())
increase_btn = Button(image=increase_icon, command=lambda: increase_brush_size())
brush_btn = Button(image=brush_icon, command=lambda: color_change(c.DEFAULT_COLOR))
remove_btn = Button(image=eraser_icon, command=lambda: color_change(c.ERASE_COLOR))
remove_all_btn = Button(text='Видалити все', width=20,bg='white', command=del_all)

# Buttons. Color Palette
blanched_almond_btn = Button(bg='#FFF1C9', width=2, command=lambda: color_change('#FFF1C9'))
melon_btn = Button(bg='#F7B7A3', width=2, command=lambda: color_change('#F7B7A3'))
watermelon_btn = Button(bg='#EA5F89', width=2, command=lambda: color_change('#EA5F89'))
violet_btn = Button(bg='#9B3192', width=2, command=lambda: color_change('#9B3192'))
dark_purple_btn = Button(bg='#2B0B3F', width=2, command=lambda: color_change('#2B0B3F'))
blue_btn = Button(bg='#0087C3', width=2, command=lambda: color_change('#0087C3'))
a1 = Button(bg='#e31746', width=2, command=lambda: color_change('#e31746'))
battery_charged_blue_btn = Button(bg='#1EB2D9', width=2, command=lambda: color_change('#1EB2D9'))
sky_blue_btn = Button(bg='#60DCE7', width=2, command=lambda: color_change('#60DCE7'))
vista_blue_btn = Button(bg='#7E9DEC', width=2, command=lambda: color_change('#7E9DEC'))
violet_blue_btn = Button(bg='#4247A5', width=2, command=lambda: color_change('#4247A5'))
alien_armpit_btn = Button(bg='#89DF00', width=2, command=lambda: color_change('#89DF00'))
spring_bud_btn = Button(bg='#A1F500', width=2, command=lambda: color_change('#A1F500'))
magic_mint_btn = Button(bg='#ADFFB9', width=2, command=lambda: color_change('#ADFFB9'))
medium_spring_green_btn = Button(bg='#00F798', width=2, command=lambda: color_change('#00F798'))
green_btn = Button(bg='#10B56F', width=2, command=lambda: color_change('#10B56F'))


picker_btn = Button(text='Кольори', width=20, bg='white', command=get_color)

w.grid(row=2, column=3, rowspan=50, columnspan=50, sticky=W+E+N+S, padx=5, pady=5)
decrease_btn.grid(row=1, column=5)
increase_btn.grid(row=1, column=6)
brush_btn.grid(row=1, column=7)
remove_btn.grid(row=1, column=8)
remove_all_btn.grid(row=1, column=9)
blanched_almond_btn.grid(row=2, column=2)
melon_btn.grid(row=3, column=2)
watermelon_btn.grid(row=4, column=2)
violet_btn.grid(row=5, column=2)
dark_purple_btn.grid(row=6, column=2)
blue_btn.grid(row=2, column=1)
battery_charged_blue_btn.grid(row=3, column=1)
sky_blue_btn.grid(row=4, column=1)
vista_blue_btn.grid(row=5, column=1)
violet_blue_btn.grid(row=6, column=1)
alien_armpit_btn.grid(row=2, column=0)
spring_bud_btn.grid(row=3, column=0)
magic_mint_btn.grid(row=4, column=0)
medium_spring_green_btn.grid(row=5, column=0)
green_btn.grid(row=6, column=0)
picker_btn.grid(row=7, columnspan=3)

root.mainloop()

