from flask import Flask, render_template
import sys
import time
from peer import *
import threading
import sqlite3

#conn = sqlite3.connect('test.db')
#cur = conn.cursor()

#cur.execute('''create table users(INTERGER PRIMARY KE)'')


app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('p2pchat.sqlite')
    cur = conn.cursor()
    cur.execute('IF TABLE DOES NOT EXISTS CREATE TABLE peers(name ,host,port)')
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":

    try:
        t1 = threading.Thread(target=main)
        t2 = threading.Thread(target=app.run, args=("localhost", 8000))
        t1.start()
        t2.start()


    except KeyboardInterrupt:
        sys.exit(0)

    except Exception as e:
        sys.exit()


