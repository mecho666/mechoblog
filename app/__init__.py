from flask import Flask, g
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging, os
from logging.handlers import SMTPHandler, RotatingFileHandler

app = Flask(__name__)
app.config.from_object(Config)#通知Flask读取并使用配置文件
db = SQLAlchemy(app)#Object Relational Mapper

#通过flask db init来创建mechoblog的迁移存储库，生成名为migrations的新目录
#数据库迁移，数据模型修改，需使用 flask db migrate -m "messages",flask db
# #migrate命令不会对数据库进行任何更改，只会生成迁移脚本。
#要将更改应用到数据库，必须使用flask db upgrade命令。
#flask db downgrade命令可以回滚上次的迁移
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'
#强制用户在查看应用的特定页面之前登录。如果未登录的用户尝试查看受保护的页面，Fl
#ask-Login将自动将用户重定向到登录表单，并且只有在登录成功后才重定向到用户想查
#看的页面

if not app.debug:
    # if app.config['MAIL_SERVER']:
    #     auth = None
    #     if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
    #         auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
    #     secure = None
    #     if app.config['MAIL_USE_TLS']:
    #         secure = ()
    #     mail_handler = SMTPHandler(
    #         mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
    #         fromaddr='no-reply@' + app.config['MAIL_SERVER'],
    #         toaddrs=app.config['ADMINS'], subject='Microblog Failure',
    #         credentials=auth, secure=secure
    #     )
    #     mail_handler.setLevel(logging.ERROR)
    #     app.logger.addHandler(mail_handler)

        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/mechoblog.log', maxBytes=10240,
                                           backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('mechobolg startup')

from app import routes, models, errors
