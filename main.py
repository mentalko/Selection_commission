import sys
import tkinter as tk
from tkinter import ttk, IntVar
import sqlite3, configobj
from tkcalendar import DateEntry
from datetime import date
from tkinter import messagebox

from child_window import *


# TODO:  Editing

class Main(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()


    def init_main(self):
        clmn_names = ('ID',  'Дата регистрации',  'Фамилия', 'Имя', 'Отчество', 'Номер телефона','На базе', 'Ср балл',  'Оценка 1', 'Оценка 2')
        clmn_width = (10,100,  90, 70, 100, 100, 50, 80, 30,30)

        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        toolbar2 = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar2.pack(side=tk.TOP, fill=tk.BOTH)

        btn_open_dialog = tk.Button(toolbar, text='Добавить  |', command=self.open_dialog, bg='#d7d8e0', bd=0, compound=tk.TOP)
        btn_edit_dialog = tk.Button(toolbar, text='  Редактировать  |', bg='#d7d8e0', bd=0, compound=tk.TOP, command=self.open_update_dialog)
        btn_delete = tk.Button(toolbar, text='  Удалить  |', bg='#d7d8e0', bd=0, compound=tk.TOP, command=self.delete_records)
        btn_add_spec = tk.Button(toolbar, text='  Добавить Специальность  |', bg='#d7d8e0', bd=0, compound=tk.TOP, command=self.open_add_spec_dialog)
        self.cbox_all_spec = ttk.Combobox(toolbar, cursor="fleur", width= 50, state='readonly')
        self.cbox_all_spec.bind("<<ComboboxSelected>>",  lambda event: self.view_records(self.cbox_all_spec.get()))
        self.e_search = tk.Entry(toolbar2, width = 100)
        self.e_search.bind('<Key>', lambda event: self.search(self.e_search.get()))

        for c in (btn_open_dialog,btn_edit_dialog, btn_delete, btn_add_spec, self.cbox_all_spec):
            c.pack(side=tk.LEFT)
        self.e_search.pack(side=tk.TOP, fill=tk.X)
        self.tree = ttk.Treeview(toolbar2, columns=clmn_names,height=50, show='headings')
        for indx in range(len(clmn_names)):
            self.tree.column(clmn_names[indx], width=clmn_width[indx])
            self.tree.heading(clmn_names[indx], text=clmn_names[indx])
        self.tree.pack( fill=tk.BOTH, expand = True, anchor='w')
        self.tree.bind("<Double-1>", lambda event: self.full_info())

    def search(self, string):
        print(string)
        self.db.c.execute("select * from abiturients where LOWER(SF) like '%{}%' ".format( self.e_search.get()))

        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def full_info(self):
        print(self.tree.set(self.tree.selection()[0]))
        messagebox.showinfo('Full info', str(self.tree.set(self.tree.selection()[0])).replace(',', '\n').replace("'", '').replace("{", '')
                            .replace("}", ''))

    def view_records(self, *selected_str):
        self.all_specialties = dict(self.db.c.execute(
            'select  id, SpecName from specialty').fetchall())
        all_spec = list(self.all_specialties.values())
        all_spec.insert(0, '')
        self.cbox_all_spec['values'] = all_spec

        if not selected_str or selected_str[0] == '':
            self.db.c.execute('''select * from abiturients''')
        else:
            for k, v in self.all_specialties.items():
                if v == selected_str[0]:
                    self.db.c.execute('''select * from abiturients where spec1=? order by avrgball desc''', [k])
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]\

    def add_records(self, *args):
        self.db.insert_data(args)
        self.view_records()

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('delete from abiturients where id=?',([self.tree.set(selection_item,'#1')]))
        self.db.conn.commit()
        self.view_records()

    def open_dialog(self):
        Child(root,app,db)

    def open_update_dialog(self): pass

    def open_add_spec_dialog(self):
        AddSpec(root,app,db)


    def edit_record(self, description, costs, total):
        self.db.c.execute('''update abiturients set description=?, costs=?, total=? where ID=?''',
                          (description, costs, total, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_records()



class DB:
    def __init__(self):
        self.conn = sqlite3.connect('commission.db')

        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS abiturients
        (id INTEGER primary KEY, SI TEXT, SF TEXT, SO TEXT, Phone TEXT, DateReg TEXT
        AvrgBall REAL,
        OnBase BLOB)''')
        self.conn.commit()
        #IF NOT EXISTS
    def insert_data(self, *args):
        print('SQL ', args)
        self.c.execute('''INSERT INTO abiturients VALUES (NULL,?,?,?,?,?,?,?,? ,?,?,?,?,?,? ,?, ?,?,?)''',
                       args[0])
        self.conn.commit()

if __name__ == "__main__":

    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Приемная комисия")
    root.geometry("850x650+200+50")

    root.resizable(True, True)
    root.mainloop()


  # inifile = 'config.ini'
        # self.config = configobj.ConfigObj(inifile)
        # variable = self.config['Variables']
        # value = self.config['Values']