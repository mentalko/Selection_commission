
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkcalendar import DateEntry
from datetime import date
py3 = True

import forDBCollege_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    forDBCollege_support.set_Tk_var()
    top = Toplevel1 (root)
    forDBCollege_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    forDBCollege_support.set_Tk_var()
    top = Toplevel1 (w)
    forDBCollege_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None










class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("739x450+339+86")
        top.minsize(739, 450)
        top.maxsize(1370, 753)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.609, rely=0.667, height=24, width=47)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Button''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.014, rely=0.022, height=21, width=107)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Дата регистрации:''')


        self.cal = DateEntry(top, format_date= 'YYYY/MM/DD', width=12, background='gray90',
                        foreground='black', borderwidth=4)
        # cal.grid(row=1, column=3, sticky='nsew')
        self.cal.place(relx=0.162, rely=0.022, relheight=0.047
                , relwidth=0.217)
        print(self.cal.get())

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.014, rely=0.089, relheight=0.278
                , relwidth=0.934)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Личные данные''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")

        self.Entry1_1 = tk.Entry(self.Labelframe1)
        self.Entry1_1.place(relx=0.145, rely=0.72, height=20, relwidth=0.238
                , bordermode='ignore')
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="black")
        self.Entry1_1.configure(insertbackground="black")
        self.Entry1_1.configure(selectbackground="#c4c4c4")
        self.Entry1_1.configure(selectforeground="black")

        self.Label1 = tk.Label(self.Labelframe1)
        self.Label1.place(relx=0.059, rely=0.24, height=21, width=41
                , bordermode='ignore')
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(cursor="fleur")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Имя:''')

        self.Label2 = tk.Label(self.Labelframe1)
        self.Label2.place(relx=0.038, rely=0.48, height=21, width=60
                , bordermode='ignore')
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Фамилия:''')

        self.Label4 = tk.Label(self.Labelframe1)
        self.Label4.place(relx=0.038, rely=0.72, height=21, width=60
                , bordermode='ignore')
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Отчество:''')

        self.Entry2 = tk.Entry(self.Labelframe1)
        self.Entry2.place(relx=0.145, rely=0.24, height=20, relwidth=0.238
                , bordermode='ignore')
        self.Entry2.configure(background="white")
        self.Entry2.configure(cursor="fleur")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.Entry4 = tk.Entry(self.Labelframe1)
        self.Entry4.place(relx=0.145, rely=0.48, height=20, relwidth=0.238
                , bordermode='ignore')
        self.Entry4.configure(background="white")
        self.Entry4.configure(cursor="fleur")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="#c4c4c4")
        self.Entry4.configure(selectforeground="black")

        self.Label4 = tk.Label(self.Labelframe1)
        self.Label4.place(relx=0.478, rely=0.24, height=21, width=109
                , bordermode='ignore')
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Номеер телефона:''')

        self.Entry2 = tk.Entry(self.Labelframe1)
        self.Entry2.place(relx=0.652, rely=0.24, height=20, relwidth=0.238
                , bordermode='ignore')
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.014, rely=0.378, relheight=0.524
                , relwidth=0.926)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1.configure(cursor="fleur")
        self.TNotebook1_t0 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t0, padding=3)
        self.TNotebook1.tab(0, text="Специальность", compound="left"
                ,underline="-1", )
        self.TNotebook1_t0.configure(background="#d9d9d9")
        self.TNotebook1_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t0.configure(highlightcolor="black")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(1, text="Паспортные  данные", compound="left"
                ,underline="-1", )
        self.TNotebook1_t1.configure(background="#d9d9d9")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(2, text="Аттестат",compound="none",underline="-1",)
        self.TNotebook1_t2.configure(background="#d9d9d9")
        self.TNotebook1_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t2.configure(highlightcolor="black")

        self.Label6 = tk.Label(self.TNotebook1_t0)
        self.Label6.place(relx=0.015, rely=0.05, height=21, width=54)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''На базе:''')

        self.Radiobutton1 = tk.Radiobutton(self.TNotebook1_t0)
        self.Radiobutton1.place(relx=0.106, rely=0.05, relheight=0.125
                , relwidth=0.123)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#d9d9d9")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(text='''9 классов''')
        self.Radiobutton1.configure(variable=forDBCollege_support.selectedButton)

        self.Radiobutton2 = tk.Radiobutton(self.TNotebook1_t0)
        self.Radiobutton2.place(relx=0.242, rely=0.05, relheight=0.125
                , relwidth=0.132)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#d9d9d9")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify='left')
        self.Radiobutton2.configure(text='''11 классов''')
        self.Radiobutton2.configure(value="False")
        self.Radiobutton2.configure(variable=forDBCollege_support.selectedButton)

        self.TCombobox2 = ttk.Combobox(self.TNotebook1_t0)
        self.TCombobox2.place(relx=0.273, rely=0.2, relheight=0.105
                , relwidth=0.212)
        self.TCombobox2.configure(textvariable=forDBCollege_support.combobox)
        self.TCombobox2.configure(takefocus="")
        self.TCombobox2.configure(cursor="fleur")

        self.Label2 = tk.Label(self.TNotebook1_t0)
        self.Label2.place(relx=0.015, rely=0.2, height=21, width=149)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Основная специальность:''')

        self.Label2 = tk.Label(self.TNotebook1_t1)
        self.Label2.place(relx=0.03, rely=0.1, height=21, width=92)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Серия и номер:''')

        self.Entry1 = tk.Entry(self.TNotebook1_t1)
        self.Entry1.place(relx=0.197, rely=0.1,height=20, relwidth=0.248)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Label5 = tk.Label(self.TNotebook1_t1)
        self.Label5.place(relx=0.047, rely=0.25, height=21, width=80)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Гражданство:''')

        self.TCombobox3 = ttk.Combobox(self.TNotebook1_t1)
        self.TCombobox3.place(relx=0.197, rely=0.25, relheight=0.105
                , relwidth=0.242)
        self.TCombobox3.configure(textvariable=forDBCollege_support.combobox)
        self.TCombobox3.configure(takefocus="")

        self.Label4 = tk.Label(self.TNotebook1_t1)
        self.Label4.place(relx=0.53, rely=0.1, height=21, width=78)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Дата выдачи:''')

        self.Entry1 = tk.Entry(self.TNotebook1_t1)
        self.Entry1.place(relx=0.662, rely=0.1,height=20, relwidth=0.248)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label5 = tk.Label(self.TNotebook1_t1)
        self.Label5.place(relx=0.506, rely=0.25, height=21, width=89)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Дата рождения:''')

        self.Entry3 = tk.Entry(self.TNotebook1_t1)
        self.Entry3.place(relx=0.667, rely=0.25,height=20, relwidth=0.248)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Label7 = tk.Label(self.TNotebook1_t1)
        self.Label7.place(relx=0.115, rely=0.4, height=21, width=32)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Пол:''')

        self.Text1 = tk.Text(self.TNotebook1_t1)
        self.Text1.place(relx=0.576, rely=0.45, relheight=0.32, relwidth=0.339)
        self.Text1.configure(background="white")
        self.Text1.configure(cursor="fleur")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(wrap="word")

        self.Label8 = tk.Label(self.TNotebook1_t1)
        self.Label8.place(relx=0.5, rely=0.425, height=21, width=48)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Адресс:''')

        self.Label9 = tk.Label(self.TNotebook1_t2)
        self.Label9.place(relx=0.015, rely=0.1, height=21, width=89)
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text='''Балл аттестата:''')

        self.Entry4 = tk.Entry(self.TNotebook1_t2)
        self.Entry4.place(relx=0.167, rely=0.1,height=20, relwidth=0.112)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")

        self.b_add = tk.Button(top)
        self.b_add.place(relx=0.365, rely=0.911, height=24, width=63)
        self.b_add.configure(activebackground="#ececec")
        self.b_add.configure(activeforeground="#000000")
        self.b_add.configure(background="#d9d9d9")
        self.b_add.configure(disabledforeground="#a3a3a3")
        self.b_add.configure(foreground="#000000")
        self.b_add.configure(highlightbackground="#d9d9d9")
        self.b_add.configure(highlightcolor="black")
        self.b_add.configure(pady="0")
        self.b_add.configure(text='''Добавить''')

        self.b_cancel = tk.Button(top)
        self.b_cancel.place(relx=0.501, rely=0.911, height=24, width=75)
        self.b_cancel.configure(activebackground="#ececec")
        self.b_cancel.configure(activeforeground="#000000")
        self.b_cancel.configure(background="#d9d9d9")
        self.b_cancel.configure(disabledforeground="#a3a3a3")
        self.b_cancel.configure(foreground="#000000")
        self.b_cancel.configure(highlightbackground="#d9d9d9")
        self.b_cancel.configure(highlightcolor="black")
        self.b_cancel.configure(pady="0")
        self.b_cancel.configure(text='''Дать пинка!''')

if __name__ == '__main__':
    vp_start_gui()





