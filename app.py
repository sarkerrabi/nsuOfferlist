from tkinter.tix import Form

from flask import Flask, render_template, request, url_for, redirect
from connection import Db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def searchit():
    search_crs = request.form['searchcourse']
    search_fac = request.form['searchcfaculty']

    db = Db()
    # conn = db.connect()
    # cur = conn.cursor()
    crs_list = db.searchQuery(search_crs,search_fac)
    list_no = list(range(1, len(crs_list)))

    return render_template('index.html', pre_takes=zip(list_no, crs_list), search=search_crs, fac=search_fac)


if __name__ == '__main__':
    app.run(debug=True)
