import sqlite3
import secrets
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

conn = sqlite3.connect('urls.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS urls (long_url TEXT, short_code TEXT PRIMARY KEY)''')
conn.commit()


def generate_short_code():
    short_code = secrets.token_urlsafe(8)
    while not is_code_unique(short_code):
        short_code = secrets.token_urlsafe(8)
    return short_code


def is_code_unique(code):
    with sqlite3.connect('urls.db') as conn:
      c = conn.cursor()
    c.execute("SELECT * FROM urls WHERE short_code = ?", (code,))
    return not c.fetchone()


def store_url(long_url, short_code):
    with sqlite3.connect('urls.db') as conn:
      c = conn.cursor()
    c.execute("INSERT INTO urls (long_url, short_code) VALUES (?, ?)", (long_url, short_code))
    conn.commit()


@app.route('/', methods=['GET', 'POST'])
def shorten_url():
    if request.method == 'POST':
        long_url = request.form['long_url']

        # Generate and store short code
        short_code = generate_short_code()
        store_url(long_url, short_code)

        short_url = f"http://localhost:5000/{short_code}"  # Adjust base URL if needed
        return render_template('shortened.html', short_url=short_url)
    return render_template('index.html')


@app.route('/<short_code>')
def redirect_to_original(short_code):
  with sqlite3.connect('urls.db') as conn:
    c = conn.cursor()
    c.execute("SELECT long_url FROM urls WHERE short_code = ?", (short_code,))
    long_url = c.fetchone()[0]
    return redirect(long_url)


if __name__ == '__main__':
    app.run(debug=True)