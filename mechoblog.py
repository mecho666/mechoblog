from app import app, db
from app.models import User, Post

#开发应用时，你经常会在Python shell中测试，所以每次重复上面的导入都会变得枯燥乏味。 
#flask shell命令是flask命令集中的另一个非常有用的工具。
#通过添加数据库实例和模型来创建了一个shell上下文环境
#装饰器将该函数注册为一个shell上下文函数
#当flask shell命令运行时，它会调用这个函数并在shell会话中注册它返回的项目。
@app.shell_context_processor
def make_shell_context():
    return{'db':db, 'User':User, 'Post':Post}