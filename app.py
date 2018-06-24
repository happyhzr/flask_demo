from flask import Flask, render_template, request, redirect, url_for, session

import config
from models import User, Question
from exts import db
from decorators import login_required

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    context = {
        'questions': Question.query.order_by('-create_time').all(),
    }
    return render_template('index.html', **context)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        phone = request.form.get('phone')
        password = request.form.get('password')
        user = User.query.filter(User.phone == phone).first()
        if not user:
            return '用户不存在'
        if password != user.password:
            return '密码错误'

        session['user_id'] = user.id
        session.permanent = True
        return redirect(url_for('index'))


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


@app.route('/logout/')
def logout():
    session.pop('user_id')
    return redirect(url_for('login'))


@app.route('/question/', methods=['GET', 'POST'])
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        question = Question(title=title, content=content, author=user)
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))


@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}


if __name__ == '__main__':
    app.run()
