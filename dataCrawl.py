import urllib.request
from bs4 import BeautifulSoup

from Course import Course


def getDataFromURL():

    url = "https://rds1.northsouth.edu/index.php/showofferedcourses"
    source_code = urllib.request.urlopen(url)

    soup = BeautifulSoup(source_code.read(),"html.parser")

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





getDataFromURL()