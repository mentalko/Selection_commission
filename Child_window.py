import sys
import tkinter as tk
from tkinter import ttk, IntVar
import sqlite3, configobj
from tkcalendar import DateEntry
from datetime import date
from tkinter import messagebox


class Child(tk.Toplevel):

    #region >>>>>> CHILD <<<<<
    def __init__(self, root, app, db):
        super().__init__(root)
        self.init_child()
        self.view = app
        self.db = db
        self.click_radiobtn()


        self.b_add.bind('<Button-1>', lambda event: self.view.add_records(self.e_SI.get(),
                                                                          self.e_SF.get(),
                                                                          self.e_SO.get(),
                                                                          self.e_phone.get(),
                                                                          self.datereg.get(),
                                                                          self.e_avgball.get().replace(',', '.'),
                                                                          self.rb_value.get(),
                                                                          self.get_cbox_id(self.cbox_spec.get())))
        #self.b_cancel.bind('<Button-1>', lambda event: messagebox.showinfo("Стоп", "Остановись!") )
        self.b_cancel.bind('<Button-1>', lambda event: print( self.get_cbox_id(self.cbox_spec.get())) )



    def click_radiobtn(self):
        self.cbox_spec.selection_clear() ############## not working 
        self.specialty = dict(self.db.c.execute('select id, SpecName from specialty where speconbase = '+str( self.rb_value.get())).fetchall())
        self.cbox_spec['values'] = list(self.specialty.values())
        print(self.specialty.values())

    def get_cbox_id(self, selected_str):
        for k, v in self.specialty.items():
            if v == selected_str:
                return k

    def init_child(self):
        self.rb_value = IntVar()
        self.rb_value.set(9)

        self.title('Добавить абитуриента')
        self.geometry('400x220+400+300')
        self.resizable(False, False)
        inifile = 'config.ini'
        self.config = configobj.ConfigObj(inifile)
        variable = self.config['Variables']
        value = self.config['Values']

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        self.geometry("739x450+339+86")
        self.minsize(739, 450)
        self.maxsize(1370, 753)
        self.resizable(1, 1)
        self.title("New Toplevel")
        self.configure(background="#d9d9d9")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="black")


