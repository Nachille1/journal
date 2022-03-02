from flask import Flask, render_template
from data import db_session
from data import jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def main():
    db_session.global_init('db/blogs.db')
    db_sess = db_session.create_session()
    jobs_list = db_sess.query(jobs.Jobs).all()
    print(jobs_list)
    return render_template('1.html', jobs_list=jobs_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
