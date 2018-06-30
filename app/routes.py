from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user
from flask_login import login_required
from app.models import User
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required#防止未登录访问，它会添加一个查询字符串参数来丰富这个URL，如/login?next=/index
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home Page', posts=posts)
    
    
#登陆
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:#一个用来表示用户是否通过登录认证的属性，用True和False表示
        return redirect(url_for('index'))#如果已登录，重定向到index
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()#查询表单username是否在数据库中
        if user is None or not user.check_password(form.password.data):#如果不存在或密码错误
            flash('invalid username or password!')#提示
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)#该函数会将用户登录状态注册为已登录，应用都会将用户实例赋值给current_user变量
        next_page = request.args.get('next')#request.args属性，可用友好的字典格式暴露查询字符串的内容
        if not next_page or url_parse(next_page).netloc != '':#url_parse()函数解析，然后检查netloc属性是否被设置
            next_page = url_for('index')
        return redirect(next_page)
        #flash('Login requested for user {}, remember_me{}'.format(
            #form.username.data, form.remember_me.data))
        #return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
    
    
#登出
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
    
    
#注册
@app.route('/register',methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:#如果用户已登录
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)#set_password将密码加密
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
