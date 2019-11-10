import sqlite3


class Backend:
    def __init__(self):
        self.conn = sqlite3.connect('commission.db')

        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS abiturients
        (id INTEGER primary KEY, SI TEXT, SF TEXT, SO TEXT, Phone TEXT, DateReg TEXT
        AvrgBall REAL,
        OnBase BLOB)''')
        self.conn.commit()
        #IF NOT EXISTS

    #================================ MAIN WINDOW ===============================================#

    def search_result(self, search_str):
        return self.c.execute("select * from abiturients where LOWER(SF) like '%{}%' ".format(search_str)).fetchall()

    def deliting(self, element):
        self.c.execute('delete from abiturients where id=?', (element))
        self.conn.commit()




    # ==================================CHILD WINDOW HELPER========================================#

    def return_rb_dictionary(self, value):
        self.list_of_specialties = dict(self.c.execute(
            'select id, SpecName from specialty where speconbase = ' + str(value)).fetchall())
        return self.list_of_specialties


    # ==================================ADDING SPECIALITY========================================#

    def add_spec(self, *args):
        print('SQL addspec:  ', args)
        self.c.execute('''INSERT INTO specialty VALUES (NULL,?,?)''',(args))
        self.conn.commit()


    #==================================ADDING================================================#
    def insert_data(self, *args):
        print('SQL insert:  ', args[0])
        self.c.execute('''INSERT INTO abiturients VALUES (NULL,?,?,?,?,?,?,?,? ,?,?,?,?,?,? ,?, ?,?,?)''',(args[0]))
        self.conn.commit()


    #==================================EDITING================================================#
    def get_data_for_editing(self, selected_id_id):
        self.c.execute('''select * from abiturients where ID=''' + selected_id_id)

        return self.c.fetchall()

    def update_after_editing(self, selected_id,  *args):
        print('SQL updated:  ', args[0])
        self.c.execute('''update abiturients set DateReg=?, SF=?,SI=?,SO=?,Phone=?,OnBase=?,AvrgBall=?,
        Spec1Mark1=?,Spec1Mark2=?,Spec1=?,PassNumber=?,PassGender=?,PassCitizenship=?,PassDateOfRelease=?,
        PassDateOfBirth=?,PassAddress=?,AttNumb=?,AttYear=? where ID='''+str(selected_id),
                          args[0])
        self.conn.commit()




