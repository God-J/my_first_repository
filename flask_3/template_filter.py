from flask import Flask, render_template
import config
from datetime import datetime

app = Flask(__name__)

# 模板文件自动更新
app.config['TEMPLATES_AUTO_RELOAD'] = True


# 自定义模板过滤器
@app.template_filter('my_cut')
def cut(value):
    return value.replace('hhh', '')


@app.template_filter('handle_time')
def handle_time(time):
    if isinstance(time, datetime):
        now = datetime.now()
        timestamp = (now - time).total_seconds()
        # 小于60秒显示刚刚
        if timestamp < 60:
            return '刚刚'
        # 大于60秒小于一个小时显示多少分钟之前
        elif timestamp >= 60 and timestamp <= 60*60:
            return '%s分钟之前' % int(timestamp/60)
        # 大于一个小时小于一天则显示多少个小时之前
        elif timestamp >= 60*60 and timestamp <= 60*60*24:
            return '%s小时之前' % int(timestamp/(60*60))


@app.route('/')
def index():
    context = {
        'username': 'hhhhell',
        'age': -18,
        'name': 'jiang',
        'es': '<script>alert("hello");</script>',
        'h1': '<h1>hello</h1>',
        'books': ['python', 'java', 'php'],
        'now_time': datetime(2020, 9, 7, 22)
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.config.from_object(config)
    app.run()
