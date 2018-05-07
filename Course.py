class Course:

    def __init__(self, no=None, name=None, sec=None, faculty=None, time=None, room=None, capacity=None):
        self.__no = no
        self.__name = name
        self.__sec = sec
        self.__faculty = faculty
        self.__time = time
        self.__room = room
        self.__capacity = capacity



    def get_no(self):
        return self.__no

    def get_name(self):
        return self.__name

    def get_sec(self):
        return self.__sec

    def get_faculty(self):
        return self.__faculty

    def get_time(self):
        return self.__time

    def get_room(self):
        return self.__room

    def get_capacity(self):
        return self.__capacity

    def set_no(self, no):
        self.__no = no

    def set_name(self, name):
        self.__name = name

    def set_sec(self, sec):
        self.__sec = sec

    def set_faculty(self, faculty):
        self.__faculty = faculty

    def set_time(self, time):
        self.__time = time

    def set_room(self, room):
        self.__room = room

    def set_capacity(self, capacity):
        self.__capacity = capacity
