import sys,configobj
import tkinter as tk
from tkinter import ttk, IntVar
from tkcalendar import DateEntry
from datetime import date
from tkinter import messagebox

from child_window import *
from Backend import Backend

db = Backend()


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.view_records()

    def init_main(self):
        clmn_names = ('ID',  'Дата регистрации',  'Фамилия', 'Имя', 'Отчество', 'Номер телефона','На базе', 'Ср балл',  'Оценка 1', 'Оценка 2')
        clmn_width = (10,100,  90, 70, 100, 100, 50, 80, 30,30)

        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        toolbar2 = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar2.pack(side=tk.TOP, fill=tk.BOTH)

        btn_open_adding_dialog = tk.Button(toolbar, text='Добавить  |', command=self.open_adding_dialog, bg='#d7d8e0', bd=0, compound=tk.TOP)
        btn_edit_dialog = tk.Button(toolbar, text='  Редактировать  |', bg='#d7d8e0', bd=0, compound=tk.TOP, command=self.open_editing_dialog)
        btn_delete = tk.Button(toolbar, text='  Удалить  |', bg='#d7d8e0', bd=0, compound=tk.TOP, command=self.delete_records)
        btn_add_spec = tk.Button(toolbar, text='  Добавить Специальность  |', bg='#d7d8e0', bd=0, compound=tk.TOP, command=self.open_add_spec_dialog)
        self.cbox_all_spec = ttk.Combobox(toolbar, cursor="fleur", width= 50, state='readonly')
        self.cbox_all_spec.bind("<<ComboboxSelected>>",  lambda event: self.view_records(self.cbox_all_spec.get()))
        self.e_search = tk.Entry(toolbar2, width = 100)
        self.e_search.bind('<Key>', self.search)

        for c in (btn_open_adding_dialog,btn_edit_dialog, btn_delete, btn_add_spec, self.cbox_all_spec):
            c.pack(side=tk.LEFT)
        self.e_search.pack(side=tk.TOP, fill=tk.X)
        self.tree = ttk.Treeview(toolbar2, columns=clmn_names,height=50, show='headings')
        for indx in range(len(clmn_names)):
            self.tree.column(clmn_names[indx], width=clmn_width[indx])
            self.tree.heading(clmn_names[indx], text=clmn_names[indx])
        self.tree.pack( fill=tk.BOTH, expand = True, anchor='w')
        self.tree.bind("<Double-1>", lambda event: self.full_info())

    def search(self):
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in db.search_result(self.e_search.get())]

    def full_info(self):
        print(self.tree.set(self.tree.selection()[0]))
        messagebox.showinfo('Full info', str(self.tree.set(self.tree.selection()[0])).replace(',', '\n').replace("'", '').replace("{", '')
                            .replace("}", ''))

    def view_records(self, selected_str=''):
        self.all_specialties = dict(db.c.execute(
            'select  id, SpecName from specialty').fetchall())
        self.cbox_all_spec['values'] = list(self.all_specialties.values())
        #self.cbox_all_spec['values'].insert(0, '')

        if selected_str == '':
            db.c.execute('''select * from abiturients''')
        else:
            for k, v in self.all_specialties.items():
                if v == selected_str:
                    db.c.execute('''select * from abiturients where spec1=? order by avrgball desc''', [k])
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in db.c.fetchall()]



    def delete_records(self):
        for selection_item in self.tree.selection():
            db.deliting([self.tree.set(selection_item, '#1')])
        self.view_records()

    def open_adding_dialog(self):
        AddingWindow(root,app)

    def open_editing_dialog(self):
        EditingWindow(root,app,self.tree.set(self.tree.selection()[0], '#1'))

    def open_add_spec_dialog(self):
        AddSpecWindow(root,app)

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Приемная комисия")
    root.geometry("850x650+200+50")

    root.resizable(True, True)
    root.mainloop()

