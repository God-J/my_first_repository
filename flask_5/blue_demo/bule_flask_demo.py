from flask import Flask, render_template, url_for
from blueprints.news import news_bp
from blueprints.book import book_bp
from blueprints.cms import cms_bp
import config

app = Flask(__name__)
app.register_blueprint(news_bp)
app.register_blueprint(book_bp)
app.register_blueprint(cms_bp)
# 模板文件自动更新
app.config['TEMPLATES_AUTO_RELOAD'] = True

# 更改host文件
# C:\Windows\System32\drivers\etc
# 127.0.0.1 => j.com
# 127.0.0.1 => cms.j.com
# flask 不支持 IP形式 localhost
# 进行这个改动之后，在这个项目里面无法再访问到127.0.0.1：5000
# app.config['SERVER_NAME'] = 'j.com:5000'


@app.route('/')
def index():
    print(url_for('news.news'))
    print(url_for('book.book_detail', bid=2))
    return '首页'


if __name__ == '__main__':
    app.config.from_object(config)
    app.run()