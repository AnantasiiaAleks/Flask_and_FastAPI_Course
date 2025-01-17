from flask import Flask, flash, redirect, render_template, request,url_for

app = Flask(__name__)
app.secret_key = b'0b6b6253d9396989f03fd74eadb5f3260d2fcfb38a66e9fea3a2ac6c28d3a75b'


@app.route('/')
def index():
    return 'Hi!'

@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Обработка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        # Обработка данных формы
        flash('Форма успешно отправлена', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)