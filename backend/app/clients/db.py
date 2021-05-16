import psycopg2
import time

from typing import List


class DBClient:

    def __init__(self, db_url):
        self.db_url = db_url
        self.curr_connection = None
        self.cur = None
        self.last_cur_refresh = None
        self.is_session_started = None

    def setup(self):
        try:
            self.curr_connection = psycopg2.connect(self.db_url)
            self.curr_connection.set_session(autocommit=True)
            self.cur = self.curr_connection.cursor()
            self.last_cur_refresh = time.time()
            self.is_session_started = True
        except psycopg2.OperationalError:
            pass

    def check_connection(self):
        if not self.is_session_started:
            self.setup()
        try:
            if (time.time() - self.last_cur_refresh) > 5:
                self.cur.execute('SELECT 1')
        except:
            self.close()
            self.setup()

    def close(self):
        self.curr_connection.close()

    def select(self, query: str, values: List):
        self.check_connection()
        self.cur.execute(query, values)
        result = self.cur.fetchall()
        self.curr_connection.commit()
        return result

    def insert(self, query: str, values: List):
        self.check_connection()
        self.cur.execute(query, values)
