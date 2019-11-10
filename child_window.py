import sys
import tkinter as tk
from tkinter import ttk, IntVar, StringVar
from tkcalendar import DateEntry

from backend import Backend

db = Backend()

list_of_genders= ('муж','жен')
list_of_stzens = ('RU','UA', 'KZ')


        
class AddingWindow(tk.Toplevel):
    
    

    # region >>>>>> CHILD <<<<<
    def __init__(self, root, app):
        self.title_value = StringVar()
        self.title_value.set("Добавление абитуриента")
        super().__init__(root)
        self.init_child()
        self.view = app

        self.click_radiobtn()

        

        self.b_add.bind('<Button-1>', lambda event: self.add_records())
        self.b_cancel.bind('<Button-1>', lambda event: self.destroy())



    def init_child(self):
        self.rb_onbase_value = IntVar()
        self.rb_onbase_value.set(9)

        self.title( self.title_value.get())
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

        self.e_attestNumb = tk.Entry(self.tkTab_2, font="TkFixedFont")
        self.e_attestNumb.place(relx=0.167, rely=0.1, height=20, relwidth=0.212)
        self.e_attestYear = tk.Entry(self.tkTab_2, font="TkFixedFont")
        self.e_attestYear.place(relx=0.167, rely=0.3, height=20, relwidth=0.112)
        self.e_avgball = tk.Entry(self.tkTab_2, font="TkFixedFont")
        self.e_avgball.place(relx=0.667, rely=0.1, height=20, relwidth=0.112)

        self.rad_btn9 = ttk.Radiobutton(self.tkTab_0, text='''9 классов''', variable=self.rb_onbase_value, value=9,command=self.click_radiobtn)
        self.rad_btn9.place(relx=0.106, rely=0.05, relheight=0.125, relwidth=0.123)
        self.rad_btn11 = tk.Radiobutton(self.tkTab_0, background="#d9d9d9", text='''11 классов''',variable=self.rb_onbase_value, value=11, command=self.click_radiobtn)

        self.cbox_spec = ttk.Combobox(self.tkTab_0, cursor="fleur", state='readonly')
        self.cbox_spec.place(relx=0.273, rely=0.2, relheight=0.105, relwidth=0.400)
        self.e_mark1 = tk.Entry(self.tkTab_0, font="TkFixedFont")
        self.rad_btn11.place(relx=0.242, rely=0.05, relheight=0.125, relwidth=0.132)
        self.e_mark1.place(relx=0.4, rely=0.4, height=20, relwidth=0.05)
        self.e_mark2 = tk.Entry(self.tkTab_0, font="TkFixedFont")
        self.e_mark2.place(relx=0.4, rely=0.6, height=20, relwidth=0.05)

        self.e_pasportNumber = tk.Entry(self.tkTab_1)
        self.e_pasportNumber.place(relx=0.197, rely=0.1, height=20, relwidth=0.248)
        self.date_of_pasport_release  = DateEntry(self.tkTab_1, date_pattern='DD.MM.YYYY', width=12, foreground='black')
        self.date_of_pasport_release.place(relx=0.662, rely=0.1, height=20, relwidth=0.248)
        self.date_of_pasport_release.configure(background="yellow")

        self.cbox_gender = ttk.Combobox(self.tkTab_1, takefocus="", values=list_of_genders, state='readonly')
        self.cbox_gender.place(relx=0.197, rely=0.25, relheight=0.105, relwidth=0.242)
        self.cbox_gender.current(0)
        self.cbox_ctzn = ttk.Combobox(self.tkTab_1, takefocus="", values=list_of_stzens, state='readonly')
        self.cbox_ctzn.place(relx=0.197, rely=0.45, relheight=0.105, relwidth=0.242)
        self.cbox_ctzn.current(0)

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
        self.Label21 = tk.Label(self.tkTab_0, background="#d9d9d9", text='''Оценка первого профильного предмета:''')
        self.Label21.place(relx=0.015, rely=0.4, height=21, width=249)
        self.Label22 = tk.Label(self.tkTab_0, background="#d9d9d9", text='''Оценка второго профильного предмета:''')
        self.Label22.place(relx=0.015, rely=0.6, height=21, width=249)
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
        self.Label9 = tk.Label(self.tkTab_2, background="#d9d9d9", text='''Номер атестата:''')
        self.Label9.place(relx=0.015, rely=0.1, height=21, width=89)

        self.Label91 = tk.Label(self.tkTab_2, background="#d9d9d9", text='''Год выдачи:''')
        self.Label91.place(relx=0.015, rely=0.3, height=21, width=89)

        self.Label92 = tk.Label(self.tkTab_2, background="#d9d9d9", text='''Балл атестата:''')
        self.Label92.place(relx=0.5, rely=0.1, height=21, width=89)
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

    def fields_values(self):
        return self.date_of_registration.get(),
        self.e_SF.get(),
        self.e_SI.get(),
        self.e_SO.get(),
        self.e_phone.get(),
        self.rb_onbase_value.get(),
        self.e_avgball.get().replace(',', '.'),
        self.e_mark1.get(),
        self.e_mark2.get(),

        self.get_spec_id_from_cbox(self.cbox_spec.get()),
        self.e_pasportNumber.get(),
        self.cbox_gender.get(),
        self.cbox_ctzn.get(),
        self.date_of_pasport_release.get(),
        self.date_of_birth.get(),
        self.e_address.get(1.0, tk.END),
        self.e_attestNumb.get(),
        self.e_attestYear.get()

    def add_records(self):
        db.insert_data(self.fields_values() )
        self.view.view_records()
        self.destroy()

    def click_radiobtn(self):
        self.cbox_spec['values'] =  list(db.return_rb_dictionary(self.rb_onbase_value.get()).values())

    def get_spec_id_from_cbox(self, selected_str):
        for k, v in db.return_rb_dictionary(self.rb_onbase_value.get()).items():
            if v == selected_str:
                return k

    # endregion
