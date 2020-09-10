from flask import Flask, url_for, request, redirect, Response, make_response
import config

app = Flask(__name__)


@app.route('/')
def index():
    # 根据函数的名字，进行反转，得到函数对应的路由.需要参数则传参数进去
    print(url_for('article_list', aid=3))
    return 'hello world'


@app.route('/article/<aid>/')
def article_list(aid):
    return 'article list {}'.format(aid)


@app.route('/detail/<did>/')
def detail_list(did):
    print(url_for('index'))
    return 'detail list {}'.format(did)

# 默认都是接收GET请求
@app.route('/login', methods=['GET', 'POST'])
def login():
    # GET请求 参数在url中
    # POST请求 参数没有直接体现在URL地址中
    print(type(request.args))  # 应该是字典类型
    print(request.args.get('username'))  # GET请求接收参数
    print(request.form.get('username'))  # POST请求接收参数
    return 'login'


# 页面重定向 登录
@app.route('/login_/')
def login_():
    return 'login_'


@app.route('/profile/')
def profile():
    name = request.args.get('name')

    if name:
        return name
    else:
        # 重定向到登录页面
        return redirect(url_for('login_'), 302)


@app.route('/about/')
def about():
    # # 不能返回列表
    # return {'name': 'hua'}
    # # 只返回第一个元素
    # return ('name', 'python')
    # return Response('关于我们', status=200, mimetype='text/html')
    return make_response('关于我们')



if __name__ == '__main__':
    app.config.from_object(config)
    app.run()