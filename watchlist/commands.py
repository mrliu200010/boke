import click
from watchlist import app,db
from watchlist.models import User,Movie,Ariticles
# 自定义initdb
@app.cli.command()
@click.option('--drop',is_flag=True,help='删除之后再创建')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('初始化数据库')

# 自定义命令forge，把数据写入数据库
@app.cli.command()
def forge():
    db.create_all()
    name = "mrliu"
    movies = [
        {'title':'杀破狼','year':'2003'},
        {'title':'扫毒','year':'2018'},
        {'title':'捉妖记','year':'2016'},
        {'title':'囧妈','year':'2020'},
        {'title':'葫芦娃','year':'1989'},
        {'title':'玻璃盒子','year':'2020'},
        {'title':'调酒师','year':'2020'},
        {'title':'釜山行','year':'2017'},
        {'title':'导火索','year':'2005'},
        {'title':'叶问','year':'2015'}
    ]
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'],year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo('数据导入完成')

#
@app.cli.command()
def aaa():
    db.create_all()
    name = "mrliu"
    articles = [
        {'title':'杀破狼','content':'2003','pubdate':'2000'},
        {'title':'扫毒','content':'2018','pubdate':'2000'},
        {'title':'捉妖记','content':'2016','pubdate':'2000'},
        {'title':'囧妈','content':'2020','pubdate':'2000'},
        {'title':'葫芦娃','content':'1989','pubdate':'2000'},
        {'title':'玻璃盒子','content':'2020','pubdate':'2000'},
        {'title':'调酒师','content':'2020','pubdate':'2000'},
        {'title':'釜山行','content':'2017','pubdate':'2000'},
        {'title':'导火索','content':'2005','pubdate':'2000'},
        {'title':'叶问','content':'2015','pubdate':'2000'}
    ]
    user = User(name=name)
    db.session.add(user)
    for a in articles:
        article = Ariticles(title=a['title'], content=a['content'],author='mrliu',pubdate=a['pubdate'])
        db.session.add(article)
    db.session.commit()
    click.echo('数据导入完成')

# 生成admin账号的函数
@app.cli.command()
@click.option('--username',prompt=True,help="用来登录的用户名")
@click.option('--password',prompt=True,hide_input=True,confirmation_prompt=True,help="用来登录的密码")
def admin(username,password):
    db.create_all()
    user = User.query.first()
    if user is not None:
        click.echo('更新用户')
        user.username = username
        user.set_password(password)
    else:
        click.echo('创建用户')
        user = User(username=username,name="admin")
        user.set_password(password)
        db.session.add(user)
    
    db.session.commit()
    click.echo('创建管理员账号完成')


