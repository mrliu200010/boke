f = open("article.txt", 'r+')
lists = f.readlines()
print(lists)
f.close()




# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         if not current_user.is_authenticated:
#             return redirect(url_for('index'))
#         # 获取表单的数据
#         title = request.form.get('title')
#         year = request.form.get('year')
#
#         # 验证title，year不为空，并且title长度不大于60，year的长度不大于4
#         if not title or not year or len(year) > 4 or len(title) > 60:
#             flash('输入错误')  # 错误提示
#             return redirect(url_for('index'))  # 重定向回主页
#
#         movie = Movie(title=title, year=year)  # 创建记录
#         db.session.add(movie)  # 添加到数据库会话
#         db.session.commit()  # 提交数据库会话
#         flash('数据创建成功')
#         return redirect(url_for('index'))
#
#     movies = Ariticles.query.all()
#     return render_template('index.html', movies=movies)


# if request.method == 'POST':
#     if not current_user.is_authenticated:
#         return redirect(url_for('index'))
#     # 获取表单的数据
#     title = request.form.get('title')
#     content = request.form.get('content')
#     author = request.form.get('author')
#     pubdate = request.form.get('pubdate')
#
#     # 验证title，year不为空，并且title长度不大于60，year的长度不大于4
#     if not title or not content or not author or not pubdate or len(pubdate) > 4 or len(
#             title) > 20 or content > 2000 or author < 0:
#         flash('输入错误')  # 错误提示
#         return redirect(url_for('index'))  # 重定向回主页
#
#     Ariticle = Ariticles(title=title, content=content, author=author, pubdate=pubdate)  # 创建记录
#     db.session.add(Ariticle)  # 添加到数据库会话
#     db.session.commit()  # 提交数据库会话
#     flash('数据创建成功')
#     return redirect(url_for('index'))