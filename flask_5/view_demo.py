from flask import Flask, render_template, url_for, views
from flask import request, jsonify
import config

app = Flask(__name__)
# 模板文件自动更新
app.config['TEMPLATES_AUTO_RELOAD'] = True


# 登录之后才能访问的装饰器
def login_required(func):
    def wrapper(*args, **kwargs):
        username = request.args.get('username')
        if username:
            return func(*args, **kwargs)
        else:
            return '请先登录'
    return wrapper


@app.route('/settings/')
@login_required
def setting():
    return '个人中心设置'


@app.route('/')
def index():
    # 如果app.add_url_rule给了endpoint，相当于给url起了一个名字
    print(url_for('geren'))
    return '首页'


# def profile():
#     return '个人中心'


class ListView(views.View):
    # 类视图必须重写dispatch_request
    def dispatch_request(self):
        return '类视图'


# 返回json的数据
class JsonView(views.View):

    def get_response(self):
        raise NotImplementedError()

    def dispatch_request(self):
        response = self.get_response()
        return jsonify(response)


class ListJsonView(JsonView):
    def get_response(self):
        return {"username": "hua"}


# 返回公共的变量
class BaseView(views.View):
    def __init__(self):
        super().__init__()

        self.context = {
            'name': 'hua'
        }


# class LoginView(BaseView):
#     def dispatch_request(self):
#
#         return render_template('login.html', **self.context)


class RegistView(BaseView):
    def dispatch_request(self):

        return render_template('regist.html', **self.context)


class LoginView(views.MethodView):
    # 调度方法的视图
    def get(self, error=None):
        return render_template('login.html', error=error)

    def post(self):
        name = request.form.get('name')
        password = request.form.get('password')
        error = '密码错误'
        # 查询数据库，验证输入是否正确
        if name == 'hua' and password == '123':
          return '登陆成功'
        else:
            return self.get("账号密码错误")


class ProfileView(views.View):
    # 在类中用装饰器
    decorators = [login_required]
    def dispatch_request(self):
        return '个人页面'

# 添加url规则
# app.add_url_rule('/profile/', endpoint='geren',  view_func=profile)
app.add_url_rule('/list/', view_func=ListView.as_view('list2'))
# 标准类视图
app.add_url_rule('/listjson/', view_func=ListJsonView.as_view('listjson'))
# app.add_url_rule('/login/', view_func=LoginView.as_view('login'))
app.add_url_rule('/regist/', view_func=RegistView.as_view('regist'))
app.add_url_rule('/login/', view_func=LoginView.as_view('login'))
app.add_url_rule('/profile/', view_func=ProfileView.as_view('profile'))
if __name__ == '__main__':
    app.config.from_object(config)
    app.run()