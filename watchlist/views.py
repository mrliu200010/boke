from watchlist import app, db
from flask import request, redirect, url_for, flash, render_template
from flask_login import login_user, logout_user, login_required, current_user
from watchlist.models import User, Movie, Ariticles


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('add'))
    Ariticle = Ariticles.query.all()
    return render_template('index.html', Ariticles=Ariticle)


#添加页面
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form.get('title')
        content_ = request.form.get('content')
        content_2 = content_.replace('<p>', '')
        content = content_2.replace('</p>', '')
        author = request.form.get('author')
        pubdate = request.form.get('pubdate')

        # 验证title，year不为空，并且title长度不大于60，year的长度不大于4
        if not title or not content or not author or not pubdate or len(
                title) > 20  or len(author) > 10:
            flash('输入错误')  # 错误提示
            return redirect(url_for('add'))  # 重定向回添加

        Ariticle = Ariticles(title=title, content=content, author=author, pubdate=pubdate)  # 创建记录
        db.session.add(Ariticle)  # 添加到数据库会话
        db.session.commit()  # 提交数据库会话
        flash('数据创建成功')
        return redirect(url_for('index'))
    return render_template('add.html')

# 编辑电影信息页面
@app.route('/movie/edit/<int:articles_id>', methods=['GET', 'POST'])
@login_required
def edit(articles_id):
    Ariticle = Ariticles.query.get_or_404(articles_id)

    if request.method == 'POST':
        title = request.form.get('title')
        content_ = request.form.get('content')
        content_2=content_.replace('<p>', '')
        content=content_2.replace('</p>', '')
        author = request.form.get('author')
        pubdate = request.form.get('pubdate')

        # 验证title，year不为空，并且title长度不大于60，year的长度不大于4
        if not title or not content or not author or not pubdate or len(pubdate) > 4 or len(
                title) > 20 or len(content) > 2000 or len(author) > 10:
            flash('输入错误')  # 错误提示
            return redirect(url_for('edit'), articles_id=articles_id)

        Ariticle.title = title
        Ariticle.content = content
        Ariticle.author = author
        Ariticle.pubdate = pubdate
        db.session.commit()
        flash('电影信息已经更新')
        return redirect(url_for('index'))
    return render_template('edit.html', article=Ariticle)


#博文页面
@app.route('/movie/check/<int:articles_id>', methods=['GET', 'POST'])

def check(articles_id):
    Ariticle = Ariticles.query.get_or_404(articles_id)
    return render_template('check.html', article=Ariticle)



# 编辑名称
@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        name = request.form['name']

        if not name or len(name) > 20:
            flash('输入错误')
            return redirect(url_for('settings'))

        current_user.name = name
        db.session.commit()
        flash('设置name成功')
        return redirect(url_for('index'))

    return render_template('settings.html')


# 删除信息
@app.route('/movie/delete/<int:articles_id>', methods=['POST'])
@login_required
def delete(articles_id):
    movie = Ariticles.query.get_or_404(articles_id)
    db.session.delete(movie)
    db.session.commit()
    flash('删除数据成功')
    return redirect(url_for('index'))


# 用户登录 flask提供的login_user()函数
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('输入错误')
            return redirect(url_for('login'))
        user = User.query.first()
        if username == user.username and user.validate_password(password):
            login_user(user)  # 登录用户
            flash('登录成功')
            return redirect(url_for('index'))  # 登录成功返回首页
        flash('用户名或密码输入错误')
        return redirect(url_for('login'))
    return render_template('login.html')


# 用户登出
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('退出登录')
    return redirect(url_for('index'))
