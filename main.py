import sys
import tkinter as tk
from tkinter import ttk, IntVar
import sqlite3, configobj
from tkcalendar import DateEntry
from datetime import date
from tkinter import messagebox

from Child_window import Child

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()


    def init_main(self):
        clmn_names = ('ID', 'Имя', 'Фамилия', 'Отчество', 'Номер', 'Дата регистрации', 'Ср балл', 'На базе')
        clmn_width = (10, 70, 70, 100, 80, 100, 150, 50)

        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_open_dialog = tk.Button(toolbar, text='Add |', command=self.open_dialog, bg='#d7d8e0', bd=0, compound=tk.TOP)
        btn_edit_dialog = tk.Button(toolbar, text=' Edit |', bg='#d7d8e0', bd=0, compound=tk.TOP, command=self.open_update_dialog)
        btn_delete = tk.Button(toolbar, text=' Delete', bg='#d7d8e0', bd=0, compound=tk.TOP, command=self.delete_records)
        self.cbox_all_spec = ttk.Combobox(toolbar, cursor="fleur", width= 50, state='readonly')
        self.cbox_all_spec.bind("<<ComboboxSelected>>",  lambda event: self.view_records(self.cbox_all_spec.get()))
        e_search = tk.Entry(toolbar, width = 100)

        for c in (btn_open_dialog,btn_edit_dialog, btn_delete, self.cbox_all_spec, e_search):
            c.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=clmn_names,height=15, show='headings')
        for indx in range(len(clmn_names)):
            self.tree.column(clmn_names[indx], width=clmn_width[indx], anchor=tk.CENTER)
            self.tree.heading(clmn_names[indx], text=clmn_names[indx])
        self.tree.pack()
        self.tree.bind("<Double-1>", lambda event: self.full_info())

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

    # def update_record(self, description, costs, total):
    #     self.db.c.execute('''update abiturients set description=?, costs=?, total=? where ID=?''',
    #                       (description, costs, total, self.tree.set(self.tree.selection()[0], '#1')))
    #     self.db.conn.commit()
    #     self.view_records()

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('delete from abiturients where id=?',([self.tree.set(selection_item,'#1')]))
        self.db.conn.commit()
        self.view_records()

    def open_dialog(self):
        Child(root,app,db)

    def open_update_dialog(self):
        Update()

class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.entry_description.insert(0, self.tree.selection()[0], '#2')

        self.title('Edit position')
        btn_edit = ttk.Button(self, text='Edit')
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.combobox.get(),
                                                                          self.entry_money.get()))
        self.btn_ok.destroy()



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
        self.c.execute('''INSERT INTO abiturients VALUES (NULL,?,?,?,?,?,?,?,?)''',
                       args[0])
        self.conn.commit()






if __name__ == "__main__":

    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Приемная комисия")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
