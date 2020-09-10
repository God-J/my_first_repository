from flask import Blueprint, render_template

# 在寻找模板文件的时候会优先寻找templates目录下的文件，如果没有才会看template_folder是否有传入参数
news_bp = Blueprint('news', __name__, url_prefix='/news', template_folder='lgcoder', static_folder='static')


@news_bp.route('/')
def news():
    # return '新闻首页'
    return render_template('news.html')