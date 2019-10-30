import sys
import tkinter as tk
from tkinter import ttk, IntVar
import sqlite3, configobj
from tkcalendar import DateEntry
from datetime import date
from tkinter import messagebox


class Child(tk.Toplevel):

    # region >>>>>> CHILD <<<<<
    def __init__(self, root, app, db):
        super().__init__(root)
        self.init_child()
        self.view = app
        self.db = db
        self.click_radiobtn()
        # inifile = 'config.ini'
        # self.config = configobj.ConfigObj(inifile)
        # variable = self.config['Variables']
        # value = self.config['Values']

        self.b_add.bind('<Button-1>', lambda event: self.view.add_records(self.e_SI.get(),
                                                                          self.e_SF.get(),
                                                                          self.e_SO.get(),
                                                                          self.e_phone.get(),
                                                                          self.date_of_registration.get(),
                                                                          self.e_avgball.get().replace(',', '.'),
                                                                          self.rb_value.get(),
                                                                          self.get_cbox_id(self.cbox_spec.get()),
                                                                          self.e_pasportNumber.get(),
                                                                          self.cbox_gender.get(),
                                                                          self.cbox_ctzn.get(),
                                                                          self.date_of_pasport_release.get(),
                                                                          self.date_of_birth.get(),
                                                                          self.e_address.get(1.0, tk.END)))
        # self.b_cancel.bind('<Button-1>', lambda event: messagebox.showinfo("Стоп", "Остановись!") )
        self.b_cancel.bind('<Button-1>', lambda event: print(self.get_cbox_id(self.cbox_spec.get())))

    def click_radiobtn(self):
        self.cbox_spec.selection_clear()  ############## not working
        self.specialty = dict(self.db.c.execute(
            'select id, SpecName from specialty where speconbase = ' + str(self.rb_value.get())).fetchall())
        self.cbox_spec['values'] = list(self.specialty.values())
        print(self.specialty.values())

    def get_cbox_id(self, selected_str):
        for k, v in self.specialty.items():
            if v == selected_str:
                return k

    def init_child(self):
        self.rb_value = IntVar()
        self.rb_value.set(9)

        self.title("Добавление абитуриента")
        self.geometry("739x450+339+86")
        self.resizable(False, False)

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor, foreground=_fgcolor, font="TkDefaultFont")
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])
        self.minsize(739, 450)
        self.maxsize(1370, 753)
        self.configure(background="#d9d9d9",highlightbackground="#d9d9d9",highlightcolor="black")

        self.menubar = tk.Menu(self, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        self.configure(menu=self.menubar)
        self.Labelframe1 = tk.LabelFrame(self, background="#d9d9d9", text='''Личные данные''')
        self.Labelframe1.place(relx=0.014, rely=0.089, relheight=0.278, relwidth=0.934)
        self.style.configure('TNotebook.Tab', background=_bgcolor, foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=[('selected', _compcolor), ('active', _ana2color)])
        self.tkNotebook = ttk.Notebook(self, takefocus="", cursor="fleur")
        self.tkNotebook.place(relx=0.014, rely=0.378, relheight=0.524, relwidth=0.926)
        self.tkTab_0 = tk.Frame(self.tkNotebook)
        self.tkTab_1 = tk.Frame(self.tkNotebook)
        self.tkTab_2 = tk.Frame(self.tkNotebook)
        self.tabsNames = {self.tkTab_0: 'Специальность', self.tkTab_1: 'Паспортные  данные', self.tkTab_2: 'Аттестат'}
        i = 0
        for tkTab, tab in self.tabsNames.items():
            self.tkNotebook.add(tkTab, padding=3)
            self.tkNotebook.tab(i, text=tab,  underline="-1")
            tkTab.configure(background="#d9d9d9",highlightbackground="#d9d9d9",highlightcolor="black")
            i += 1






        self.date_of_registration = DateEntry(self, date_pattern='DD.MM.YYYY', width=12, background='gray90',
                                              foreground='black')
        self.date_of_registration.place(relx=0.162, rely=0.022, relheight=0.047, relwidth=0.217)
        self.e_SI = tk.Entry(self.Labelframe1)
        self.e_SI.place(relx=0.145, rely=0.24, height=20, relwidth=0.238, bordermode='ignore')
        self.e_SF = tk.Entry(self.Labelframe1)
        self.e_SF.place(relx=0.145, rely=0.48, height=20, relwidth=0.238, bordermode='ignore')
        self.e_SO = tk.Entry(self.Labelframe1)
        self.e_SO.place(relx=0.145, rely=0.72, height=20, relwidth=0.238, bordermode='ignore')
        self.e_phone = tk.Entry(self.Labelframe1, font="TkFixedFont")
        self.e_phone.place(relx=0.652, rely=0.24, height=20, relwidth=0.238 , bordermode='ignore')

        self.e_avgball = tk.Entry(self.tkTab_2, font="TkFixedFont")
        self.e_avgball.place(relx=0.167, rely=0.1, height=20, relwidth=0.112)

        self.rad_btn9 = ttk.Radiobutton(self.tkTab_0, text='''9 классов''', variable=self.rb_value, value=9,command=self.click_radiobtn)
        self.rad_btn9.place(relx=0.106, rely=0.05, relheight=0.125, relwidth=0.123)
        self.rad_btn11 = tk.Radiobutton(self.tkTab_0, background="#d9d9d9", text='''11 классов''',variable=self.rb_value, value=11, command=self.click_radiobtn)
        self.rad_btn11.place(relx=0.242, rely=0.05, relheight=0.125, relwidth=0.132)

        self.cbox_spec = ttk.Combobox(self.tkTab_0, cursor="fleur", state='readonly')
        self.cbox_spec.place(relx=0.273, rely=0.2, relheight=0.105, relwidth=0.400)

        self.e_pasportNumber = tk.Entry(self.tkTab_1)
        self.e_pasportNumber.place(relx=0.197, rely=0.1, height=20, relwidth=0.248)
        self.e_pasportNumber.configure(background="red")
        self.date_of_pasport_release  = DateEntry(self.tkTab_1, date_pattern='DD.MM.YYYY', width=12, foreground='black')
        self.date_of_pasport_release.place(relx=0.662, rely=0.1, height=20, relwidth=0.248)
        self.date_of_pasport_release.configure(background="yellow")

        self.cbox_gender = ttk.Combobox(self.tkTab_1, takefocus="", values=('муж','жен'))
        self.cbox_gender.place(relx=0.197, rely=0.25, relheight=0.105, relwidth=0.242)
        self.cbox_ctzn = ttk.Combobox(self.tkTab_1, takefocus="", values=('RU','UA', 'KZ'))
        self.cbox_ctzn.place(relx=0.197, rely=0.45, relheight=0.105, relwidth=0.242)

        self.date_of_birth =  DateEntry(self.tkTab_1, date_pattern='DD.MM.YYYY', width=12, foreground='black')
        self.date_of_birth.place(relx=0.667, rely=0.25, height=20, relwidth=0.248)
        self.date_of_birth.configure(background="green")

        self.e_address = tk.Text(self.tkTab_1)
        self.e_address.place(relx=0.576, rely=0.45, relheight=0.32, relwidth=0.339)
        self.e_address.configure(background="white")
        self.e_address.configure(wrap="word")

        #region >>>>> LABELS <<<<<
        self.Label1 = tk.Label(self.Labelframe1, background="#d9d9d9", text='''Имя:''')
        self.Label1.place(relx=0.059, rely=0.24, height=21, width=41, bordermode='ignore')
        self.Label2 = tk.Label(self.Labelframe1, background="#d9d9d9", text='''Фамилия:''')
        self.Label2.place(relx=0.038, rely=0.48, height=21, width=60, bordermode='ignore')
        self.Label4 = tk.Label(self.Labelframe1, background="#d9d9d9", text='''Отчество:''')
        self.Label4.place(relx=0.038, rely=0.72, height=21, width=60, bordermode='ignore')
        self.Label4 = tk.Label(self.Labelframe1, background="#d9d9d9", text='''Номер телефона:''')
        self.Label4.place(relx=0.478, rely=0.24, height=21, width=109, bordermode='ignore')
        self.Label2 = tk.Label(self.tkTab_0, background="#d9d9d9", text='''Основная специальность:''')
        self.Label2.place(relx=0.015, rely=0.2, height=21, width=149)
        self.Label2 = tk.Label(self.tkTab_1, background="#d9d9d9", text='''Серия и номер:''')
        self.Label2.place(relx=0.03, rely=0.1, height=21, width=92)
        self.Label3 = tk.Label(self, background="#d9d9d9", text='''Дата регистрации:''')
        self.Label3.place(relx=0.014, rely=0.022, height=21, width=107)
        self.Label5 = tk.Label(self.tkTab_1, background="#d9d9d9", text='''Пол:''')
        self.Label5.place(relx=0.047, rely=0.25, height=21, width=80)
        self.Label5 = tk.Label(self.tkTab_1, background="#d9d9d9", text='''Гражданство:''')
        self.Label5.place(relx=0.047, rely=0.45, height=21, width=80)
        self.Label4 = tk.Label(self.tkTab_1, background="#d9d9d9", text='''Дата выдачи:''')
        self.Label4.place(relx=0.53, rely=0.1, height=21, width=78)
        self.Label6 = tk.Label(self.tkTab_0, background="#d9d9d9", text='''На базе:''')
        self.Label6.place(relx=0.015, rely=0.05, height=21, width=54)
        self.Label6 = tk.Label(self.tkTab_1, background="#d9d9d9", text='''Дата рождения:''')
        self.Label6.place(relx=0.506, rely=0.25, height=21, width=89)
        self.Label7 = tk.Label(self.tkTab_1, background="#d9d9d9", text='''Адресс:''')
        self.Label7.place(relx=0.5, rely=0.4, height=21, width=42)
        self.Label9 = tk.Label(self.tkTab_2, background="#d9d9d9", text='''Балл атестата:''')
        self.Label9.place(relx=0.015, rely=0.1, height=21, width=89)
        #endregion
        self.b_add = tk.Button(self, activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", pady="0", text='''Добавить''')
        self.b_add.place(relx=0.365, rely=0.911, height=24, width=63)
        self.b_cancel = tk.Button(self, activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", pady="0", text='''Дать пинка!''')
        self.b_cancel.place(relx=0.501, rely=0.911, height=24, width=75)

        self.grab_set()
        self.focus_set()

    # endregion