################################## 1 ###############################
        self.Label3 = tk.Label(self,background="#d9d9d9", text='''Дата регистрации:''')
        self.Label3.place(relx=0.014, rely=0.022, height=21, width=107)

        self.datereg = DateEntry(self, format_date='YYYY/MM/DD', width=12, background='gray90',
                             foreground='black', borderwidth=4)
        self.datereg.place(relx=0.162, rely=0.022, relheight=0.047, relwidth=0.217)
        print(self.datereg.get())

        self.menubar = tk.Menu(self, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        self.configure(menu=self.menubar)
        self.Labelframe1 = tk.LabelFrame(self,background="#d9d9d9" , text='''Личные данные''')
        self.Labelframe1.place(relx=0.014, rely=0.089, relheight=0.278, relwidth=0.934)

        self.e_SI = tk.Entry(self.Labelframe1)
        self.e_SI.place(relx=0.145, rely=0.24, height=20, relwidth=0.238, bordermode='ignore')
        self.e_SF = tk.Entry(self.Labelframe1)
        self.e_SF.place(relx=0.145, rely=0.48, height=20, relwidth=0.238 , bordermode='ignore')
        self.e_SO = tk.Entry(self.Labelframe1)
        self.e_SO.place(relx=0.145, rely=0.72, height=20, relwidth=0.238, bordermode='ignore')

        self.Label1 = tk.Label(self.Labelframe1, background="#d9d9d9", text='''Имя:''')
        self.Label1.place(relx=0.059, rely=0.24, height=21, width=41
                          , bordermode='ignore')
        self.Label2 = tk.Label(self.Labelframe1, background="#d9d9d9", text='''Фамилия:''')
        self.Label2.place(relx=0.038, rely=0.48, height=21, width=60
                          , bordermode='ignore')
        self.Label4 = tk.Label(self.Labelframe1, background="#d9d9d9", text='''Отчество:''')
        self.Label4.place(relx=0.038, rely=0.72, height=21, width=60
                          , bordermode='ignore')
        self.Label4 = tk.Label(self.Labelframe1, background="#d9d9d9", text='''Номер телефона:''')
        self.Label4.place(relx=0.478, rely=0.24, height=21, width=109
                          , bordermode='ignore')

        self.e_phone = tk.Entry(self.Labelframe1,font="TkFixedFont")
        self.e_phone.place(relx=0.652, rely=0.24, height=20, relwidth=0.238
                          , bordermode='ignore')
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
        [('selected', _compcolor), ('active', _ana2color)])
        self.TNotebook1 = ttk.Notebook(self)
        self.TNotebook1.place(relx=0.014, rely=0.378, relheight=0.524
                              , relwidth=0.926)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1.configure(cursor="fleur")
        self.TNotebook1_t0 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t0, padding=3)
        self.TNotebook1.tab(0, text="Специальность", compound="left"
                            , underline="-1", )
        self.TNotebook1_t0.configure(background="#d9d9d9")
        self.TNotebook1_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t0.configure(highlightcolor="black")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(1, text="Паспортные  данные", compound="left"
                            , underline="-1", )
        self.TNotebook1_t1.configure(background="#d9d9d9")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(2, text="Аттестат", compound="none", underline="-1", )
        self.TNotebook1_t2.configure(background="#d9d9d9")
        self.TNotebook1_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t2.configure(highlightcolor="black")

        ######################################################################

        self.e_avgball = tk.Entry(self.TNotebook1_t2, font="TkFixedFont")
        self.e_avgball.place(relx=0.167, rely=0.1, height=20, relwidth=0.112)


        self.Label6 = tk.Label(self.TNotebook1_t0,background="#d9d9d9",text='''На базе:''')
        self.Label6.place(relx=0.015, rely=0.05, height=21, width=54)


        self.rad_btn9 = ttk.Radiobutton(self.TNotebook1_t0, text='''9 классов''',
                                       variable=self.rb_value, value=9, command=self.click_radiobtn)
        self.rad_btn9.place(relx=0.106, rely=0.05, relheight=0.125, relwidth=0.123)
        self.rad_btn11 = tk.Radiobutton(self.TNotebook1_t0, background="#d9d9d9", text='''11 классов''',
                                        variable=self.rb_value, value=11, command=self.click_radiobtn)
        self.rad_btn11.place(relx=0.242, rely=0.05, relheight=0.125 , relwidth=0.132)


        self.cbox_spec = ttk.Combobox(self.TNotebook1_t0, cursor="fleur", state='readonly')
        self.cbox_spec.place(relx=0.273, rely=0.2, relheight=0.105
                              , relwidth=0.400)


        self.Label2 = tk.Label(self.TNotebook1_t0, background="#d9d9d9", text='''Основная специальность:''')
        self.Label2.place(relx=0.015, rely=0.2, height=21, width=149)

        self.Label2 = tk.Label(self.TNotebook1_t1, background="#d9d9d9", text='''Серия и номер:''')
        self.Label2.place(relx=0.03, rely=0.1, height=21, width=92)


        self.Entry1 = tk.Entry(self.TNotebook1_t1)
        self.Entry1.place(relx=0.197, rely=0.1, height=20, relwidth=0.248)
        self.Entry1.configure(background="red")

        self.Label5 = tk.Label(self.TNotebook1_t1, background="#d9d9d9", text='''Гражданство:''')
        self.Label5.place(relx=0.047, rely=0.25, height=21, width=80)

        self.cmb_ctzn = ttk.Combobox(self.TNotebook1_t1, takefocus="")
        self.cmb_ctzn.place(relx=0.197, rely=0.25, relheight=0.105
                              , relwidth=0.242)

        self.Label4 = tk.Label(self.TNotebook1_t1,background="#d9d9d9", text='''Дата выдачи:''')
        self.Label4.place(relx=0.53, rely=0.1, height=21, width=78)

        self.Entry1 = tk.Entry(self.TNotebook1_t1)
        self.Entry1.place(relx=0.662, rely=0.1, height=20, relwidth=0.248)

        self.Label5 = tk.Label(self.TNotebook1_t1, background="#d9d9d9", text='''Дата рождения:''')
        self.Label5.place(relx=0.506, rely=0.25, height=21, width=89)

        self.Entry3 = tk.Entry(self.TNotebook1_t1)
        self.Entry3.place(relx=0.667, rely=0.25, height=20, relwidth=0.248)
        self.Entry3.configure(background="green")

        self.Label7 = tk.Label(self.TNotebook1_t1, background="#d9d9d9", text='''Адресс:''')
        self.Label7.place(relx=0.115, rely=0.4, height=21, width=32)


        self.Text1 = tk.Text(self.TNotebook1_t1)
        self.Text1.place(relx=0.576, rely=0.45, relheight=0.32, relwidth=0.339)
        self.Text1.configure(background="white")
        self.Text1.configure(wrap="word")

        self.Label8 = tk.Label(self.TNotebook1_t1, background="#d9d9d9", text='''Адресс:''')
        self.Label9 = tk.Label(self.TNotebook1_t2, background="#d9d9d9", text='''Балл атестата:''')
        self.Label9.place(relx=0.015, rely=0.1, height=21, width=89)



        self.b_add = tk.Button(self)
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


        self.b_cancel = tk.Button(self)
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

        self.grab_set()
        self.focus_set()

    #endregion