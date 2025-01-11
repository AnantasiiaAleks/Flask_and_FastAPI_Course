from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/users/')
def users():
    _users = [{'name': 'Никита',
               'mail': 'nik@mail.ru',
               'phone': '+7-573-883-09-98',
               },
              {'name': 'Степан',
               'mail': 'ste@mail.ru',
               'phone': '+7-909-345-87-63',
               },
              {'name': 'Джайна',
               'mail': 'dja@mail.ru',
               'phone': '+7-846-382-93-46',
               },
              ]

    context = {'users': _users,
               'title': 'Точечная нотация'}
    return render_template('users.html', **context)


if __name__ == '__main__':
    app.run(debug=True)