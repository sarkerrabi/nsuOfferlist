import MySQLdb
from MySQLdb import Error


class Db:

    def connect(self):
        global conn
        try:
            conn = MySQLdb.connect(host='localhost', database='nsuOfferlistCrisis', user='rabi',
                                   password='1234')

            if conn:
                print("connection Success full")
                return conn
        except Error as e:
            print(e)