import urllib.request
from bs4 import BeautifulSoup
from Course import Course
from connection import Db


def getDataFromURL():
    # url = "https://rds1.northsouth.edu/index.php/showofferedcourses"
    # source_code = urllib.request.urlopen(url)
    #
    # soup = BeautifulSoup(source_code.read(), "html.parser")
    soup = BeautifulSoup(open("weblink/SPRING2018/OnlinePortalNorthSouthUniversity.html"), "html.parser")

    for tr in soup.find_all('tr'):
        course = Course()
        crs = []
        for td in tr.find_all('td'):
            # print(td.text.strip())
            crs.append(td.text.strip())
            # crs.set_no(td.text.strip())
        if crs:
            # print(crs[1])
            course.set_no(crs[0])
            course.set_name(crs[1])
            course.set_sec(crs[2])
            course.set_faculty(crs[3])
            course.set_time(crs[4])
            course.set_room(crs[5])
            course.set_capacity(crs[6])
        # print(course.get_name())
        print(course.get_name())
        if course.get_no() is not None or course.get_name() is not None or course.get_sec()!= None or course.get_faculty()!= None or course.get_time()!= None or course.get_room()!= None or course.get_capacity()!= None:
            insertIntoDatabase(course, "SPRING18")


def insertIntoDatabase(course, semester):
    db = Db()
    conn = db.connect()
    cur = conn.cursor()
    # query = "insert into offerlist( semesterName, courseNo, courseName, sec, faculty, time, room, capacity) values ('summer','1','cse115',1,'akr','n/a','141','40/40')"

    query = "insert into offerlist( semesterName, courseNo, courseName, sec, faculty, coursetime, room, capacity) values (%s,%s,%s,%s,%s,%s,%s,%s)"

    cur.execute(query, (semester, course.get_no(), course.get_name(), course.get_sec(), course.get_faculty(), course.get_time(), course.get_room(), course.get_capacity()))
    conn.commit()


# insertIntoDatabase()
# getDataFromURL()

def showResult():
    db = Db()
    # conn = db.connect()
    # cur = conn.cursor()
    db.searchQuery("ACT201")


showResult()