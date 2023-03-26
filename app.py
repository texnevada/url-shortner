from flask import Flask, redirect
import sqlite3

app = Flask(__name__)
db_file = "urls.db"


def init_db():
    with sqlite3.connect(db_file) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS urls
                     (key TEXT PRIMARY KEY, url TEXT)''')
        # Add some example data
        conn.commit()


def get_url(key):
    with sqlite3.connect(db_file) as conn:
        c = conn.cursor()
        c.execute("SELECT url FROM urls WHERE key=?", (key,))
        result = c.fetchone()
        if result:
            return result[0]
        return None


@app.route('/<key>')
def redirect_url(key):
    url = get_url(key)
    if url:
        return redirect(url)
    else:
        return f"No URL redirect found for '{key}'"


if __name__ == '__main__':
    init_db()
    app.run() #debug=True)