class EditingWindow(AddingWindow):
    def __init__(self, root, app,  selected_id):
        super().__init__( root, app, )
        self.selected_id = selected_id
        self.init_edit()
        self.paste_data()
        self.title('Редактировать данные')


    def init_edit(self):
        self.b_update = ttk.Button(self, text='Обновить')
        self.b_update.place(relx=0.365, rely=0.911, height=24, width=63)
        self.b_update.bind('<Button-1>', lambda event: db.update_after_editing(self.selected_id, self.fields_values()))
        self.b_add.destroy()

    def paste_data(self):
        self.listOfData = db.get_data_for_editing(self.selected_id)[0]
        self.listOfData = [' ' if x is None else x for x in self.listOfData]


        self.date_of_registration.set_date(self.listOfData[1]); self.date_of_registration.config(date_pattern='DD.MM.YYYY')
        self.e_SF.insert(0,self.listOfData[2])
        self.e_SI.insert(0,self.listOfData[3])
        self.e_SO.insert(0,self.listOfData[4])
        self.e_phone.insert(0,self.listOfData[5])
        self.rb_onbase_value.set(self.listOfData[6])
        self.e_avgball.insert(0,self.listOfData[7])
        self.e_mark1.insert(0,self.listOfData[8])
        self.e_mark2.insert(0,self.listOfData[9])

        #self.cbox_spec.current(self.cbox_spec['values'].index( self.list_of_specialties.get(self.listOfData[10]))); print(self.cbox_spec['values'])
        self.e_pasportNumber.insert(0,self.listOfData[11])
        self.cbox_gender.current(list_of_genders.index(self.listOfData[12]))
        self.cbox_ctzn.current(list_of_stzens.index(self.listOfData[13]))
        self.date_of_pasport_release.set_date(self.listOfData[14]); self.date_of_pasport_release.config(date_pattern='DD.MM.YYYY')
        self.date_of_birth.set_date(self.listOfData[15]); self.date_of_birth.config(date_pattern='DD.MM.YYYY')
        self.e_address.insert(1.0,self.listOfData[16])
        self.e_attestNumb.insert(0,self.listOfData[17])
        self.e_attestYear.insert(0,self.listOfData[18])


class AddSpecWindow(tk.Toplevel):
    def __init__(self, root, app):
        self.title_value = StringVar()
        self.title_value.set("Добавление специальности")
        super().__init__(root)
        self.init_child()
        self.view = app
        self.click_radiobtn()



    def init_child(self):

        self.title(self.title_value.get())
        self.geometry("300x100+339+86")
        self.resizable(False, False)
        self.maxsize(1370, 753)

        lbl = tk.Label(self, text='Название специальности:')
        self.e_spec_name = tk.Entry(self, width=100)
        lbl2 = tk.Label(self, text='На базе какого класса:')
        self.e_spec_onbase = tk.Entry(self, width=10)
        btn = tk.Button(self, text='Добавить')
        btn.bind('<Button-1>', lambda event: db.add_spec(self.e_spec_name.get(), self.e_spec_onbase.get()))
        for item in (lbl, self.e_spec_name,  lbl2,self.e_spec_onbase, btn ):
            item.pack()



