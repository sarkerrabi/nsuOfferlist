import MySQLdb
from MySQLdb import Error

from Course import Course


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

    def searchQuery(self, cou, faculty):
        db = Db()
        conn = db.connect()
        cur = conn.cursor()

        if cou and faculty:
            cur.execute(
                "SELECT semesterName,courseName,sec,faculty,coursetime,room,capacity FROM offerlist WHERE courseName= %(courseName)s and faculty= %(facultyName)s",
                {'courseName': cou, 'facultyName': faculty})
        elif cou:
            cur.execute(
                "SELECT semesterName,courseName,sec,faculty,coursetime,room,capacity FROM offerlist WHERE courseName= %(courseName)s",
                {'courseName': cou})
        elif faculty:
            cur.execute(
                "SELECT semesterName,courseName,sec,faculty,coursetime,room,capacity FROM offerlist WHERE faculty= %(facultyName)s",
                {'facultyName': faculty})




        # rows = cur.fetchone()
        # course = Course()
        # course.set_semester(rows[0])
        # course.set_name(rows[1])
        # course.set_sec(rows[2])
        # course.set_faculty(rows[3])
        # course.set_time(rows[4])
        # course.set_room(rows[5])
        # course.set_capacity(rows[6])
        #
        # print(course.get_faculty())

        crs = []
        rows = cur.fetchall()
        # for each_row in rows :
        #     course = Course()
        #     course.set_semester(each_row[0])
        #     course.set_name(each_row[1])
        #     course.set_sec(each_row[2])
        #     course.set_faculty(each_row[3])
        #     course.set_time(each_row[4])
        #     course.set_room(each_row[5])
        #     course.set_capacity(each_row[6])
        #     # print(course.get_faculty())
        #     crs.append(course)
        # print(crs[0].get_faculty())

        return rows
