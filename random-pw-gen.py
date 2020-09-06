import random
import string
try:
    from tkinter import *
except ImportError : from Tkinter import *

window = Tk() ; window.title('Password Generator')
window.geometry('200x100') ; window.configure(background='#ffffff')

def gen_pw(scale):
    pw = ''.join(random.choice(string.ascii_letters+string.punctuation+string.digits) for i in range(random.randint(scale,scale)))
    set_pw(pw)
    
def set_pw(text):
    text_field.delete(0,"end")
    text_field.insert(0, text)
    
def update_textfield(do_you_see_the_bug):
    gen_pw(pw_scale.get())


text_field = Entry(window,width = 100)
pw_scale = Scale(window, from_=0, to=100,orient=HORIZONTAL,command=update_textfield)
btn = Button(text="Refresh",command=update_textfield,width = 100)


for item in [text_field, pw_scale,btn]:
	item.pack()


if __name__ == '__main__':
    mainloop()

