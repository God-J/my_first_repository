from flask import Flask, render_template
import config

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'username': 'GodJ',
        'age': 18,
        'books': {
            'python': 33,
            'java': 22
        },
        'book': ['python', 'java']
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.config.from_object(config)
    app.run()
