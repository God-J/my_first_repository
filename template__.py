from flask import Flask, render_template
import config

app = Flask(__name__)
# 模板文件自动更新
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.config.from_object(config)
    app.run()