from flask import Flask, request
import config

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hua/')
def hello_hua():
    return '这是我的第一个flask页面'


@app.route('/list/<aid>/')
def article_list(aid):
    return '这是第{}篇文章'.format(aid)


@app.route('/list/<path:aid>/')
def article_detail(aid):
    return 'detail-这是第{}篇文章'.format(aid)


@app.route('/<any(article, blog):url_path>/')
def item(url_path):
    return url_path


@app.route('/wd/')
def baidu():
    return request.args.get('name')


if __name__ == '__main__':
    # app.debug = True
    # app.run(debug=True)
    app.config.from_object(config)
    app.run()
