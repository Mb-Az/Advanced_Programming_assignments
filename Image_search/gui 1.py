


import tkinter as tk
from bingsearch_network import *
from PIL import Image, ImageTk


class ImageHolder:
    '''a class to hold opened images and keeping them with diffrent varibles'''
    def hold(self,number,img):
        setattr(self,f'img{number}',img)

def searched():
    '''called after clicking search button to get and show the result
     for text searched in Entry'''
    if entry.get().strip():
        clear()
        image_count = search_for(entry.get().strip())
        for i in range(image_count):
                try:
                        
                        image_holder.hold(i,ImageTk.PhotoImage(Image.open( f"img{i}.gif")))
                        exec(f'image_area.image_create(tk.END,image=image_holder.img{i},padx=5,pady=5)')
                except FileNotFoundError:
                        pass

            
       
def clear():
    '''called to clear offer scr text and showing last images result via clear button'''
    image_area.config(state = 'normal')
    image_area.delete(0.0,tk.END)
    image_area.config(state = 'disable')
    
def entry_clear(action):
    '''clearing entry after focusing on it'''
    entry.configure(bg='white')
    entry.delete(0,tk.END)
def exit():
    '''exiting the app with exit button'''
    win.destroy()

if __name__ == '__main__':
    creat_folder()
    image_holder = ImageHolder()

    win = tk.Tk()
    win.title('Job Finder')
    win.geometry('820x600')
    win.resizable(False,False) 
    entry_frame = tk.Frame(win) # the frame to hold search area
    entry_frame.grid(row=0) 
    button_frame = tk.Frame(win) # the frame to hold buttons
    button_frame.grid(row=1)
    scroll_frame = tk.Frame(win) # the frame to hold scrolled images
    scroll_frame.grid(row=2)

    search_text = tk.StringVar()
    entry = tk.Entry(entry_frame,width=50,textvariable=search_text,bg='lightgrey')# search area
    entry.insert(0,'Search in here')
    entry.bind('<FocusIn>',entry_clear)
    entry.grid(column=0,row=0,columnspan=4)

    search_b = tk.Button(button_frame,text='Search',command=searched,padx=10)
    search_b.grid(column=0,row=0)
    padframe_bu = tk.Frame(button_frame,width=100)
    padframe_bu.grid(column=1,row=0)
    clear_b = tk.Button(button_frame,text='Clear',command=clear,width=5,padx=10)
    clear_b.grid(column=2,row=0)
    exit_b = tk.Button(scroll_frame,text='Exit',command=exit,padx=10)
    exit_b.grid(column=2,row=1)
    
    image_area = tk.Text(scroll_frame,height=30,width=90) #images are shown in here
    image_area.insert(tk.END,'\n')
    image_area.grid(column=0,row=0,columnspan=5)
    image_area.configure(state ='disable')

    win.mainloop()