import random
import string
try:
    from tkinter import *
except ImportError : from Tkinter import *
h,w = 200,100

window = Tk() ; window.title('Password Generator')
window.geometry(f'{h}x{w}') ; window.configure(background='#282a36')
    
def gen_pw():
    text_field.delete(0,"end")
    text_field.insert(0, ''.
                      join(random.choice(string.ascii_letters+string.punctuation+string.digits)
                           for i in range(random.randint(pw_scale.get(),pw_scale.get()))))

text_field = Entry(window,width = w,bg='#000000',foreground='#50fa7b')
pw_scale = Scale(window, from_=0, to=100,orient=HORIZONTAL,bg='#282a36',foreground='white')
btn = Button(text="Generate",command=gen_pw,width = w,bg='#000000')

for item in [text_field, pw_scale,btn]:
	item.pack()

if __name__ == '__main__':
    mainloop()
