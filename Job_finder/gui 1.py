

import tkinter as tk
from tkinter import  ttk,scrolledtext
from network import *
def searched():
    '''called after clicking search button to get and show the result
     for text searched in Combobox'''

    if job_kind.get() and job_kind.get() in jobs:
        url = f'{start_url[:-4]}{jobs[job_kind.get()]}?' #creating url from start_url and job_kind
        get_job_offers(url)
        clear() #clearing the details shown if any from offer scroll text
        text_area.delete(0,tk.END) # clearing offers shown if any from text area
        text_area.insert(1,*[f'{index+1 : <4}_  {job_offers[index]["name"][:70]}...' for index in range(len(job_offers))])

def lst_action(event):
    '''called after offer selection to show details of selected offer by its url '''
    if text_area.curselection(): #if any line selected
        url = job_offers[text_area.curselection()[0]]['link'] #extracting url
        table,offer_detail = get_offer_detail(url)
        text_area.grid_forget() # hiding text area
        
        offer_scr.configure(state ='normal') 
        offer_scr.insert(tk.INSERT,f'           General Information \n\n{table}\n      {"_"*40}\n\n    {offer_detail}')
        offer_scr.configure(state ='disabled')
        offer_scr.grid(column=0,row=0,columnspan=3,padx=5,pady=5)# showing offer scr which was hidden

def clear():
    '''called to clear offer scr text and showing last offers result'''
    offer_scr.grid_forget()
    text_area.grid(column=0,row=0,columnspan=3,padx=5,pady=5)
    
if __name__ == '__main__':
    get_job_selection(start_url)
    get_job_offers(start_url)
    win = tk.Tk()
    win.title('Job Finder')
    win.geometry('760x350')
    win.resizable(False,False) 
    bar_frame = tk.Frame(win) # the frame to hold search area
    bar_frame.grid(column=0,row=0) 
    button_frame = tk.Frame(win) # the frame to hold buttons
    button_frame.grid(column=0,row=1)
    scroll_frame = tk.Frame(win) # the frame to hold scrolled text, offers and details
    scroll_frame.grid(column=0,row=2)

    search_b = tk.Button(button_frame,text='Search',command=searched,padx=10)
    search_b.grid(column=0,row=0,sticky='W')
    padframe_bu = tk.Frame(button_frame,width=100)
    padframe_bu.grid(column=1,row=0)
    clear_b = tk.Button(button_frame,text='Back',command=clear,width=5,padx=10)
    clear_b.grid(column=2,row=0,sticky='E')

    job_kind = tk.Variable()
    job_combo = ttk.Combobox(bar_frame,width=105,textvariable=job_kind) #area to choose job kind 
    job_combo['values'] = [job for job in jobs]
    job_combo.grid(column=3,row=0)

    job_lst = tk.StringVar(value=[f'{index+1 : <4}_  {job_offers[index]["name"][:70]}...' for index in range(len(job_offers))]) #varible which offers are stored in
                                                                                                                                # 'number- offer name...'
    text_area = tk.Listbox(scroll_frame,width=105,height=15,listvariable=job_lst) # area which job offers is shown
    text_area.bind('<<ListboxSelect>>',lst_action) #selecting a job offer 
    text_area.grid(column=0,row=0,columnspan=3,padx=5,pady=5)

    offer_scr= scrolledtext.ScrolledText(scroll_frame,width=80,height=15,wrap=tk.WORD) #not been grided

    win.mainloop()