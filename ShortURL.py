from uuid import uuid4
import sqlite3


def create_short_url(url):
    short_url = is_url_exist(url)
    if short_url is None:
        return insert_new_url(url)
    return short_url


def is_url_exist(url):
    connection = sqlite3.connect('test.db')
    result = connection.execute("SELECT * FROM ShortURL WHERE REAL_URL=?", [url])
    if result:
        return result.fetchone()
    return None


def get_real_url(url):
    connection = sqlite3.connect('test.db')
    result = connection.execute("SELECT REAL_URL FROM ShortURL WHERE SHORT_URL=?", [url])
    if result:
        return result.fetchone()
    return None


def insert_new_url(url):
    result = is_url_exist(url)
    if not result:
        connection = sqlite3.connect('test.db')
        new_url_prefix = uuid4().hex
        connection.execute("INSERT INTO ShortURL VALUES (?, ?)", [url, new_url_prefix]);
        connection.commit()
        connection.close()
        return url, new_url_prefix
    return result

