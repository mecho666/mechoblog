import os
basedir = os.path.abspath(os.path.dirname(__file__))#项目的绝对路径

class Config(object):
    #Flask及其一些扩展使用密钥的值作为加密密钥，用于生成签名或令牌。
    #保护网页表单免受名为Cross-Site Request Forgery或CSRF（发音为“seasurf”）的恶意攻击。
    #在开发阶段，安全性要求较低，因此可以直接使用硬编码字符串。
    #但是，当应用部署到生产服务器上的时候，我将设置一个独一无二且难以揣摩的环境变量，
    #这样，服务器就拥有了一个别人未知的安全密钥了。
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    #配置数据库信息
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    #配置项用于设置数据发生变更之后是否发送信号给应用
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    #MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USE_TLS = True
    MAIL_USE_SSL = True  # qq邮箱需使用ssl，默认为Flase
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')#填写授权码
    ADMINS = ['wy553171@qq.com']
