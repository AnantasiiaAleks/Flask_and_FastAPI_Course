from flask import Flask, flash, redirect, render_template, request,url_for

app = Flask(__name__)
app.secret_key = b'b8fec7f506651023ed1c11bfee1fbf3af99a523f2816d2690ed6e38bdb3e9303'


"""
Генерация надежного секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""



@app.route('/')
def index():
    return 'Hi!'

@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Обработка данных формы
        flash('Форма успешно отправлена', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)