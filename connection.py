import mysql.connector
from mysql.connector import Error


class Db:

    def connect(self):
        global conn
        try:
            conn = mysql.connector.connect(host='localhost', database='nsuOfferlistCrisis', user='rabi',
                                           password='1234')

            if conn.is_connected():
                print("connection Success full")
        except Error as e:
            print(e)

        finally:
            conn.close()



