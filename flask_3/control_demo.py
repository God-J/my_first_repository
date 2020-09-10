from flask import Flask, render_template
import config
from datetime import datetime

app = Flask(__name__)

# 模板文件自动更新
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    context = {
        'username': 'hua',
        'books': ['python', 'java', 'php'],
        'users': {
            'name': 'hua',
            'age': 18,
            'address': 'zs'
        }
    }
    return render_template('if_for.html', **context)


@app.route('/macro/')
def macro():
    return render_template('macro.html')


@app.route('/detail/')
def detail():
    return render_template('detail.html')


if __name__ == '__main__':
    app.config.from_object(config)
    app.run()
