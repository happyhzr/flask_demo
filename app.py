from flask import Flask, render_template, request, redirect, url_for

import config
from models import User
from exts import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        phone = request.form.get('phone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if password1 != password2:
            return '密码不相等'

        user = User.query.filter(User.phone == phone).first()
        if user:
            return '该手机号码已被注册'

        user = User(phone=phone, username=username, password=password1)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
