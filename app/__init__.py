from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)#通知Flask读取并使用配置文件
db = SQLAlchemy(app)#Object Relational Mapper

#通过flask db init来创建mechoblog的迁移存储库，生成名为migrations的新目录
#数据库迁移，数据模型修改，需使用 flask db migrate -m "messages",flask db #migrate命令不会对数据库进行任何更改，只会生成迁移脚本。
#要将更改应用到数据库，必须使用flask db upgrade命令。
#flask db downgrade命令可以回滚上次的迁移
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'
#强制用户在查看应用的特定页面之前登录。如果未登录的用户尝试查看受保护的页面，Fl
#ask-Login将自动将用户重定向到登录表单，并且只有在登录成功后才重定向到用户想查
#看的页面

from app import routes, models
