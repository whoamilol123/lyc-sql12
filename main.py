from data.db_session import global_init, create_session
from flask import Flask, render_template

from data.jobs import Jobs

global_init('db/some.db')
session = create_session()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    return render_template('log.html', log=session.query(Jobs).all())


if __name__ == '__main__':
    app.run()
